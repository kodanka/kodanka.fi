import os
from bs4 import BeautifulSoup


bs = lambda x: BeautifulSoup(x, 'html.parser')

forms = {
    "inledning": "https://docs.google.com/forms/d/e/1FAIpQLSffI7Jy2O-49nxunVk3OHKpr4XeypX9OSQFFzX1Sg0lf5nZBA/viewform?embedded=true",
    "listor": "https://docs.google.com/forms/d/e/1FAIpQLSeb6ntlHgATI0pLBQ0w3KD6-iQeRVavkDAV_yRb8FKnZLFPtQ/viewform?embedded=true"
}

for root, dirs, files in os.walk("_build"):

    for file in files:

        if file.endswith(".html"):

            filename = f"{root}/{file}"
            print(filename)
            if "/" in root:
                name = root.split("/")[1]
                notebook = f"{name}.ipynb"
            else:
                notebook = "index.ipynb"

            # Open all html files for modification
            with open(filename, "r") as page:
                soup = bs(page)

                # Change HTML title
                titlename = soup.find("a", attrs={"class": "current reference internal"})
                if titlename:
                    soup.title.string = f"Kodanka - {titlename.text.strip()}"
                else:
                    soup.title.string = "Kodanka"

                # Translate navigation buttons to swedish
                navigation = soup.find("div", attrs={"aria-label": "footer navigation"})
                if navigation:
                    next_button = navigation.find("a", attrs={"accesskey": "n"})
                    if next_button:
                        next_button.clear()
                        next_button.insert(0, "Nästa ")
                        next_arrow = soup.new_tag("span", attrs={"class": "fa fa-arrow-circle-right"})
                        next_button.insert(1, next_arrow)
                        navigation.insert(1, next_button)
                    previous_button = navigation.find("a", attrs={"accesskey": "p"})
                    if previous_button:
                        previous_button.clear()
                        previous_arrow = soup.new_tag("span", attrs={"class": "fa fa-arrow-circle-left"})
                        previous_button.insert(0, previous_arrow)
                        previous_button.insert(1, " Föregående")
                        navigation.insert(0, previous_button)

                # Copyright info
                copyright = soup.new_tag("div", attrs={"role": "contentinfo"})
                copyright.insert(0, soup.new_tag("p"))
                copyright.string = "© Copyright 2020, Kodanka"

                # Insert into footer
                footer = soup.find("footer")
                footer.clear()
                if navigation:
                    footer.insert(0, navigation)
                footer.insert(1, soup.new_tag("hr"))
                footer.insert(2, copyright)

                # Translate search functionality to swedish
                soup = bs(str(soup).replace("placeholder=\"Search docs\"", "placeholder=\"Sök\""))

                # Modify page header
                if os.path.isfile(notebook):
                    colab = soup.new_tag("a",
                        target="_blank",
                        rel="noopener noreferrer",
                        href=f"https://colab.research.google.com/github/kodanka/kodanka.fi/blob/master/{notebook}")
                    colab_icon = soup.new_tag("img",
                        alt="Öppna i Colab",
                        src="../_static/colab-badge.svg",
                        style="width: 117px; height: 20px;")
                    colab.insert(0, colab_icon)
                    wy_list = soup.find("ul", attrs={"class": "wy-breadcrumbs"}).find_all("li")
                    if wy_list:
                        for li in wy_list:
                            li.decompose()
                        soup.find("ul", attrs={"class": "wy-breadcrumbs"}).insert(0, colab)
                else:
                    header = soup.find("div", attrs={"aria-label": "breadcrumbs navigation"})
                    if header:
                        header.decompose()

                # Insert python console
                if os.path.isfile(notebook):
                    footer = soup.find("footer")
                    console_header = soup.new_tag("h2")
                    console_header.string = "Python kompilator"
                    footer.insert_before(console_header)
                    console = soup.new_tag("iframe", 
                        style="border: none; width: 100%; height: 500px; padding-bottom: 20px;",
                        scrolling="no",
                        frameborder="no",
                        allowtransparency="true",
                        allowfullscreen="true",
                        sandbox="allow-forms allow-pointer-lock allow-popups allow-same-origin allow-scripts",
                        src="https://repl.it/@kodanka/python?lite=true")
                    footer.insert_before(console)

                # Insert forms
                if os.path.isfile(notebook):
                    try:
                        src = forms[name]
                        footer = soup.find("footer")
                        form_header = soup.new_tag("h2")
                        form_header.string = "Quiz"
                        footer.insert_before(form_header)
                        form = soup.new_tag("iframe",
                            style="border: none; width: 100%; height: 500px; padding-bottom: 20px;",
                            src=src)
                        footer.insert_before(form)
                    except KeyError as e:
                        print(e, "lacks form")

            with open(filename, "w") as page:
                # Write changes
                page.write(str(soup))

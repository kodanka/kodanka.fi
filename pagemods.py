import os
from bs4 import BeautifulSoup


bs = lambda x: BeautifulSoup(x, 'html.parser')

for root, dirs, files in os.walk("_build"):

    for file in files:

        if file.endswith(".html"):

            filename = f"{root}/{file}"
            name = file.split(".")[0]
            notebook = f"{name}.ipynb"

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
                next_button = soup.find("a", attrs={"accesskey": "n"})
                if next_button:
                    next_button.clear()
                    next_button.insert(0, "Nästa")
                    next_arrow = soup.new_tag("span", attrs={"class": "fa fa-arrow-circle-right"})
                    next_button.insert(1, next_arrow)
                previous_button = soup.find("a", attrs={"accesskey": "p"})
                if previous_button:
                    previous_button.clear()
                    previous_button.insert(1, "Föregående")
                    previous_arrow = soup.new_tag("span", attrs={"class": "fa fa-arrow-circle-left"})
                    previous_button.insert(0, previous_arrow)

                # Translate search functionality to swedish
                soup = bs(str(soup).replace("placeholder=\"Search docs\"", "placeholder=\"Sök\""))

                # Modify page footer
                old_footer = "Built with <a href=\"http://sphinx-doc.org/\">Sphinx</a> using a <a href=\"https://github.com/rtfd/sphinx_rtd_theme\">theme</a> provided by <a href=\"https://readthedocs.org\">Read the Docs</a>."
                new_footer = "Byggt med <a href=\"http://sphinx-doc.org/\">Sphinx</a> med ett <a href=\"https://github.com/rtfd/sphinx_rtd_theme\">tema</a> av <a href=\"https://readthedocs.org\">Read the Docs.</a>"
                soup = bs(str(soup).replace(old_footer, new_footer))

                # Modify page header
                if os.path.isfile(f"{name}.ipynb"):
                    colab = bs(f"<a target=\"_blank\" rel=\"noopener noreferrer\" \
                                href=\"https://colab.research.google.com/github/kodanka/kodanka.fi/blob/master/{notebook}\"> \
                                <img alt=\"Öppna i Colab\" src=\"_static/colab-badge.svg\" style=\"width:117px;height:20px;\"/></a>")
                    wy_list = soup.find("ul", attrs={"class": "wy-breadcrumbs"}).find_all("li")
                    if wy_list:
                        for li in wy_list:
                            li.decompose()
                        soup.find("ul", attrs={"class": "wy-breadcrumbs"}).insert(0, colab)
                else:
                    header = soup.find("div", attrs={"aria-label": "breadcrumbs navigation"})
                    if header:
                        header.decompose()

            with open(filename, "w") as page:
                # Write changes
                page.write(str(soup.prettify()))

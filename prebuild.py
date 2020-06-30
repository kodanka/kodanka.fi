import os
import nbformat as nbf

for file in os.listdir("."):
    if file.endswith(".ipynb"):
        with open(file) as f:
            nb = nbf.read(f, as_version=4)
            if any(cell["source"] == "## Quiz" for cell in nb.cells):
                print("Headers already in", file)
                continue
            nb.cells.append(nbf.v4.new_markdown_cell(source="## Konsol"))
            nb.cells.append(nbf.v4.new_markdown_cell(source="## Quiz"))

        with open(file, "w", encoding="utf-8") as f:
            nbf.write(nb, f)
            print("Headers added to", file)

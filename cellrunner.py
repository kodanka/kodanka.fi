import os
from nbformat import read, write
from nbconvert.preprocessors import ExecutePreprocessor
ep = ExecutePreprocessor(timeout=600, kernel_name="python3", allow_errors=True)

def set_colab_name(file):
    with open(file) as f:
        nb = read(f, as_version=4)
        nb.metadata.colab = {"name": file}

    with open(file, "w", encoding="utf-8") as f:
        write(nb, f)

def calls_input(file):
    with open(file) as f:
        nb = read(f, as_version=4)
        cells = nb.cells
        code_cells = [c for c in cells if c.cell_type == "code"]
        for cell in code_cells:
            if "input(" in cell.source:
                return True
        return False

for file in os.listdir("."):
    if file.endswith(".ipynb"):
        set_colab_name(file)
        # skip running cells if input is called in notebook
        if calls_input(file):
            print("Skip", file)
            continue
        with open(file) as f:
            nb = read(f, as_version=4)
            ep.preprocess(nb)

        with open(file, "w", encoding="utf-8") as f:
            write(nb, f)
            print("Ran", file)

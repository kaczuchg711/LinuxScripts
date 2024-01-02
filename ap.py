import os
import pathlib


def _create_new_PATH_line(newSinglePath, i):
    new_line = line[:] + ":" + newSinglePath
    lines[i] = new_line
    print("add " + newSinglePath + " to PATH")

def _add_line_with_PATH():
    f.seek(0, 1)
    f.write("\nexport PATH=$PATH" + ":" + newSinglePath)
    print("add " + newSinglePath + " to PATH")

newSinglePath = os.getcwd()

with open(pathlib.Path.home().__str__() + '/.bashrc', 'r+') as f:
    lines = f.readlines()
    foundLineWithPATH = False
    for i, line in zip(range(len(lines)), lines):
        if "export PATH=$PATH" in line:
            foundLineWithPATH = True
            if newSinglePath not in line:
                _create_new_PATH_line(newSinglePath, i)
                break
            else:
                print(newSinglePath + " already in PATH")
    if not foundLineWithPATH:
        _add_line_with_PATH()
    else:
        f.seek(0)
        f.writelines(lines)

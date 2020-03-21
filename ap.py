import os
import pathlib

str = os.getcwd()
f = open(pathlib.Path.home().__str__() + '/.bashrc', 'r+')
f.seek(0,2)
f.write(':' + str)
f.close()

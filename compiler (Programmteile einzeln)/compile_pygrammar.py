import os

t_antlr= os.path.getmtime('py.g4')
t_py= os.path.getmtime('pyParser.py')
if t_antlr>t_py:
    os.system('java org.antlr.v4.Tool -Dlanguage=Python2 py.g4')

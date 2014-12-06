from pylex.space2braces import space2braces
from antlr2py import pytree

def compile_grammar():
    t_antlr= os.path.getmtime('py.g4')
    t_py= os.path.getmtime('pyParser.py')
    if t_antlr>t_py:
        os.system('java org.antlr.v4.Tool -Dlanguage=Python2 py.g4')

def py2cpp(prog):
    prog= 'program.py'
    prog_= space2braces(prog)
    AST= pytree(prog_)
    AST.tofile(prog.replace('.py', '.cpp'))

    return AST #zur Kontrolle

if __name__=='__main__':

    prog= 'program.py'
    AST= py2cpp(prog)

    #Kontrollausgaben
    print '---------------------- Python Programm ------------------------\n'
    print open(prog).read()
    print '---------------------- Parsetree Text  ------------------------\n'
    print AST.root.ot()
    print '---------------------- C++ Programm ---------------------------\n'
    print AST.root.text()

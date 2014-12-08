from pylex.space2braces import space2braces
from antlr2py import pytree

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

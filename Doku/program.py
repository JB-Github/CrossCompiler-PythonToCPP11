from __future__ import division

"""
Test program  for codegeneration
"""

def f(x):
    """calculate"""
    return x**2 + x*4 - (x-3) /x -1.3e2+2\
           +5 #comment



if __name__=='__main__':

    L= [0]*10 #(*\label{array_decl}*)

    for i in range(len(L)):
        if i>3:
            L[i]= f(i+1)
        else:
            L[i]+=1

    for x in L:
        print x

    print 'program', 'end'

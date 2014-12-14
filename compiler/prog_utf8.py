from __future__ import division

"""
Test
"""

def g(x):
    """c"""
    return x + 2*x*x**3

if __name__=='__main__':

    L= [0]*7

    for i in range(len(L)-2):
        L[i]= g(i**2)

    for x in L:
        print x
        




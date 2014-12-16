from __future__ import division;

"""
Test
""";

def g(x):$blockbegin
    """c""";
    return x + 2*x*x**3;
$blockend

if __name__=='__main__':$blockbegin

    L= [0]*7;

    for i in range(len(L)-2):$blockbegin
        L[i]= g(i**2);
    $blockend

    for x in L:$blockbegin
        print x;
    $blockend
$blockend





from __future__ import division;

"""
Test program  for codegeneration
""";

def f(x):$blockbegin
    """calculate""";
    return x**2 + x*4 - (x-3) /x -1.3e2+2\
           +5;
$blockend #comment



if __name__=='__main__':$blockbegin

    L= [0]*10;

    for i in range(len(L)):$blockbegin
        if i>3:$blockbegin
            L[i]= f(i+1);
        $blockend
        else:$blockbegin
            L[i]+=1;
        $blockend
    $blockend

    for x in L:$blockbegin
        print x;
    $blockend

    print 'program', 'end';
$blockend


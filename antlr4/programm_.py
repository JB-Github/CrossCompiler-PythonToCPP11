from __future__ import division;


"""
Testprogramm fuer codegen
""";

def f(x):$blockbegin
    """rechnen""";
    return x**2 + x*4 - (x-3) /x -1.3e2+2\
           +5; #comment
$blockend



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
$blockend

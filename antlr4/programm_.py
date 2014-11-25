
def f(x):$blockbegin
    """rechnen""";
    return x**2 + x*4 - (x-3) /x -1.3e4+2\
           +5; #comment
$blockend

#S= 'gd\'gf';#


L= [0]*10;

for i in range(len(L)):$blockbegin
    if i>3:$blockbegin
    	L[i]= f(i+1);
    $blockend
    else:$blockbegin
        pass;
    $blockend
$blockend

print L;


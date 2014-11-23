
def f(x):$blockbegin
    """rechnen""";
    return x**2 + x*4 - (x-3) /x -1.3e4+2\
           +5; #COMM
$blockend
#S= 'gd\'gf';#
#T= "'g$d\'gf'\n";
#U= "'gd\'gf";#




L= [0]*10;

for i in range(len(L)):$blockbegin
    if i>3:$blockbegin
    	L[i]= f(i+1);
    $blockend
    else:$blockbegin
        pass;
    	#pa.a.b;
    $blockend
$blockend

print L;

#2>=1 >3<4;
#{'a':1,r"""b""":2};

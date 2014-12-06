#include <cmath>
#include <array>
#include <iostream>

using namespace std;

/*

Testprogramm fuer codegen

*/

double f(double x) {
    /*rechnen*/
    return pow(x, 2)+ x*4 - (x-3) / x -1.3e2+2
           +5; //comment

}

//S= "abc\n";

int main() {

    array<double,10> L={};

    for (int i= 0; i<L.size(); i++) {
        if (i>3) {
        	L[i]= f(i+1);
        }
        else {
            L[i]++;
        }
    }

    for (auto x : L) {
        cout<< x << endl;
    }

    return 0;

}

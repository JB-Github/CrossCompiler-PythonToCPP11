#include <array>
#include <cmath>
#include <iostream>

using namespace std;

/*
Test program  for codegeneration
*/

double f(double x) {
    /*calculate*/
    return pow(x, 2)+ x*4 - (x-3) /(double) x-1.3e2+2
           +5; //comment
}



int main() {

    array<double,10> L={};

    for (int i= 0; i<L.size(); i++) {
        if (i>3) {
            L[i]= f(i+1);
        }
        else {
            L[i]++; // com
        }
    }

    for (auto x : L) {
        cout<< x << endl;
    }

    cout<< "program" <<' '<< "end" << endl;

    return 0;

}

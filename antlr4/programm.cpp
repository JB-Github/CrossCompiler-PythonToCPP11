#include <iostream>
#include <cmath>
#include <array>
using namespace std;

template <typename T>
double f(T x) {
  /*rechnen*/
  return pow(x, 2) + x*4 - (x-3) /(double)x -1.3e4+2
           +5; //comment
}



int main(){

  //S= 'gd\'gf';#


  array<double, 10> L= {};


  for (int i= 0; i<L.size(); i++) {
      //cout<< L[i]<<endl;
      if (i>3) {
	      L[i]= f(i+1);
      }
      else {
	  ;
      }
      //cout<< L[i]<<endl;
  }

  cout<< L[0]<< endl;


  return 0;
}
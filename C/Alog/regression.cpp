#include <math.h>
#include<iostream>

using namespace std;
int func ( int x ){
    
    if (x == 0 ) return 0;
    else return (2*func(x-1)+x^2);

}

int main(){

    for(int i;i<=10;i++){
        cout << func(i) << endl;
    }
}
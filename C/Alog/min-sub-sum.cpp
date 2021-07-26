#include <iostream>
# define LENGTH_OF_A 99
int main(){

    int A[99] ;
    /*  Read a sequence from somewhere ,make it A[]  */
    
    
    int Res;
    for (int i; i <= LENGTH_OF_A ;i++)
        if (A[i] < 0  )
            Res += A[i];
        else if ( (Res + A[i]) >= 0 )
            break;

    return Res;




}
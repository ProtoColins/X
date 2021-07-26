#include <stdio.h>
 
int main (){
    char c ;
    int Once = 1;
    while( ( c = getchar() ) != "\n") 
        if ( c == ' '){
            if ( Once == 1 ){
                putchar(' ');
                Once = -1;
            }
        }
        else{
            printf("%c",c);
            Once = 1;
        }





}
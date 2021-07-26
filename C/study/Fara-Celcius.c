#include <stdio.h>

#define Lower  0
#define Upper  70
#define Step  10


int main(){
    float farh = Lower;
    float cel;
    
    while (farh <= Upper){
        cel = (5.0/9.0)*farh - 32;
        
        printf("%03.1f \t %03.1f\n",farh,cel);

        farh += Step;
    }

}
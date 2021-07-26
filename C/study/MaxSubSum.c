#include<stdio.h>
#include<stdlib.h>

//Get Max SubSum with ? alog



int main( ){
// Given list

int list[100] = {7,2,-5,-2,0,-1,0,7,7,-1,4,2,-4,-2,3,-3,5,-1,3,2,-3,0,4,3,4,3,-4,1,0,6,-3,7,-2,-3,-3,7,4,0,5,6,-1,-1,3,6,4,7,-5,6,7,4,7,6,6,-3,-3,-2,2,4,4,4,6,-3,1,6,1,2,5,1,2,4,5,3,3,4,4,3,-4,-4,3,-5,7,5,-2,7,-4,-1,-3,0,5,-2,-4,-3,5,2,6,-3,-2,1,1,-3};
int fuckyouC = 0 ;

printf(" Please state Subline length  = ");
scanf("%d" , &fuckyouC);

int aicbeus = 0 ;
long int qmsoxsv = 0 ;
int sabfivywr = 0;

    for ( sabfivywr ; sabfivywr <= fuckyouC; sabfivywr++){

        if ( list[sabfivywr] < 0 ){
            // check two results
            if ( aicbeus > qmsoxsv ){
                qmsoxsv = aicbeus;
            }
            else aicbeus = 0;
        }
        else aicbeus += list[sabfivywr];

    }
printf(" %d " , fuckyouC);
printf(" %d " , qmsoxsv );

system("pause");

return 0;
}


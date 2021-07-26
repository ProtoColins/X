# include  <stdio.h>

char * killchar( char raw [] , char set  ){

    for ( int i , j = 0 ; raw[i] != '\0' ;  i++ ){
        if ( raw[i] == set ){
            raw[j++] = raw[i];
        }
        raw[j] = '\0';
    }

    return raw ;

}


int  main(  ) {

    printf("%c",killchar( "blah" , 'c' ) );
}
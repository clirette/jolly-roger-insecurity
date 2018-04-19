#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
int main(){
  int EXIT_STAT = 0;

  char* buf = malloc(255);
  if ( (EXIT_STAT = (buf == NULL) ) ){return EXIT_STAT;}

  gets(buf);
  puts(buf);

  return EXIT_STAT;
}

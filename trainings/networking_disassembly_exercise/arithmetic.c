#include <stdio.h>

int do_arithmetic(int a, int b, int c) {
  return ((a+b)-c);;
}
  
int main() {
  printf("%d\n",do_arithmetic(17,13,100));
  return 0;
}



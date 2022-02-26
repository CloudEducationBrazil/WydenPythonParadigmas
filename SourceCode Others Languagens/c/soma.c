#include <stdio.h>
#include <locale.h>

int main(void){
  setlocale(LC_ALL, "Portuguese");
  double n1, n2, avarage;

  printf("Digite número 1: "); scanf("%lf", &n1);
  printf("Digite número 2: "); scanf("%lf", &n2);

  avarage = ( n1 + n2 ) / 2.0;
  printf("\nResultado = %.2lf", avarage);
}

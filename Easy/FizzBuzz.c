#include <stdio.h>

int main(int argc, char* argv[])
{
  int num, end;
  int n1, n2, n3;
  FILE *in;

  in = fopen(argv[1], "r");
  end = fscanf(in, "%i", &n1);
  while(end != EOF)
  {
    fscanf(in, "%i", &n2);
    fscanf(in, "%i", &n3);
    num = 1;
    while(num <= n3)
    {
      if(num % n1 == 0 && num % n2 == 0)
      {
        printf("FB");
      }
      else if(num % n1 == 0)
      {
        printf("F");
      }
      else if(num % n2 == 0)
      {
        printf("B");
      }
      else
      {
        printf("%i", num);
      }
      printf(" ");
      num++;
    }
    printf("\n");
    end = fscanf(in, "%i", &n1);
  }
  return 0;
}


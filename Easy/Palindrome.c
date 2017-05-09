#include <stdio.h>
#include <math.h>

//Check if a number is palindrome
int is_palindrome(int num)
{
  int i = 0;
  int size = 1;
  while(num/pow(10, size) >= 1)
  {
    size++;
  }

  while(i < size/2)
  {
    int endNum = ((int) num % ( (int) pow(10, i + 1)) / ((int) pow(10, i))) ;
    int beginNum = ((int) (num/(int)pow(10, size-i-1))) % 10;

    if(endNum != beginNum)
    {
      return 0;
    }
    i++;
  }
  return 1;
}

int is_prime(int num)
{
  int i = 3;
  while(i < sqrt(num) + 1)
  {
    if(num%2 == 0 || num%i == 0)
    {
      return 0;
    }
    i+=2;
  }
  return 1;
}

int main(void) {

  int i[200], size = 1, n = 3, j;

  i[0] = 2;

  //Get all the primes
  while(n < 1000)
  {
    if(is_prime(n))
    {
      i[size++] = n;
    }
    n+=2;
  }

  for(j = size-1; j>0; j--)
  {
    if(is_palindrome(i[j]))
    {
      printf("%i", i[j]);
      return 0;
    }
  }
}


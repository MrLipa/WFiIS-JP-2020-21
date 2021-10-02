#include "funkcja.h"

void insert_sort(int* tab,int size)
{
  int j=0;
  int temp=0;
  for(int i=0;i<size;i++)
  {
    temp=tab[i];
    j=i-1;
    while (j>0 && tab[j]>temp)
    {
      tab[j+1]=tab[j];
      j=j-1;
    };
    tab[j+1]=temp;
  }
}

int nwd(int a,int b)
{
  if(b==0)
  {
    return a;
  }
  else
  {
    return nwd(b,a%b);
  }
}
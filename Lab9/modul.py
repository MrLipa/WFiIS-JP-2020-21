import math
import random
import string

##########1##########

def pascal(n):
  '''Dokumentacja generator liczb paskala przyjmuje parametr ile tych licz b trza wygenerować'''
  l = [1]
  yield l
  for i in range(n):
      l1 = []
      a = 0
      for i in l:
          l1.append(a + i)
          a = i
      l1.append(1)
      l = l1
      yield l

def fun1(n):
  '''Dokumentacja
funkcja wypisująca na ekran trójkat pascala
'''
  suma=0
  for i,j in enumerate(pascal(n)):
    if i==n:
      for k in j:
        suma+=int(math.log10(k))+1
  print(f'Trójkąt Pascala dla n={n}'.center(n+suma+1))
  for i in pascal(n):
    napis=' '.join(str(j) for j in i)
    print(napis.center(n+suma+1))
##########2##########

def euler(n,k):
  '''Dokumentacja
generator liczb eulera przyjmuje parametr ile tych liczb trza wygenerować
'''
  if k>=n or n==0:
    return 0
  if k==0:
    return 1
  return (k+1)*euler(n-1,k)+(n-k)*euler(n-1,k-1)

def fun2(n):
  '''Dokumentacja
funkcja wypisująca na ekran trójkat z liczb eulera
'''
  temp=int(math.log10(euler(n-1,(n-1)//2)))+1
  for i in range(n):
    for j in range(n):
      if i==j:
        print(f'{euler(i,j)}'.ljust(temp))
      if i>j:
        print(f'{euler(i,j)}'.ljust(temp),end= " ")

def fun3(nazwa1,nazwa2,n):
  '''Dokumentacja
  funkcja szyfrująca tekst @parmetr 1 szyfrem cezara do pliku wynikowego @parametr2
  jeśli podasz
  dodatnie n przesuwa litery w tekśie o n w prawo("szyfruje")
  ujemne n przesua litery w tekście o n w lewo("deszyfruje")
  '''
  with open(nazwa1,'r') as pl1, open(nazwa2,'w') as pl2:
    line=pl1.read()
    s=line.lower()
    pl2.write(''.join((i) for i in map(lambda i: ((chr(ord(i)+n) if ord(i)+n>=97 else chr(121-n)) if ord(i)+n<=122 else chr(96+n)  ) if i in string.ascii_letters else i,s) ))

##########5##########
def fun5(nazwa1,nazwa2,nazwa3):
  '''Dokumentacja
  funkcja deszyfrująca tekst w języku polskim
  '''
  slownik1={}
  slownik2={}
  for i in string.ascii_lowercase:
    slownik1.setdefault(i,0)
    slownik2.setdefault(i,0)
  with open(nazwa2,'r') as pl:
    for line in pl:
      slownik2[line.split("\t")[0]]=float(line.split("\t")[1])
  with open(nazwa1,'r') as pl:
    line=pl.read().lower()
    for i in string.ascii_lowercase:
      slownik1[i]=line.count(i)/100
  slownik1=sorted(slownik1.items(), key=lambda x: x[1])
  slownik2=sorted(slownik2.items(), key=lambda x: x[1])
  with open(nazwa1,'r') as pl1, open(nazwa3,'w') as pl2:
    line=pl1.read()
    s=line.lower()
    pl2.write(''.join((i) for i in map(lambda i: slownik2[get_num(slownik1,i)][0] if i in string.ascii_lowercase else " ",s)))

def get_num(slownik,n):
  for i in range(len(slownik)):
    if slownik[i][0]==n:
      return i
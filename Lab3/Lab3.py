import sys


print("##########1##########")
print()

if len(sys.argv)<=1:
  print("Nie wpisałes argumentów wywołania programu")
  sys.exit(0)
string=("".join(sys.argv[1:]))
print("Wpisany ciąg znaków to: ",string)


print()
print("##########2##########")
print()

lower=[]
upper=[]
numeric=[]
other=[]
for i in string:
  if i.islower():
    lower.append(i)
  elif i.isupper():
    upper.append(i)
  elif i.isnumeric():
    numeric.append(i)
  else:
    other.append(i)
print("Lista małych znakow w zmiennej string: \n",string,lower)
print("Lista dużych znakow w zmiennej string: \n",string,upper)
print("Lista cyfr w zmiennej string: \n",string,numeric)
print("Lista innych znakow w zmiennej string: \n",string,other)


print()
print("##########3##########")
print()

lower1=[]
for i in range(len(lower)):
  if lower[i] not in lower1:
    lower1.append(lower[i])
print("Lista małych znakow w zmiennej string bez powtórzeń: \n",string,lower1)
lista=[(lower1[i],lower.count(lower1[i])) for i in range(len(lower1))]
print("Lista krotek (litera, liczba występien) w stringu: \n",string, lista)


print()
print("##########4##########")
print()

lista.sort(key=lambda x: x[1],reverse =True)
print("Lista krotek (litera, liczba występien) w porządu malejącej krotności:\n",string, lista)


print()
print("##########5##########")
print()

lista1=[]
a=0
b=0
samogloski=('a','e','i','o','u')
for i in string.lower():
  if i in samogloski:
    a+=1
b=len(lower)+len(upper)-a
print("Współcznnik a: ",a)
print("Współcznnik b: ",b)
for i in numeric:
  temp=(int(i),a*int(i)+b)
  lista1.append(temp)
print("Utworzona lista krotek (lista cyfra,a*x+b): \n",lista1)


print()
print("##########6##########")
print()

D=0
x=0
y=0
a1=0
b1=0
for i in range(len(lista1)):
  x+=int(lista1[i][0])
  y+=int(lista1[i][1])
if len(lista1)!=0:
  x=x/len(lista1)
  y=y/len(lista1)
else:
  sys.exit()
for i in range(len(lista1)):
  D+=pow(int(lista1[i][0])-x,2)
for i in range(len(lista1)):
  a1+=int(lista1[i][1])*(int(lista1[i][0])-x)
a1=a1/D
b1=y-a1*x
print("Współczynnik a prostej y=a*x+b ",a1)
print("Współczynnik b prostej y=a*x+b ",b1)
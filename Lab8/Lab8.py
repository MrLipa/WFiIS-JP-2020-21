import glob
import numpy
import string


print("##########1##########")
print()

def fun1(nazwa, a):
    with open(nazwa) as pl:
        line = pl.readlines()
        print(line[:a])
        print(line[-a:])
        print(line[::a])
        print(list(i.split(" ")[a - 1] for i in line))
        print(list(i[a - 1] for i in line))
fun1("zad1.txt", 2)


print()
print("##########2##########")
print()

def fun2():
    files = glob.glob('./data/data*')
    temp = []
    for file in files:
        with open(file) as pl:
            temp.append(pl.readlines())
    with open("zad2.txt", 'w') as pl:
        for i in range(len(temp[0])):
            pl.write(f'{i} {numpy.average([float(temp[j][i]) for j in range(len(files))])} {numpy.std([float(temp[j][i]) for j in range(len(files))])}\n')
fun2()


print()
print("##########3##########")
print()

def fun3():
    file = open("zad3.py", "w")
    file.writelines('''import matplotlib.pyplot as plt
with open("dataout.txt") as pl:
  line=pl.readlines()
  x=list( float(i.split(" ")[0]) for i in line )
  y=list( float(i.split(" ")[1]) for i in line )
  dy=list( float(i.split(" ")[2]) for i in line )
#wyrysowanie krzywej y(x), 'o' oznacza styl punktu
plt.plot(x, y, 'o')
#wyrysowanie krzywej y(x) wraz z niepewnościami
plt.errorbar(x, y, marker='*', yerr=dy)
#opis osi
plt.xlabel('x')
#zapis do pliku, format określony przez rozszerzenie w nazwie
plt.savefig('res.pdf')
  ''')
    file.close()
fun3()


print()
print("##########4##########")
print()

def fun4():
    files = glob.glob('./rank/20*')
    slownik = {}
    slownik.setdefault('Nazwisko'.ljust(10), [str(2000 + i).ljust(5) for i in range(21)])
    for file in files:
        with open(file,encoding='utf-8') as pl:
            for i in pl:
                slownik.setdefault(str(i.split(" ")[0]).ljust(10), [])
                if i.split(" ")[1] != '\n':
                    slownik[str(i.split(" ")[0]).ljust(10)].append((str(file)[7:11],str(int(i.split(" ")[1])).ljust(5)))
    with open("zad4.txt", "w") as pl:
      for i in slownik.keys():
        if i=='Nazwisko'.ljust(10):
          pl.write(f'{i}')
          for j in range(len(slownik[i])):
            pl.write(f'{slownik[i][j]}')
        else:
          pl.write(f'{i} ')
          k=0
          for j in range(len(files)):
            if len(slownik[i])==0 or k>=len(slownik[i]):
              pl.write(str("---".ljust(5)))
            elif slownik[i][k][0]==str(2000+j):
              pl.write(slownik[i][k][1])
              k+=1
            else:
              pl.write(str("---".ljust(5)))
        pl.write(f'\n')
fun4()


print()
print("##########5##########")
print()

def fun5(file):
  slownik={}
  for i in string.ascii_uppercase:
    slownik.setdefault(i,0)
  with open(file) as pl:
    for i in pl:
      for j in i.split(" "):
        if j.capitalize()[0].isalpha():
          slownik[j.capitalize()[0]]+=1
  wybor=int(input("1. Alfabetycznie\n2. Rosnąca\n3. Malejąco\nPosortuj: "))
  if wybor==1:
    print(slownik)
  elif wybor==2:
    print(dict(sorted(slownik.items(), key=lambda x: x[1])))
  elif wybor==3:
    print(dict(sorted(slownik.items(), key=lambda x: x[1], reverse=True)))

fun5("zad5A.in")
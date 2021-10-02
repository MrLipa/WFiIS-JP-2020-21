import sys
sys.path.append('build/lib.linux-x86_64-3.8')
import moddd
import random
import time


print("##########1##########")
print()

print(moddd.met(1,2))
print(moddd.met(1,2,5))
print(moddd.met(1,2,5,[2,3,4]))


print()
print("##########2##########")
print()

def insert_sort(tab,size):
  j=0
  temp=0
  for i in range(size):
    temp=tab[i]
    j=i-1
    while j>0 and tab[j]>temp:
      tab[j+1]=tab[j]
      j=j-1
    tab[j+1]=temp


n=[10,10**2,10**3]
time_python=[]
time_c=[]
for i in n:
  tab1=[random.randint(0,i) for _ in range(i)]
  tab2=[j for j in tab1]
  start=time.time()
  moddd.sort(tab1)
  koniec=time.time()
  time_c.append(koniec-start)

  start=time.time()
  insert_sort(tab2,len(tab2))
  koniec=time.time()
  time_python.append(koniec-start)

print("Czasy w Pythonie: ", time_python)
print("Czasy w C: ", time_c)


print()
print("##########3##########")
print()

dir={random.randint(10,100): random.randint(10,100) for _ in range(3)}
print(dir)
print(moddd.NWD(dir))
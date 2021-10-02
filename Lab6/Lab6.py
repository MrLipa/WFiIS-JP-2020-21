import functools
import math
import random
import time

print("##########1##########")
print()

powt=1000
N=10000

def forStatement(a):
  lista=[]
  for i in range(a):
    lista.append(i)
  return lista

def listComprehension(a):
  return [i for i in range(a)]

def mapFunction(a):
  return map(lambda x:x,range(a))

def generatorExpression(a):
  return (i for i in range(a))

def tester(fun):
  start=time.time_ns()
  for _ in range(powt):
    fun(N)
  return abs(time.time_ns()-start)

test=(forStatement, listComprehension, mapFunction, generatorExpression)

for testFunction in test:
    print(testFunction.__name__.ljust(20), '=>', tester(testFunction))

#####Wyniki#####
# forStatement         => 2068085324
# listComprehension    => 735284608
# mapFunction          => 936199
# generatorExpression  => 1053044

# forStatement         => 7394509868
# listComprehension    => 5510763323
# mapFunction          => 1198122
# generatorExpression  => 1418536

# forStatement         => 3229754115
# listComprehension    => 1975355411
# mapFunction          => 5109414128
# generatorExpression  => 3713828611

# forStatement         => 2343374514
# listComprehension    => 1005825312
# mapFunction          => 2667817095
# generatorExpression  => 1117738234

# forStatement         => 2880867832
# listComprehension    => 1028117049
# mapFunction          => 1899827923
# generatorExpression  => 1467816325


print()
print("##########2##########")
print()

def fun2(N=10000):
  return len(list(filter(lambda x: x<=1,[math.sqrt(random.uniform(-1,1)**2 +random.uniform(-1,1)**2) for i in range(N)])))/N*4
print(fun2())


print()
print("##########3##########")
print()

M1=[[1,2,3],[1,2,4],[1,2,5]]
print(list(map(lambda x: max(x),M1)))
M2=[[3,2,3],[5,2,4],[6,2,5]]
print(list(map(lambda x: max(x),zip(*M2))))
M3=[[3,2,3],[5,2,4],[6,2,5]]
M=[M1,M2,M3]
print(functools.reduce(lambda x,y: [list(map(sum,zip(*i))) for i in zip(x,y)] ,M ))


print()
print("##########4##########")
print()

lista=[[random.randint(1,5),random.randint(1,5)] for i in range(10)]
print(lista)
lista1=[list(map(lambda x:x[0],lista)),list(map(lambda x:x[1],lista))]
print(lista1)


print()
print("##########5##########")
print()

def fun5(x,y):
  sx=sum(x)/len(x)
  D=functools.reduce(lambda x,y: x+y,map(lambda x: (x-sx)**2,x))
  a=functools.reduce(lambda x,y: x+y,map(lambda x,y: y*(x-sx),x,y))/D
  sy=sum(y)/len(x)
  b=sy-a*sx
  dy=math.sqrt( functools.reduce(lambda x,y:x+y, map(lambda x,y:(y-(a*x+b))**2,x,y)) )
  da=dy/D
  db=dy*math.sqrt(1/len(x) + sx**2/D)
  return a,b,da,db
print(fun5([1,2,3,4],[1,2,3,4]))
import math
import random


print("##########1##########")
print()

def fun1_1():
    i = 0
    yield i
    while True:
        i += 1
        yield i

print("fun1_1 ", end=" ")  # przykładowe wywołanie generatora
for i in fun1_1():
    if i > 10:
        break
    print(i, end=" ")

print()

def dziel(i):
    for j in range(1, i):
        if i % j == 0:
            yield j

def fun1_2(a):
    for i in a:
        if i == sum(k for k in dziel(i)):
            yield i

print("fun1_2 ", end=" ")  # przykładowe wywołanie generatora
for i in fun1_2([2, 4, 6, 24, 28, 56, 34, 496]):
    print(i, end=" ")

print()

def fun1_3(a, b):
    for i in a:
        if i > b:
            break
        yield i

print("fun1_3 ", end=" ")  # przykładowe wywołanie generatora
for i in fun1_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5):
    print(i, end=" ")

print()

N = 100
print(f"fun1_2(fun1_3(fun1_1(),{N}) ", end=" ")
for i in fun1_2(fun1_3(fun1_1(), N)):
    print(i, end=" ")


print()
print("##########2##########")
print()

def fun2(a, u, x):
    i = 1
    temp = x
    while x != 1.5:
        u = u + a / x
        x = temp + i * a
        i += 1
        yield x, u, math.log(x)


for j in fun2(0.05, 0, 1):
    print(f"ln({j[0]})={j[1]}".ljust(30), f"ln({j[0]})={j[2]}")


print()
print("##########3##########")
print()

def fun3(a):
  x=0
  y=a
  for i in range(math.ceil((a-1)/2)):
    x+=1
    y-=1
    z=y
    lista=[]
    lista.append(x)
    lista.append(z)
    for j in range(y):
      if z<x:
        break
      yield lista
      lista.pop()
      lista.append(1)
      lista.append(z-1)
      z-=1

a = 7
print(f"Wszystkie rozkłady liczby {a}:")
for i in fun3(a):
    print(i, end=" ")


print()
print("##########4##########")
print()

def fun4():
    temp = 0
    a = random.random()
    while a > 0.1:
        temp = a
        a = random.random()
        if abs(temp - a) >= 0.4:
            yield temp, a


for i in fun4():
    print(i)


print()
print("##########5##########")
print()

def newrange(a, b=None, c=1):
    if b is None:
        b = a
        a = 0
    if c == 0:
        return
    elif c > 0 and b > a:
        while a < b:
            yield a
            a += c
    elif c < 0 and b < a:
        while a > b:
            yield a
            a += c
    else:
        return


print("newrange: ".ljust(10), list(newrange(8)))
print("range: ".ljust(10), list(range(8)))

print("newrange: ".ljust(10), list(newrange(-8)))
print("range: ".ljust(10), list(range(-8)))

print("newrange: ".ljust(10), list(newrange(1, 8)))
print("range: ".ljust(10), list(range(1, 8)))

print("newrange: ".ljust(10), list(newrange(8, 1)))
print("range: ".ljust(10), list(range(8, 1)))

print("newrange: ".ljust(10), list(newrange(1, 8, 2)))
print("range: ".ljust(10), list(range(1, 8, 2)))

print("newrange: ".ljust(10), list(newrange(1, 8, -2)))
print("range: ".ljust(10), list(range(1, 8, -2)))

print("newrange: ".ljust(10), list(newrange(8, 1, 2)))
print("range: ".ljust(10), list(range(8, 1, 2)))

print("newrange: ".ljust(10), list(newrange(8, 1, -2)))
print("range: ".ljust(10), list(range(8, 1, -2)))
import random
import scipy.misc
import math

print("##########1##########")
print()

class Fibonacci1():
  ile=0
  def __init__(self,a=0,b=1,stop=10):
    self.a=a
    self.b=b
    self.stop=10
    Fibonacci1.ile=0
  def __iter__(self):
    return self
  def __next__(self):
    if Fibonacci1.ile==0:
      Fibonacci1.ile+=1
      return self.a
    if Fibonacci1.ile==1:
      Fibonacci1.ile+=1
      return self.b
    if Fibonacci1.ile>=self.stop:
      raise StopIteration
    self.a,self.b=self.b,self.a+self.b
    Fibonacci1.ile+=1
    return self.b
a=Fibonacci1(stop=10)
print("Ciąg Fibonaciego")
for i in a:
  for j in a:
   print(f'({i} {j})',end=" ")
  print()
print()

class Fibonacci2():
  def __init__(self,a=0,b=1,stop=10):
    self.a=a
    self.b=b
    self.stop=10
    self.ile=0
  def __iter__(self):
    return Fibonacci2(self.a,self.b,self.stop)
#    return FibonacciNext(self.a,self.b,self.stop)
#class FibonacciNext():
#  ile=0
#  def __init__(self,a=0,b=1,stop=10):
#    self.a=a
#    self.b=b
#    self.stop=10
#    FibonacciNext.ile=0
  def __next__(self):
    if self.ile==0:
      self.ile+=1
      return self.a
    if self.ile==1:
      self.ile+=1
      return self.b
    if self.ile>=self.stop:
      raise StopIteration
    self.a,self.b=self.b,self.a+self.b
    self.ile+=1
    return self.b
a=Fibonacci2(stop=10)
print("Ciąg Fibonaciego")
for i in a:
  for j in a:
   print(f'({i} {j})',end=" ")
  print()
print()


print()
print("##########2##########")
print()

class Rand():
  def __init__(self):
    self.x=1
    self.a=7**5
    self.c=0
    self.m=2**31-1
  def __iter__(self):
    return self
  def __next__(self):
    self.x=(self.a*self.x+self.c)%self.m
    return self.x/self.m
r=Rand()
ile1,ile2=0,0
for i in range(1,11):
  ile1=0
  ile2=0
  a=i/10
  for _ in range(10**5):
    if next(r)<a and next(r)<a:
      ile1+=1
    if random.random()<a and random.random()<a:
      ile2+=1
  print(f'Kwadrat o boku 0.1*{i} {ile1/10**3}% {ile2/10**3}%')


print()
print("##########3##########")
print()

def fun(x):
  return math.sin(x)-(0.5*x)**2
class NewtonRaphson():
  def __init__(self,x,eps):
    self.x=x
    self.eps=eps
  def __iter__(self):
    return self
  def __next__(self):
    temp=self.x
    self.x=self.x-fun(self.x)/scipy.misc.derivative(fun,self.x)
    if abs(fun(self.x))<=self.eps:
      raise StopIteration
    return self.x
for i in NewtonRaphson(1.5,10**(-5)):
  print(i)
print(fun(1.9337532188662476))
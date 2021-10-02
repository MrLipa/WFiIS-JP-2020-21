import abc
import types
import random


print("##########1##########")
print()

def fun1(x):
  return x**2

def fun2(x):
  return x**3+4*x

class Calka(abc.ABC):
    def __init__(self, a,b,n, fun):
      if not (isinstance(a,(float,int)) and isinstance(b,(float,int)) and isinstance(n,(int)) and a<=b and n>0 and isinstance(fun,types.FunctionType)):
        raise TypeError
      self.a=a
      self.b=b
      self.n=n
      self.fun=fun
    @abc.abstractmethod
    def calculate(self):
      pass

class CalkaTrapeze(Calka):
    def __init__(self, a,b,n, fun):
        super().__init__(a,b,n,fun)
    def calculate(self):
      """Metoda obliczająca całke metodą trapezów"""
      h=(self.b-self.a)/self.n
      s=sum(map(lambda x: self.fun(self.a+x*h)+self.fun(self.a+(x+1)*h),range(1,self.n)))
      return h/2*s

class CalkaSimpson(Calka):
    def __init__(self, a,b,n, fun):
        super().__init__(a,b,n,fun)
    def calculate(self):
      """Metoda obliczająca całke metodą Simpsona"""
      h=(self.b-self.a)/(2*self.n)
      s=sum(map(lambda x: 4*self.fun(self.a+x*h) if x%2 else 2*self.fun(self.a+x*h),range(1,2*self.n)))+self.fun(self.a)+self.fun(self.b)
      return h/3*s

print("Całka metodą trapezów dla funkcji x**2 w [1,2] z n=100 wynosi: ",round(CalkaTrapeze(1,2,100,fun1).calculate(),3))
print("Całka metodą Simpsona dla funkcji x**2 w [1,2] z n=100 wynosi: ",round(CalkaSimpson(1,2,100,fun1).calculate(),3))


print()
print("##########2##########")
print()

class Stack:
  def __init__(self,a=None):
    if isinstance(a,Stack):
      self.value=[i for i in a.value]
    else:
      self.value=[]
  def push(self,a):
    self.value.append(a)
  def pop(self):
    self.value.pop()
  def expend(self,a):
    if isinstance(a,Stack):
      for i in a.value:
        self.push(i)
  def __len__(self):
    return len(self.value)
  def __str__(self):
    return str(self.value)

class StackSort(Stack):
  def __init__(self,a=None):
    super().__init__(a)
  def push(self,a):
    if len(self.value)==0 or a>=self.value[-1]:
      self.value.append(a)
  def expend(self,a):
    if isinstance(a,Stack) and self.value[-1]<=a.value[0]:
      for i in a.value:
        self.push(i)

a=Stack()
a.push(1)
a.push(2)
a.push(3)
print(a)

b=Stack(a)
b.push(1)
b.push(2)
b.push(3)
b.pop()
print(b)
print("Rozmiar: ",len(b))

c=StackSort()
c.push(1)
c.push(2)
c.push(3)
c.push(1)
c.push(2)
print(c)

s=0
for _ in range(100):
  d=StackSort()
  for _ in range(100):
    d.push(random.randint(0,100))
  s+=len(d)
print("Sredni rozmiar posortowanego stosu przy losowaniu zmiennych w zakresie [0,100] to:",s/100)


print()
print("##########3##########")
print()

class Counter:
  files=[]
  lines=[]
  words=[]
  characters=[]
  def __init__(self,*files):
    self.files=[i for i in files]
  def cout(self):
    for i in self.files:
      with open(i,'r') as pl:
        l=0
        w=0
        c=0
        for line in pl:
          l+=1
          w+=len(line.split(' '))
          c+=len(line)
        Counter.lines.append(l)
        Counter.words.append(w)
        Counter.characters.append(c)
        Counter.files.append(i)
  @staticmethod
  def message():
    for i in range(len(Counter.files)):
      print(f'{Counter.lines[i]}  {Counter.words[i]}  {Counter.characters[i]}  {Counter.files[i]}')
    print(f'{sum(Counter.lines)}  {sum(Counter.words)}  {sum(Counter.characters)}  razem')

e=Counter('plik1.txt','plik2.txt')
e.cout()
e.message()

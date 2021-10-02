import random
class A:
  def __init__(self,a,b,fun= lambda x:x):
    self.a,self.b,self.fun=a-1,b,fun
  def __iter__(self):
    return self
  def __next__(self):
    if self.a>=self.b:
      raise StopIteration
    self.a+=1
    return self.fun(self.a)
for a in A(2,6,lambda x:x+5):
  print(a,end=" ")
print()

for a in A(2,6,lambda x:x+5):
  print(a,end=" ")
print()

class A:
  def __init__(self,*els):
    self.els=els
    self.s=0
  def __iter__(self):
    return self
  def __next__(self):
    if self.s==len(self.els):
      raise StopIteration
    self.s+=1
    return sum(self.els[:self.s])
wart=[random.randrange(10) for _ in range(10)]
print(wart)

for a in A(*wart):
  print(a,end=" ")
print()

for a in A(*wart):
  print(a,end=" ")
print()
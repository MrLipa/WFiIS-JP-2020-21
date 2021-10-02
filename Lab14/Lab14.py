import math


print("##########1##########")
print()

class Point:
  def __init__(self):
    self.x=0
    self.y=0

  @property
  def x(self):
    return self._x

  @property
  def y(self):
    return self._y

  @x.setter
  def x(self,a):
    self._x=a

  @y.setter
  def y(self,a):
    self._y=a

  @x.getter
  def x(self):
    return self._x

  @y.getter
  def y(self):
    return self._y

  def __str__(self):
    return f'({self._x},{self._y})'

a=Point()
print("Point A: ",a)
a.x=4
a.y=4
print("Point A: ",a)
b=Point()
print("Point B: ",b)
b.x=5
b.y=5
print("Point B: ",b)


print()
print("##########2##########")
print()

# Proszę zdefiniować funkcje dodawania i odejmowania współrzędnych (z wykorzystaniem wcześniej zdefiniowanej klasy) oraz opatrzyć je dekoratorem (implementowanym jako funkcja) sprawdzającym czy współrzędne leżą w określonym zakresie, jeżeli nie - proszę zgłosić wyjątek (3p)
def dec1(range1,range2):
  def dec2(fun):
    def dec3(p1,p2):
      if range1<=p1.x<=range2 and range1<=p1.y<=range2 and range1<=p2.x<=range2 and range1<=p2.y<=range2:
        return fun(p1,p2)
      else:
        raise ValueError("Punkty poza range")
    return dec3
  return dec2
@dec1(-100,100)
def add(p1,p2):
  p=Point()
  p.x=p1.x+p2.x
  p.y=p1.y+p2.y
  return p

@dec1(-100,100)
def sub(p1,p2):
  p=Point()
  p.x=p1.x-p2.x
  p.y=p1.y-p2.y
  return p

c=Point()
d=Point()
c.x=10
c.y=10
d.x=50
d.y=50
print("Point C: ",c)
print("Point D: ",d)
print("Point C + D: ",add(c,d))
print("Point C - D: ",sub(c,d))


print()
print("##########3##########")
print()

class Count:
  @staticmethod
  def Triangle(a,b,c):
    area,circumference=0,0
    ab=math.sqrt((b.x-a.x)**2+(b.y-a.y)**2)
    bc=math.sqrt((c.x-b.x)**2+(c.y-b.y)**2)
    ca=math.sqrt((a.x-c.x)**2+(a.y-c.y)**2)
    circumference=ab+bc+ca
    p=circumference/2
    area=math.sqrt(p*(p-ab)*(p-bc)*(p-ca))
    return area,circumference
  @staticmethod
  def Quadrangle(a,b,c,d):
    area,circumference=0,0
    ab=math.sqrt((b.x-a.x)**2+(b.y-a.y)**2)
    bc=math.sqrt((c.x-b.x)**2+(c.y-b.y)**2)
    cd=math.sqrt((d.x-c.x)**2+(d.y-c.y)**2)
    da=math.sqrt((a.x-d.x)**2+(a.y-d.y)**2)
    circumference=ab+bc+cd+da
    p=circumference/2
    area=math.sqrt((p-ab)*(p-bc)*(p-cd)*(p-da))
    return area,circumference
a.x=-1
a.y=0
b.x=1
b.y=0
c.x=0
c.y=2
d.x=2
d.y=2
print(a,b,c,"Circumference: ",round(Count.Triangle(a,b,c)[1],3),"   Area: ",round(Count.Triangle(a,b,c)[0],3))
print(a,b,c,d,"Circumference: ",round(Count.Quadrangle(a,b,c,d)[1],3),"   Area: ",round(Count.Quadrangle(a,b,c,d)[0],3))


print()
print("##########4##########")
print()

class Call:
  dic={}
  def __init__(self,fun):
    self._fun=fun
    Call.dic.setdefault(self._fun.__name__,0)
  def __call__(self,*a):
    Call.dic[self._fun.__name__]+=1
    return self._fun(*a)
  @staticmethod
  def count():
    return Call.dic

@Call
def fun1():
  pass
@Call
def fun2():
  pass
@Call
def fun3():
  pass

fun1()
fun2()
fun3()
fun1()
fun2()

print(Call.count())

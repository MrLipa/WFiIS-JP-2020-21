import math


print("##########1##########")
print()

a=int(input("Podaj parametr a:"))
b=int(input("Podaj parametr b:"))
c=int(input("Podaj parametr c:"))

print()
print(str(a)+"*x^2 + "+str(b)+"*x + "+str(c))
delta=b**2-4*a*c

print()
if delta<0:
  print("Nie ma rozwiązań rzeczywistych")
elif abs(delta)<(1e-7):
  print("Jedno rozwiązanie")
  print("x_0=",-b/(2*a))
else:
  print("Dwa rozwiązania")
  x1=(-b-math.sqrt(delta))/(2*a)
  x2=(-b+math.sqrt(delta))/(2*a)
  print("x_1=",x1)
  print("x_2=",x2)

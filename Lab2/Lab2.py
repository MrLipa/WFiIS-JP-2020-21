import math


print("##########1##########")
print()

a=[1,2,3,4,5,1,2,3,4]
print(a)
for i in range(a.count(2)):
  a.remove(2)
print(a)


print()
print("##########2##########")
print()

a=[1,2,3,4,5,1,2,3,4]
print(a)
while 3 in a:
  a.remove(3)
print(a)


print()
print("##########3##########")
print()

a=[1,2,3,4,5,1,2,3,4]
print(a)
print("[",end="")
for i in range( 1,len(a),2 ):
  print(a[i],end=", ")
print("\b\b]")


print()
print("##########4##########")
print()

print(a)
print(a[1::2])


print()
print("##########5##########")
print()

print(a)
print("[",end="")
for i in range(len(a)-1,1,-2):
  print(a[i],end=", ")
print("\b\b]")


print()
print("##########6##########")
print()

print(a)
print(a[::-2])


print()
print("##########7##########")
print()

k=[(i,a[i]) for i in range(len(a))]
print(k)


print()
print("##########8##########")
print()

k.sort(key=lambda x: x[1])
print(k)


print()
print("##########9##########")
print()

k=[(i,a[i]) for i in range(len(a)) if not a[i]%2 ]
print(k)


print()
print("##########10##########")
print()

k=[(i,a[i]) for i in range(len(a)) if i>a[i] ]
print(k)
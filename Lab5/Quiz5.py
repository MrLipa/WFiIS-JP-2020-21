print("##########1##########")
print()

s1={1: 'a', 2: 'b', 3: 'c'}
s2={1: 'x', 2: 'y', 3: 'x'}
s2.update(s1)
print(s1,s2)


print()
print("##########2##########")
print()

s={}
s.setdefault(3,None)
s.setdefault(3,13)
print(s)


print()
print("##########3##########")
print()

v=[1,2,3,4,5]
# s={v[i:]: i for i in range(len(v))}
# print(s)


print()
print("##########4##########")
print()

s={2: 3, 0:2 , 1:2}
s={(w,k) for k,w in s.items()}
print(s)


print()
print("##########5##########")
print()

s={2: 3, 0:2 , 1:2}
s={w:k for k,w in s.items()}
print(s)


print()
print("##########6##########")
print()

import random
lista=[random.randrange(1,20,2) for i in range(2)]


print()
print("##########7##########")
print()

a,b=5,8
lista=[random.randrange(a if a<b else b) for i in range(a if a>b else b)]


print()
print("##########8##########")
print()

lista=[random.randint(2,10) for _ in range(10)]


print()
print("##########9##########")
print()

s={2: 3, 0:2 , 1:2}
li=[k/w for k,w in s.items() if w]
print(li)


print()
print("##########10##########")
print()

lista=[1,2,3,4,5,5]
slownik={i:lista.count(i) for i in lista}
print(slownik)
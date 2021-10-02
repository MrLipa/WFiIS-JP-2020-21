print("##########1##########")
print()

s='qwertyrtyrty'
print(s.split('r',2))


print()
print("##########2##########")
print()

a=[2,3,4,5]
s=0
for i in a:
   s+=i
print(s)


print()
print("##########3##########")
print()

import sys
a=True if len(sys.argv)-1 else False
print(a)


print()
print("##########4##########")
print()

a=[[]]*5
a[2].append(1)
print(a)


print()
print("##########5##########")
print()

a,b=2,3/4
print(f'{a=} {b=:.3f}')        #a=2 b=0.750


print()
print("##########6##########")
print()

import sys
if a:=len(sys.argv)>5:
   print(type(a))


print()
print("##########7##########")
print()

import sys
a,b=sys.argv[1:3] if len(sys.argv)>=3 else (None, None)


print()
print("##########8##########")
print()

k=[4,2,6,7,5,3]
k.sort()
print(k)        #[2, 3, 4, 5, 6, 7]


print()
print("##########9##########")
print()

s='qwerty'
a=[i for i in s if i in 'aeiouy']
print(a)


print()
print("##########10##########")
print()

k=[2,3,4,5,6,7]
a=[k[-i-1] for i in range(len(k))]
print(a)

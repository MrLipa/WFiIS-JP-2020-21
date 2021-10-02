print("##########1##########")
print()

k=[1,2,3,4,5,6]
print(k[:-3])


print()
print("##########2##########")
print()

k=[2,4,6,8]
for i in k:
    if i%2:
        print('break')
        break
else:
    print('else')


print()
print("##########3##########")
print()

k=[1,2,3]
k.extend([1,2,3])
print(k)


print()
print("##########4##########")
print()

import math
print(math.fabs(-2))


print()
print("##########5##########")
print()

print(1.//2)


print()
print("##########6##########")
print()

k=[1,2,3,4,5,6]
# a,b=k
# print(a,b)


print()
print("##########7##########")
print()

k=[[] for i in range(3)]
k[1].append(1)
print(k)


print()
print("##########8##########")
print()

print(list(range(10,5)))


print()
print("##########9##########")
print()

kr=(1)
print(type(kr))


print()
print("##########10##########")
print()

k=[1,2,3,4,5,6]
for i in k:
    i='q'
print(k)
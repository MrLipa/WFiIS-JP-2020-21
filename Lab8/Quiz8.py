print("##########1##########")
print()
import random
def fun (a,r={}):
    for i,j in a:
        r[j]=i
    return r
t=[(i,j) for i,j in enumerate(random.choices(range(3),k=5))]
print(t)                            #f(0, 1), (1, 1), (2, 2), (3, 0), (4, 0]
print(fun(*t))
for i in range (5):
    for j in range (3):
        if i==j:
            break
    else:
        print(i)
t=[(x:=random.randrange (10), x%2) for _ in range(2)]
print(t)                               #[(2, 0), (5, 1)]
print(fun (t))


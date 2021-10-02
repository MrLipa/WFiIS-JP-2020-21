print("##########1##########")
def fun(N):
    yield from range(N)
f=fun(5)
print(list(f))
print(list(f))


print()
print("##########2##########")
import glob
for name in glob.glob('.py'):
    print(name)


print()
print("##########3##########")
with open('plik') as pl:
    s = sum(map(float, pl.readlines()))
    print(s)


print()
print("##########4##########")
with open('plik') as pl:
    pass


print()
print("##########5##########")
import random

# def fun(*par):
#     for i in range(len(par)):
#         par[i]+=random.random()
#     yield from par

# for el in fun(1,2,3,4):
#     print(el)


print()
print("##########6##########")
import random
with open('nazwa','w') as pl:
    for _ in range(10):
        pl.write(f'{random.randrange(10)} {random.random()}\n')


print()
print("##########7##########")
def fun(seq, w):
    for i in seq:
        if i>w:
            return i
        yield i
t = [3,5,99,2,101,34,2]
for el in fun(t,100):
    print(el)


print()
print("##########8##########")
def fun(n):
    while True:
        yield tuple(random.random() for _ in range(n))
f=fun(4)
print(next(f))
print(next(f))
print(next(f))


print()
print("##########9##########")
res  = list(map(lambda x,y : min(x,y), random.choices(range(100), k=5),
                    random.choices(range(100), k=5)))


print()
print("##########10##########")
res  = list(map(lambda x,y : min(x,y), random.choices(range(100), k=5),
                    random.choices(range(100), k=5)))
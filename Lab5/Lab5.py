import random
import string

print("##########1##########")
print()

def fun1(napis):
    lista = [0] * 10
    slownik={}
    for i in range(len(string.ascii_lowercase)):
        if string.ascii_lowercase[i] in napis and string.ascii_lowercase[i] != 'x':
            slownik[string.ascii_lowercase[i]]=str(random.randrange(10))
    tr = napis.maketrans(slownik)
    for i in range(10):
        x = random.uniform(0, 1)
        lista[i] = (x, eval(napis.translate(tr)))
    return lista
print(fun1('a*x**2+b*x+c'))


print()
print("##########2##########")
print()

def fuc2(*args):
    lista = []
    for i in args[0]:
        for j in args[1:]:
            if i not in j:
                break
        else:
            lista.append(i)
    return lista


print(fuc2([1, 2, 3], (1, 3, 5), [3, 2]))
print(fuc2([1, 2, 3], (1, 3, 5), [3, 2, 1]))


print()
print("##########3##########")
print()

def fuc3(lista1, lista2, a=True):
    if a == True:
        size = min(len(lista1), len(lista2))
        lista3 = [(lista1[i], lista2[i]) for i in range(size)]
        return lista3
    else:
        if len(lista1) > len(lista2):
            lista3 = [None] * len(lista1)
            lista3[:len(lista2)] = [(lista1[i], lista2[i]) for i in range(len(lista2))]
            return lista3
        else:
            lista3 = [None] * len(lista2)
            lista3[:len(lista1)] = [(lista1[i], lista2[i]) for i in range(len(lista1))]
            return lista3


print(fuc3([1, 2, 3], [1, 2, 3]))
print(fuc3([1, 2, 3], [1, 2, 3, 4], False))
print(fuc3([1, 2, 3, 4], [1, 2, 3, ], False))


print()
print("##########4##########")
print()

def fun4(a, n=(10, 5, 2)):
    lista2 = []
    while (a > 0):
        v = 0
        current = 0;
        for i in range(len(n)):
            if a >= n[i] and n[i] > current:
                current = n[i]
        lista2.append(current)
        a -= current
    return lista2


print(fun4(10))
print(fun4(32))
print(fun4(9, (5, 4, 1)))


print()
print("##########5##########")
print()

def fun5(number, lim1, lim2, way='r'):
    ile = 0
    x = 0
    if way == 'r':
        while x != number:
            x = random.randint(lim1, lim2)
            ile += 1
    else:
        ile += 1
        while x != number:
            x = (lim1 + lim2) // 2
            if number > x:
                lim1 = x
            else:
                lim2 = x
            ile += 1
    return ile


print(fun5(14, 1, 20, 'r'))
print(fun5(14, 1, 20, 't'))
import random
import string


print("##########1##########")
print()

k = int(input("Podaj ilosc elementów: "))
lista = [random.randint(0, 5 * k - 1) for i in range(k)]
slownik = {}
listakopia = lista[:]
print("Lista: ", lista)
for i in range(100):
    random.shuffle(lista)
    count = 0
    for j in range(k):
        if listakopia[j] == lista[j]:
            count += 1
    slownik[i+1] = count
print("Słownik: ", slownik)


print()
print("##########2##########")
print()

nazwa = '.'.join(random.choice(string.ascii_lowercase) for i in range(k))
print("String: ", nazwa)
print()


print()
print("##########3##########")
print()

lista1 = [random.randrange(20) for i in range(100)]
slownik2 = {}
for i, v in enumerate(lista1):
    slownik2.setdefault(v, []).append(i)
print("Slownik2:", slownik2)

slownik2 = {}
for i in lista1:
  slownik2.setdefault(i, []).append(lista1.index(i,slownik2[i][-1]+1) if slownik2[i] else lista1.index(i))

print("Slownik2:", slownik2)


print()
print("##########4##########")
print()

slownik3 = {}
for n in range(3, 7):
    polindrome = 0
    for i in range(1000):
        num = random.randint(pow(10, n - 1), pow(10, n) - 1)
        temp = num
        reversal = 0
        digital = 0
        while temp > 0:
            digital = temp % 10
            reversal = reversal * 10 + digital
            temp = temp // 10
        if (reversal == num):
            polindrome += 1
    slownik3[n] = polindrome
print("Slownik polindromów", slownik3)


print()
print("##########5##########")
print()

slownik4 = {i: random.randrange(100) for i in range(10)}
slownik5 = {i: random.randrange(100) for i in range(10)}
slownik6 = {}
print("Slownik4: ", slownik4)
print("Slownik5: ", slownik5)
slownik4 = {slownik4[i]: i for i in slownik4}
slownik5 = {slownik5[i]: i for i in slownik5}
print("Slownik4 po zamianie: ", slownik4)
print("Slownik5 po zamianie: ", slownik5)

slownik6 = {i: (slownik4[i], slownik5[i]) for i in slownik4 if i in slownik5}
print("Slownik6:", slownik6)

import datetime


print("##########1##########")
print()

class Pesel(Exception):
    print(Exception)
    pass

def fun1(p, data, pl):
    wagi = [1, 3, 7, 9, 1, 3, 7, 9, 1, 3]
    pesel = []
    k = 0
    plec = ''
    year = 1900
    mouth = 0
    day = 0
    try:
        for i in p:
            pesel.append(int(i))
    except ValueError as ex1:
        print("Zły pesel")
    else:
        for i in range(10):
            k += pesel[i] * wagi[i]
        k = k % 10
        k = 10 - k
        k = k % 10

        if pesel[9] % 2:
            plec = 'mężczyzna'
        else:
            plec = 'kobieta'

        mouth = pesel[2] * 10 + pesel[3]
        if 80 < mouth <= 82:
            year -= 100
            mouth -= 80
        elif 20 < mouth <= 32:
            year += 100
            mouth -= 20
        elif 40 < mouth <= 52:
            year += 200
            mouth -= 40
        elif 60 < mouth <= 72:
            year += 300
            mouth -= 60
        year = year + pesel[0] * 10 + pesel[1]
        day = pesel[4] * 10 + pesel[5]
        try:
            if year != data.year or mouth != data.month or day != data.day:
                raise Pesel("Zły pesel (data)")
            elif plec != pl:
                raise Pesel("Zły pesel (plec)")
            elif k != pesel[10]:
                raise Pesel("Zły pesel (suma kontrolna)")
            else:
                print()
                print("Podany pesel jest poprawny")
                print("Pesel ", p)
                print("Płeć ", plec)
                print("Data ", day, mouth, year)
        except Pesel as ex1:
            print("Zły pesel")

data = datetime.date(1902, 7, 8)
pesel = '02070803628'
plec = 'kobieta'
fun1(pesel, data, plec)

data = datetime.date(2002, 7, 8)
pesel = '02270803624'
plec = 'kobieta'
fun1(pesel, data, plec)

data = datetime.date(2002, 7, 8)
pesel = '02270812350'
plec = 'mężczyzna'
fun1(pesel, data, plec)


print()
print("##########2##########")
print()

def przestepny(a):
    return a[2] % 4 == 0 and a[2] % 100 != 0 or a[2] % 400 == 0


def check(a):
    days = [31, 28, 31, 30, 30, 31, 31, 30, 31, 30, 31]
    if przestepny(a):
        days[1] += 1
    if a[2] <= 2021:
        if a[1] <= 12 and a[1] > 0:
            if a[0] > 0 and a[0] <= days[a[1]]:
                if a[2] >= 2021 and a[1] > 5 and a[0] >= 5:
                    return False
                else:
                    pass
            else:
                return False
        else:
            return False
    else:
        return False
    return True


def age(a):
    today = datetime.date.today()
    return today.year - a[2]


def fun2(name, tryb):
    l = []
    l1 = []
    with open(name) as pl:
        for line in pl:
            try:
                if check((int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2]))):
                    l.append((int(line.split(" ")[0]), int(line.split(" ")[1]), int(line.split(" ")[2])))
                    l1.append(age(l[len(l) - 1]))
                else:
                    raise IndexError
            except IndexError:
                if tryb == 'r':
                    return
    s = 0
    for i in l1:
        s += i
    return s / len(l1)

print("Srednia wieku ludzi z pliku daty.in to:", round(fun2("daty.in", 'l'), 3), "lat")


print()
print("##########3##########")
print()

def fun3(a):
    try:
        if len(a) <= 3:
            raise ValueError
    except ValueError:
        print("Niepoprawne dane")
    else:
        t = []
        f = []
        t1 = []
        f1 = []
        for i in range(0, len(a), 3):
            try:
                if a[i] ** 2 + a[i + 1] ** 2 == a[i + 2] ** 2:
                    t.append((a[i], a[i + 1], a[i + 2]))
            except IndexError:
                print("Nieprawidłowa tablica")
                break
        for i in range(0, len(a), 4):
            try:
                if a[i] ** 2 + a[i + 1] ** 2 + a[i + 2] ** 2 == a[i + 3] ** 2:
                    f.append((a[i], a[i + 1], a[i + 2], a[i + 3]))
            except IndexError:
                print("Nieprawidłowa tablica")
                break
        for i in t:
            np = len(list(filter(lambda x: x % 2, i)))
            t1.append((np, 3 - np))
        for i in f:
            np = len(list(filter(lambda x: x % 2, i)))
            f1.append((np, 4 - np))
        print("Trójki Pitagorejskie: ", t)
        print("Czwórki Pitagorejskie: ", f)
        print("Lista krotek dla trójek (Nieparzyste, Parzyste)", t1)
        print("Lista krotek dla czwórek (Nieparzyste, Parzyste)", f1)


l1 = (
    1, 2, 2, 3, 2, 3, 6, 7, 1, 4, 8, 9, 4, 4, 7, 9, 2, 6, 9, 13, 6, 6, 7, 11, 3, 4, 12, 13, 2, 5, 14, 15, 2, 10, 11, 15,
    1,
    12, 12, 17, 8, 9, 12, 17, 1, 6, 18, 19, 6, 6, 17, 19, 6, 10, 15, 21, 4, 5, 20, 21, 4, 8, 19, 21, 4, 13, 16, 21, 8,
    11,
    16, 21, 3, 6, 22, 23, 3, 13, 18, 23, 6, 13, 18, 23, 9, 14, 20, 25, 12, 15, 16, 25, 2, 7, 26, 27, 2, 10, 25, 27, 2,
    14,
    23, 27, 7, 14, 22, 27, 10, 10, 23, 27, 3, 16, 24, 29, 11, 12, 24, 29, 12, 16, 21, 29, 2)
l2 = (
    1, 2, 2, 3, 2, 3, 6, 7, 1, 4, 8, 9, 4, 4, 7, 9, 2, 6, 9, 13, 6, 6, 7, 11, 3, 4, 12, 13, 2, 5, 14, 15, 2, 10, 11, 15,
    1,
    12, 12, 17, 8, 9, 12, 17, 1, 6, 18, 19, 6, 6, 17, 19, 6, 10, 15, 21, 4, 5, 20, 21, 4, 8, 19, 21, 4, 13, 16, 21, 8,
    11,
    16, 21, 3, 6, 22, 23, 3, 13, 18, 23, 6, 13, 18, 23, 9, 14, 20, 25, 12, 15, 16, 25, 2, 7, 26, 27, 2, 10, 25, 27, 2,
    14,
    23, 27, 7, 14, 22, 27, 10, 10, 23, 27, 3, 16, 24, 29, 11, 12, 24, 29, 12, 16, 21, 29)
l3 = (3, 4, 5, 5, 12, 13, 7, 24, 25, 9, 40, 41, 6, 8, 10, 60, 80, 100, 18, 24, 30, 15, 8, 17)
l4 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
fun3(l1)
fun3(l2)
fun3(l3)
fun3(l4)

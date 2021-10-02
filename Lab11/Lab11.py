import random
import math
import matplotlib.pyplot as plt


print("##########1##########")
print()

class Iterated_Function_System:
    def __init__(self, param, p=()):
        self.x = []
        self.y = []
        self.tab = []
        self.x.append(0)
        self.y.append(0)
        if len(param) != len(p):
            self.p = [1] * len(param)
        else:
            self.p = list(p)
        for i in param:
            self.tab.append(i)

    def fun(self, n):
        for _ in range(n):
            param = random.choices(self.tab, weights=self.p, k=1)
            param = param[0]
            self.x.append(param[0] * self.x[-1] + param[1] * self.y[-1] + param[2])
            self.y.append(param[3] * self.x[-2] + param[4] * self.y[-1] + param[5])

    def draw(self):
        plt.scatter(self.x, self.y, marker='.', s=1.5)
        plt.show()


a = Iterated_Function_System(((0.787879, -0.424242, 1.758647, 0.242424, 0.859848, 1.408065),
                              (-0.121212, 0.257576, -6.721654, 0.151515, 0.05303, 1.377236),
                              (0.181818, -0.136364, 6.086107, 0.090909, 0.181818, 1.568035)), (0.90, 0.05, 0.05))
b = Iterated_Function_System(((0, 0.053, -7.083, -0.429, 0, 5.43), (0.143, 0, -5.619, 0, -0.053, 8.513),
                              (0.143, 0, -5.619, 0, 0.083, 2.057), (0, 0.053, -3.952, 0.429, 0, 5.43),
                              (0.119, 0, -2.555, 0, 0.053, 4.536),
                              (-0.0123806, -0.0649723, -1.226, 0.423819, 0.00189797, 5.235),
                              (0.0852291, 0.0506328, -0.421, 0.420449, 0.0156626, 4.569),
                              (0.104432, 0.00529117, 0.976, 0.0570516, 0.0527352, 8.113),
                              (-0.00814186, -0.0417935, 1.934, 0.423922, 0.00415972, 5.37),
                              (0.093, 0, 0.861, 0, 0.053, 4.536), (0, 0.053, 2.447, -0.429, 0, 5.43),
                              (0.119, 0, 3.363, 0, -0.053, 8.513), (0.119, 0, 3.363, 0, 0.053, 1.487),
                              (0, 0.053, 3.972, 0.429, 0, 4.569),
                              (0.123998, -0.00183957, 6.275, 0.000691208, 0.0629731, 7.716),
                              (0, 0.053, 5.215, 0.167, 0, 6.483), (0.071, 0, 6.279, 0, 0.053, 5.298),
                              (0, -0.053, 6.805, -0.238, 0, 3.714), (-0.121, 0, 5.941, 0, 0.053, 1.487)))
c = Iterated_Function_System(((0.824074, 0.281428, -1.88229, -0.212346, 0.864198, -0.110607),
                              (0.088272, 0.520988, 0.78536, -0.463889, -0.377778, 8.095795)), (0.8, 0.2))
a.fun(10000)
a.draw()
b.fun(10000)
b.draw()
c.fun(10000)
c.draw()


print()
print("##########2##########")
print()

class Vector:
    def __init__(self, *a):
        self.val = []
        for i in a:
            self.val.append(i)

    def __len__(self):
        return len(self.val)

    def __str__(self):
        s = "("
        for i in range(len(self.val)):
            s = s + str(self.val[i])
            if i != len(self.val) - 1:
                s = s + ","
        s = s + ")"
        return s

    def __add__(self, vec):
        if type(vec) == Vector:
            if len(self) == len(vec):
                temp = Vector()
                for i in range(len(self.val)):
                    temp.val.append(self.val[i] + vec.val[i])
                return temp

    def __sub__(self, vec):
        if type(vec) == Vector:
            if len(self) == len(vec):
                temp = Vector()
                for i in range(len(self.val)):
                    temp.val.append(self.val[i] - vec.val[i])
                return temp

    def __mul__(self, num):
        temp = Vector()
        for i in range(len(self.val)):
            temp.val.append(self.val[i] * num)
        return temp

    __rmul__ = __mul__

    def dlugosc(self):
        s = 0
        for i in self.val:
            s += i ** 2
        return math.sqrt(s)

    def skalarny(self, vec):
        s = 0
        if type(vec) == Vector:
            if len(self) == len(vec):
                for i in range(len(self.val)):
                    s += self.val[i] * vec.val[i]
        return s

    def wektorowy(self, vec):
        if len(vec) == 3 and len(self) == 3 and type(vec) == Vector:
            x = self.val[1] * vec.val[2] - self.val[2] * vec.val[1]
            y = self.val[2] * vec.val[0] - self.val[0] * vec.val[2]
            z = self.val[0] * vec.val[1] - self.val[1] * vec.val[0]
            return Vector(x, y, z)

    def mieszany(self, vec1, vec2):
        if type(vec1) == Vector and type(vec2) == Vector:
            return self.wektorowy(vec1).skalarny(vec2)


a = Vector(1, 2, 3)
print("Wektor a ", a)
b = Vector(4, 5, 6)
print("Wektor b ", b)
print("Wektor a+b ", a + b)
print("Wektor a-b ", a - b)
print("Wektor a*4 ", a * 4)
print("Wektor 4*a ", 4 * a)
print("Wymiar wektora a ", len(a))
print("Długość wektora a ", a.dlugosc())
print("Iloczyn skalarny a i b ", a.skalarny(b))  # ok
print("Iloczyn wektorowy a i b ", a.wektorowy(b))  # ok
e = Vector(1, -2, -1)
f = Vector(3, 2, 1)
g = Vector(1, -1, 0)
print("Wektor e ", e)
print("Wektor f ", f)
print("Wektor g ", g)
print("Iloczyn mieszany e, f i g ", e.mieszany(f, g))  # ok


print()
print("##########3##########")
print()

def strumien_indukcji_magnetycznej(B, S):
    if type(B) == Vector and type(S) == Vector:
        return B.skalarny(S)


def sila_Lorentza(q, E, v, B):
    if type(E) == Vector and type(v) == Vector and type(E) == Vector:
        return q * (E + v.wektorowy(B))


def praca_sily_Lorentza(q, E, v):
    if type(E) == Vector and type(v) == Vector:
        return q * (E.skalarny(v))


B = Vector(4, 5, 6)
S = Vector(4, 5, 6)
E = Vector(4, 5, 6)
v = Vector(4, 5, 6)
q = 2
print(f"Strumien indukcji magnetycznej dla B={B} oraz S={S} to \u03A6={strumien_indukcji_magnetycznej(B, S)}")
print(f"Sila Lorentza dla q={q} E={E} v={v} i B={B} to F={sila_Lorentza(q, E, v, B)}")
print(f"Praca sily Lorentza dla q={q} E={E} i v={v} to W={praca_sily_Lorentza(q, E, v)}")
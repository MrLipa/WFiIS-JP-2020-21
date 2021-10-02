import abc


class F(abc.ABC):
    k = 0

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @abc.abstractmethod
    def pole(self):
        pass
    @staticmethod
    def ile():
        return F.k

    def __str__(self):
        return f'{self.a}x{self.b}'


class K(F):
    def __init__(self, a):
        super().__init__(a)
        F.k += 1

    def pole(self):
        return self.a * self.a

    def str(self):
        return f'{self.a}x{self.a}'


for el in (K(1), K(2), K(3)):
    print(f'{el}: {el.pole()}')  # 9

print(f'Liczba utowrzonych kwadratów: {F.ile()}')

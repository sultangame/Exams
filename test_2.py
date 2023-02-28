class Kvadrat:
    def __init__(self,a):
        self.a = a
    def S(self):
        return self.a * 4
    def P(self):
        return self.a + self.a * 2

class Terugolnik(Kvadrat):
    def __init__(self, c, d, b):
        super().__init__(a)
        self.c = c
        self.d = d
        self.b = b
    @staticmethod
    def p(c,b, d):
        return b + c + d
    @staticmethod
    def s(c,b,d):
        return c * b * d
a = int(input("a:"))
b = int(input("b:"))
c = int(input("c:"))
d = int(input("d:"))
object = Kvadrat(a)
obj = Terugolnik(c,d,b)
print(object.S())
print(object.P())
print(obj.p(c, b, d))
print(obj.s(c,b,d))
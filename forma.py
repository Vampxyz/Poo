import math

class Forma:
    def __init__(self, nome):
        self.nome = nome


class Circulo(Forma):
    def __init__(self, nome, raio):
        self.raio = raio
        super().__init__(nome)

    def aC(self):
        return math.pi * self.raio ** 2
    
    def pC(self):
        return 2 * math.pi * self.raio


class Retangulo(Forma):
    def __init__(self, nome, base, altura):
        self.base = base
        self.altura = altura
        super().__init__(nome)

    def aR(self):
        return self.base * self.altura

    def pR(self):
        return 2 * (self.base + self.altura)


class Triangulo(Forma):
    def __init__(self, nome, base, altura):
        self.base = base
        self.altura = altura
        super().__init__(nome)

    def aT(self):
        return (self.base * self.altura) / 2 

    def pT(self):
        return "Preguiça de fazer o resto, não vai ter perimetro do triângulo"

circulo = Circulo("Circulo", input("Digite o raio do circulo: "))
print(f"A área do circulo é {circulo.aC()}")
print(f"O perimetro do circulo é {circulo.pC()}")

retangulo = Retangulo("Retângulo", input("Digite a base do retângulo: "), input("Digite a altura do retângulo: "))
print(f"A área do retângulo é {retangulo.aR()}")
print(f"O perimetro do retângulo é {retangulo.pR()}")

triangulo = Triangulo("Triângulo", input("Digite a base do triângulo: "), input("Digite a altura do triângulo: "))
print(f"A área do triângulo é {triangulo.aT()}")
print(f"O perimetro do triângulo é {triangulo.pT()}")
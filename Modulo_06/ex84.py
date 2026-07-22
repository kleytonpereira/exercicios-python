class Retangulo():
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura


    def perimetro(self):
        return (self.base * 2) + (self.altura * 2)
    
assert Retangulo(5,3).area() == 15, 'Area calculada incorretamente'
assert Retangulo(5,3).perimetro() == 16, 'Perimetro calculado incorretamente'
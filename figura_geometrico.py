from figura_geometrica import FiguraGeometrica

class Triangulo(FiguraGeometrica):

    def _init_(self, lado: float = 0.0):

        super()._init_(ancho=lado, alto=lado)

    def _str_(self):

        return f'triangulo [lado = {self.alto}]'

    def calcular_area(self):

        return (self.alto * self.ancho) / 2

    def calcular_perimetro(self):

        return 3 * self.alto

if _name_ == '_main_':

    c1 = Triangulo(lado=3)

    print(c1)

    print(f'el area del tiangulo es: {c1.calcular_area()}')

    print(f'el perimetro del tiangulo es: {c1.calcular_perimetro()}')
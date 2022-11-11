class Circulo:
    # atributo de classe
    PI = 3.14

    # Podemos criar um static method
    @staticmethod
    def obter_pi():
        return 3.14


if __name__ == '__main__':
    print(Circulo.obter_pi())

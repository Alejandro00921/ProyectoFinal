class Menu:
    def __init__(self, laboratorio):
        self.laboratorio = laboratorio

    def ver(self):
        print("Bienvenido al sistema".center(20, "*"))
        print("laboratorio:" + self.laboratorio)
        print("1.tecnicos")
        print("2.estudiantes")
        op = input(">>>")
        return op
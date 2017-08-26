class dojo:

    def __init__(self, x, y, s):
        self.menor = x
        self.mayor = y
        self.salto = s
        self.rango = range(menor, mayor, salto)

    def sum(self):
        sum = 0
        for i in self.rango:
            sum += i #sum = sum + i
        print(sum)
        return sum

print("Ingrese menor")
menor = int(input())

print("Ingrese mayor")
mayor = int(input())

print("Ingrese salto")
salto = int(input())

print(menor, mayor)
calcular = dojo(menor, mayor, salto);
calcular.sum()

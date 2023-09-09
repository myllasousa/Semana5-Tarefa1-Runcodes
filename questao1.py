def calcular(a, b, c) :
    resultado = 2 * a + 5 * b - c
    return resultado
a = int(input(""))
b = int(input(""))
c = int(input(""))

resultado_calculo = calcular(a, b, c)
print(f'{resultado_calculo}')

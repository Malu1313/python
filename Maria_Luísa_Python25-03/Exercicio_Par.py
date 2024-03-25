import time
def verificar_par(numero):
    if numero > 0:
        if numero % 2 == 0:
            print('"P-A-R"')
        else:
            print('tente outra vez!')

num = int(input("Digite um número inteiro positivo: "))
verificar_par(num)

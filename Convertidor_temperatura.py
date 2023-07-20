import os
def CaF(n):
    return (n*(9/5))+32
def FaC(n):
    return (n-32)*(5/9)
def CaK(n):
    return (n+273.15)
def KaC(n):
    return (n-273.15)
def FaK(n):
    return (n-32)*(5/9)+273.15
def KaF(n):
    return (n-273.15)*(9/5)+32
def Menu():
    print('     Menu')
    print('''
1) Grados Centigrados a Grados Fahrenheit.
2) Grados Cahrenheit a Grados Centigrados.
3) Grados Centigrados a Grados Kelvin.
4) Grados Kelvin a Grados Centigrados.
5) Grados Fahrenheit a Grados Kelvin.
6) Grados Felvin a Grados Fahrenheit.
7) Salir\n
    ''')
    op = int(input('Seleccione una opcion: '))
    return op
#Main
continuar = True
while continuar:
    os.system('cls')
    a = Menu()
    if a == 1:
        os.system('cls')
        print('Centigrados a Fahrenheit')
        g = float(input('Ingrese la temperatura en grados Centigrados: '))
        print(CaF(g))
    elif a == 2:
        os.system('cls')
        print('Farenheit a Centigrados')
        g = float(input('Ingrese la temperatura en grados Farenheit: '))
        print(FaC(g))
    elif a == 3:
        os.system('cls')
        print('Centigrados a Kelvin')
        g = float(input('Ingrese la temperatura en grados Kelvin: '))
        print(CaK(g))
    elif a == 4:
        os.system('cls')
        print('Kelvin a Cenigrados')
        g = float(input('Ingrese la temperatura en grados Centigrados: '))
        print(KaC(g))
    elif a == 5:
        os.system('cls')
        print('Farenheit a Kelvin')
        g = float(input('Ingrese la temperatura en grados Farenheit: '))
        print(FaK(g))
    elif a == 6:
        os.system('cls')
        print('Kelvin a Farenheit')
        g = float(input('Ingrese la temperatura en grados Kelvin: '))
        print(KaF(g))
    elif a == 7:
        os.system('cls')
        continuar = False
    else:
            print('Opción Inválida...')

    input('Presione ENTER para continuar...')
input('Nos Vemos...')

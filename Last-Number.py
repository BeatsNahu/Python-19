numeros = []
def separar(x):
    while x > 0:
        numeros.append(x % 10)
        x = x // 10
    print('The last digit of the number is;', numeros[0])    
Last = int(input('Enter a random integer number:'))
separar(Last)
def duplicate(x):
    print(f'Starting to duplicate the number {x}')
    return 2 * x


def sumar(x, y):
    return x + y


def restar(x, y):
    return x - y

print(sumar(23.3, 34.0))


def imprimir_elementos(lista: list) -> None:
    for index, elem in enumerate(lista):
        print(f'El elemen {elem} tiene indice {index}')


# linter: black, mypy, 
imprimir_elementos(12321)

# TODO: Buscar linters de python para verificacion temprana de errores semanticos

# number_a = int(input('Write the first number: '))
# number_b = int(input('Write the second number: '))
# operation = input('Write the operation: ')

# if operation == '+':
#     print(f'Your sum is {sumar(number_a, number_b)}')
# elif operation == '-':
#     print(f'Your sum is {restar(number_a, number_b)}')
# else:
#     print('Invalid operation')

# try:
#     numerator = int(input('Write the numerator: '))
#     denominator = int(input('Write the denominator: '))

#     print(f'Your division result: {numerator / denominator}')
# except ValueError as exception_info:
#     print(exception_info)
#     print(exception_info.args)
#     print('Estas intentando ingresar un valor no numerico')
# except ZeroDivisionError:
#     print('Estas intentando dividir por zero')
# except KeyboardInterrupt:
#     print('El usuario presiono CTRL + C')


# def get_user_data(user_id):
#     pass

# user_id = input('Write your id: ')
# try:
#     user_data = get_user_data(user_id)
# except DatabaseError:
#     print('Something went wrong')


# user_id = input('Write your id: ')
# if is_valid_id(user_id):
#     user_data = get_user_data(user_id)


def suma_2_numeros(number_1, number_2):
    return number_1 + number_2


def suma_3_numeros(number_1, number_2, number_3):
    return number_1 + number_2 + number_3


def suma(*numeros):
    return sum(numeros)


def cuantos_hijos_tienes(father_name, *childs_names):
    print(f'{father_name} has {len(childs_names)}')
    print('Their names are: ')
    for child in childs_names:
        print(child)


def con_valores_por_defecto(father_name, *childs_names, parametro=2):
    print(parametro)


def main():
    # result = suma_2_numeros(2, 3)

    # print(f'{result}')

    # print(suma(1, 2, 3))

    # cuantos_hijos_tienes('Carlos', 'Luis', 'Pamela')

    # cuantos_hijos_tienes('Maria', 'Federio')

    # cuantos_hijos_tienes('Andrea')

    # cuantos_hijos_tienes()

    con_valores_por_defecto()

main()
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

try:
    numerator = int(input('Write the numerator: '))
    denominator = int(input('Write the denominator: '))

    print(f'Your division result: {numerator / denominator}')
except ValueError as exception_info:
    print('Se ingreso un valor no numerico')
except ZeroDivisionError as exception_info:
    print('No se puede dividir por 0')
except KeyboardInterrupt as exception_info:
    print('\nVuelve pronto!')
except:
    print('El padre paga por el error del hijo')
finally:
    pass

# Modos de apertura: w (write), r(read), a(append), (rb, wb, ab)
# wildcards: . | ..
# file = open('./files/testing_file.txt', mode='w')




# try:
#     numerator = int(input('Write the numerator: '))
#     denominator = int(input('Write the denominator: '))

#     file.write(f'Your division result: {numerator / denominator}')
# except Exception:
#     print('Algo salio mal')
# finally:
#     file.close()


# with open('./files/testing_file.txt', mode='w') as file:
#     numerator = int(input('Write the numerator: '))
#     denominator = int(input('Write the denominator: '))

#     file.write(f'Your division result: {numerator / denominator}')

with open('./files/testing_file.txt', mode='r') as file:
    for line in file.readlines():
        print(line)
    
    # print(file.readlines())

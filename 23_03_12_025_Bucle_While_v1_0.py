# El bucle while - Curso de Python desde cero - Capítulo 27

# Crea un bucle while que se ejecute hasta que x valga 15 con incrementos de 5.
x = 0
print('x = ' + str(x))
while x < 15:
    x = x + 5
    print('x = ' + str(x))

# Crea un bucle while que se ejecute hasta que x valga -100 con decrementos de 20.
x = 0
print('\nx = ' + str(x))
while x > -100:
    x = x - 20
    print('x = ' + str(x))

# Crea un bucle while que se ejecute hasta que x valga 0 con decrementos de 1 y que
# muestre en cada ejecución esta frase con el valor de ejecución correspondiente:
# 'El valor del bucle es 10'...
x = 10
print('\nEl valor del bucle es ' + str(x))
while x > 0:
    x = x - 1
    print('El valor del bucle es ' + str(x))
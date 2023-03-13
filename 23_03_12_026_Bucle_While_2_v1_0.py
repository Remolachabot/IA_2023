# El bucle while con condicional if - Curso de Python desde cero - Capítulo 28

# Crea un bucle while con las siguientes características:
#  - El valor inicial de la variable x será de 0.
#  - El valor de incremento será 1.
#  - La condición de salida del bucle será mayor o igual a 30.
#  - La ejecución se deberá romper cuando x valga 15.
#  - Debes imprimir la siguiente frase cada vez que se ejecute el bucle: 'El valor del bucle es: ' + x.
#  - Debes saltarte las ejecuciones con valor de x en 4, 6 y 10.
#  - En cada salto de ejecución, deberás mostrar los valores saltado con este mensaje: 'Se saltó el valor ' + x ' de x'.
#  - Cuando se rompa la ejecución del bucle deberás mostrar un mensaje indicándolo:
#    'Se rompió la ejecución del bucle cuando x valía ' + x.
x = 0
while x < 30:
    x += 1
    if x == 15:
        print('Se rompió la ejecución del bucle cuando x valía: ' + str(x))
        break
    if x == 4 or x == 6 or x == 10:
        print('Se saltó el valor ' + str(x) + ' de x')
        continue
    print('El valor del bucle es: ' + str(x))

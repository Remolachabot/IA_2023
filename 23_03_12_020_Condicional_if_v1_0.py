# El condicional IF y operadores de comparación - Curso de Python desde cero - Capítulo 21

# Cambia el operador para que la condición sea True.
num1 = 15
num2 = 20

if num1 < num2:                 # Cambio de == a <
    print('Se ejecuta el if.')

# Cambia el operador para que la condición sea True.
num1 = 1450
num2 = 60

if num1 > num2:                 # Cambio de == a >
    print('Se ejecuta el if.')

# Haz que el siguiente condicional se convierta en False sin cambiar el operador.
num1 = 1450
num2 = 60

if not num1 != num2:            # Agregar 'not' al condicional if para negar la condicion
    print('Se ejecuta el if.')

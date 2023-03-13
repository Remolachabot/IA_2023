# El condicional if elif else e input, entrada de datos - Curso de python desde cero - Capítulo 23

# Al siguiente código añádele un par de rangos de edad. Uno de 18 años hasta 45 y otro de más de 100 años hasta 120.
edad = int(input('¿Cuál es tu edad?\n'))

if edad <= 0:
    print('Nadie puede tener esa edad.')
elif 1 <= edad <= 18:
    print('Eres menor de edad.')
elif 45 < edad <= 100:
    print('Eres mayor de edad.')
elif 18 < edad <= 45:
    print('No estas viejo')
elif 100 < edad <= 120:
    print('No se como sigues vivo :O')
else:
    print('Edad no válida.')

# Ordenar elementos con sort() y sorted() - Curso de Python - Capitulo 17

# Ordena la siguiente lista en orden alfabético descendente (de la letra 'z' a la 'a').
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón',
          'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Lista original:')
print(colores)

colores.sort(reverse=True)
print('\nLista ordenada (z-a):')
print(colores)

# Eliminar elementos con del() - Curso de Python - Capitulo 12

# De esta lista, elimina los colores 'azul', 'marrón', 'negro' y 'rosa'.
# Debes utilizar al menos una vez las posiciones negativas para eliminar un color.
# Después, imprime la lista para ver los colores que se han eliminado.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Lista original:')
print(colores)

del colores[1]
del colores[3]
del colores[4]
del colores[-3]
print('\nLista actualizada:')
print(colores)

# Eliminar elementos con pop() - Curso de Python - Capitulo 14

# Elimina de la siguiente lista los elementos 'azul' y 'blanco'.
# Solo puedes eliminarlos utilizando el método pop(). Además, tendrás que guardar esos dos colores en una nueva lista
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
print('Lista original:')
print(colores)

coloresBorrados = [colores.pop(1), colores.pop(-2)]
print('\nLista actualizada:')
print(colores)
print('\nElementos borrados:')
print(coloresBorrados)

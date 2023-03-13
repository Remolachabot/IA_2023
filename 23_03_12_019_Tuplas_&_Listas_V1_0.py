# Cómo convertir tuplas a listas y viceversa - Curso de Python - Capítulo 20

# Convierte la siguiente lista en una tupla y asegúrate que se haya convertido en
# tupla correctamente imprimiendo en la consola el tipo de elemento que es.
colores = ['rojo', 'azul', 'verde', 'amarillo', 'marrón', 'lila', 'negro', 'rosa', 'blanco', 'naranja']
colores_tpl = tuple(colores)
print('Tupla:')
print(colores_tpl)
print(type(colores_tpl))

colores_lst = list(colores_tpl)
print('\nLista:')
print(colores_lst)
print(type(colores_lst))

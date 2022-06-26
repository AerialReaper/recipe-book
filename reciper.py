import os
from pathlib import Path
from os import system


mi_ruta = Path(Path.cwd(), 'recetario/Recetas')

# Mostrar menu inicio
def inicio():
    system('cls')
    print('*' * 50)
    print('*' * 5 + ' Bienvenido al administrador de recetas ' + '*' * 5)
    print('*' * 50)
    print('\n')
    print(f'Las recetas se encuentran en { mi_ruta }')
    print(f'Total de recetas: { contador_recetas(mi_ruta) }')

    eleccion_menu = 'x'
    while not eleccion_menu.isnumeric() or eleccion_menu not in range(1, 7):
        print('Elige una opción:')
        print('''
        [1] - Leer receta
        [2] - Crear receta nueva
        [3] - Crear categoría nueva
        [4] - Eliminar receta
        [5] - Eliminar categoría
        [6] - Salir del programa
        ''')

        eleccion_menu = int(input('Selecciona una opción: '))
        return eleccion_menu

def contador_recetas(ruta: Path):
    contador = 0
    for txt in ruta.glob("**/*.txt"):
        contador += 1
    return contador

def mostrar_categorias(ruta_categorias: Path):
    print('Categorías:')
    lista_categorias = []

    for indx, carpeta in enumerate(ruta_categorias.iterdir()):
        carpeta_nombre = str(carpeta.name)
        print(f'[{ indx + 1 }] - { carpeta_nombre }')
        lista_categorias.append(carpeta)

    return lista_categorias

def elegir_categoria(lista_categorias: list[Path]):
    eleccion = 'x'

    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista_categorias) + 1 ):
        eleccion = input('\nElije una categoría: ')
    
    return lista_categorias[int(eleccion) - 1]

def mostrar_recetas(ruta_recetas: Path):
    print('Recetas:')
    lista_recetas = []

    for indx, receta in enumerate(ruta_recetas.glob('*.txt')):
        receta_nombre = str(receta.name)
        print(f'[{ indx + 1 }] - { receta_nombre }')
        lista_recetas.append(receta)

    return lista_recetas

def elegir_recetas(lista_recetas: list[Path]):
    eleccion = 'x'

    while not eleccion.isnumeric() or int(eleccion) not in range(1, len(lista_recetas) + 1 ):
        eleccion = input('\nElije una receta: ')
    
    return lista_recetas[int(eleccion) - 1]

def leer_receta(ruta_receta: Path):
    print(Path.read_text(ruta_receta))

def crear_receta(ruta_categoria: Path):
    existe = False
    while not existe:
        print("Escribe el nombre de tu receta: ")
        nombre_receta = input() + '.txt'
        print("Escribe tu nueva receta: ")
        contenido_receta = input()
        ruta_nueva = Path(ruta_categoria, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"Tu receta { nombre_receta } ha sido creada")
            existe = True
        else:
           print("Lo siento, esa receta ya existe") 

def crear_categoria(ruta_categorias: Path):
    existe = False
    while not existe:
        print("Escribe el nombre de la nueva categoría: ")
        nombre_categoria = input()
        ruta_nueva = Path(ruta_categorias, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"Tu categoría { nombre_categoria } ha sido creada")
            existe = True
        else:
           print("Lo siento, esa categoría ya existe") 

def eliminar_receta(receta: Path):
    receta.unlink()
    print(f"La receta { receta.name } ha sido eliminada")

def eliminar_categoria(categoria: Path):
    for receta in categoria.glob('*'):
        if receta.is_file():
            receta.unlink()
        else:
            eliminar_categoria(receta)
    categoria.rmdir()
    print(f"La categoría { categoria.name } ha sido eliminada")

def volver_inicio():
    eleccion = 'x'

    while eleccion.lower() != 'v':
        eleccion = input("\nPresione 'V' para volver al inicio: ")

finalizar_programa = False
while not finalizar_programa:
    menu = inicio()

    if menu == 1:
        mis_categorias = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(categoria_elegida)
        mi_receta = elegir_recetas(mis_recetas)
        leer_receta(mi_receta)
        volver_inicio()
    elif menu == 2:
        mis_categorias = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoria(mis_categorias)
        crear_receta(categoria_elegida)
        volver_inicio()
    elif menu == 3:
        crear_categoria(mi_ruta)
        volver_inicio()
    elif menu == 4:
        mis_categorias = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoria(mis_categorias)
        mis_recetas = mostrar_recetas(categoria_elegida)
        mi_receta = elegir_recetas(mis_recetas)
        eliminar_receta(mi_receta)
        volver_inicio()
    elif menu == 5:
        mis_categorias = mostrar_categorias(mi_ruta)
        categoria_elegida = elegir_categoria(mis_categorias)
        eliminar_categoria(categoria_elegida)
        volver_inicio()
    elif menu == 6:
        finalizar_programa = True
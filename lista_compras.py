lista_compras = []

while True:
    print("\nMenú de opciones:")
    print("a. Agregar artículo")
    print("b. Eliminar artículo")
    print("c. Mostrar lista")
    print("d. Salir")
    
    opcion = input("Elige una opción (a-d): ")
    
    if opcion == 'a':
        articulo = input("Ingresa el nombre del artículo: ")
        lista_compras.append(articulo)
        print(f"'{articulo}' ha sido agregado a la lista")
        
    elif opcion == 'b':
        if lista_compras:
            print("Lista de compras actual:")
            for i, articulo in enumerate(lista_compras):
                print(f"{i}. {articulo}")
            
            try:
                indice = int(input("Ingresa el número del artículo a eliminar: "))
                if 0 <= indice < len(lista_compras):
                    eliminado = lista_compras.pop(indice)
                    print(f"'{eliminado}' ha sido eliminado de la lista")
                else:
                    print("Índice inválido")
            except ValueError:
                print("Error, ingresa un número válido")
        else:
            print("No hay nada que eliminar")
    
    elif opcion == 'c':
        if lista_compras:
            print("Lista de compras actual:")
            for i, articulo in enumerate(lista_compras):
                print(f"{i}. {articulo}")
        else:
            print("La lista está vacía")
    
    elif opcion == 'd':
        print("¡Muchas Gracias!")
        break
    
    else:
        print("Opción no válida, por favor elige una opción entre a y d")

from vtable import Vtable


def filter(functions):
    """ Chequea si existe repeticiones en una lista de funciones y elimina los
        posibles strings vacios que se pudieron haber obtenido al leer el input """
    functions = [function for function in functions if function != '']
    filtered = list(set(functions))
    return len(functions) == len(filtered), functions


def run():
    """ Loop principal de ejecución"""

    # Objeto para representar la tabla vitual
    classes = Vtable()

    while (True):
        
        line = input().strip().split(' ')
        inst = line[0]

        # Definir clases
        if inst == "CLASS":
            name = line[1]
            if name in classes:
                print(f"Error. Clase {name} declarada previamente")
            else:
                # Se chequea si la clase hereda de otra
                if len(line) > 2 and line[2] == ":":
                    sup = line[3]
                    if sup not in classes:
                        print(f"Error. Clase {sup} no declarada previamente")
                    else:
                        valid, functions = filter(line[4:])
                        if valid:
                            # Añade la clase con su superclase
                            classes.add(name, functions, sup)
                        else:
                            print("Nombre de método repetido en la lista de métodos.")
                else:
                    # Añade la clase sin superclase
                    classes.add(name, line[2:])
        
        # Describir clases
        elif inst == "DESCRIBIR":
            name = line[1]
            if name not in classes:
                print(f"Error. Clase {name} no declarada previamente")
            response = classes.describe(name).strip()
            if response == "":
                print(f"La clase {name} no posee métoos virtuales." )
            else:
                print(response)

        elif inst == "SALIR":
            break

        else:
            print("Opción inválida")


if __name__ == "__main__":
    run()

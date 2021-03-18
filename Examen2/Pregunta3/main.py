from type_manager import TypeManager


def loop():
    ''' Flujo principal de lectura de input e interacción con el manejador'''
    
    manager = TypeManager()

    while True:

        tokens = input().split()
    
        if tokens[0] == "SALIR":
            break

        elif tokens[0] == "ATOMICO":

            if not manager.contains(tokens[1]):
                manager.insert_simple(tokens[1], int(tokens[2]), int(tokens[3]))
            else:
                print("Nombre %s definido previamente" % tokens[1])

        elif tokens[0] == "STRUCT":

            if not manager.contains(tokens[1]):
                if not all(manager.contains(name) for name in tokens[2:]):
                    print("Tipo de dato en la lista no definido previamente")
                else:
                    manager.insert_composed(tokens[1], tokens[2:], 0)
            else:
                print("Nombre %s previamente definido" % tokens[1])

        elif tokens[0] == "UNION":

            if not manager.contains(tokens[1]):
                if not all(manager.contains(name) for name in tokens[2:]):
                    print("Tipo de dato en la lista no definido previamente")
                else:
                    manager.insert_composed(tokens[1], tokens[2:], 1)
            else:
                print("Nombre %s previamente definido" % tokens[1])

        elif tokens[0] == "DESCRIBIR":
            if manager.contains(tokens[1]):
                manager.describe(tokens[1])
            else:
                print("Nombre %s no definido" % tokens[1])
        else:
            print("Entrada Inválida")


if __name__ == '__main__':
    loop()

class ClassEntry:
    """ Clase usada para instanciar objetos que representan a las clases
        declaradas en nuestro programa """

    def __init__(self, name, functions, *args):
        """ Constructor de una entrada en nuestra lista de clases en el programa """
        self.name = name
        self.functions = functions
        # Superclase
        if len(args) > 0:
            self.parent = args[0]
        else:
            self.parent = None

    @staticmethod
    def format(function, class_name):
        """ Función auxiliar para crear el nombre completo de una función """
        return function + " -> " + class_name + " :: " + function

    def list_functions(self):
        """ Lista todas las funciones que pueden ser llamadas por una clase """
        functions = dict()
        self.list_functions_recursive(functions)
        result = [ClassEntry.format(f, c) for f, c in functions.items()]
        result = sorted(result)
        return "\n".join(result)

    def list_functions_recursive(self, result):
        """ Almacena en el arreglo result las clases que pueden ser llamadas por
            la clase actual y luego se llama recursivamente con la superclase """
        for function in self.functions:
            if function not in result:
                result.update({function: self.name})

        if self.parent is not None:
            self.parent.list_functions_recursive(result)

        return result


class Vtable:
    """ Clase que representa la tabla virtual de nuestro programa """

    def __init__(self):
        """ Constructor de la clase """    
        self.classes = dict()

    def __contains__(self, item):
        """ Auxiliar para determinar si un nombre de clase se encuentra 
            en nuestra tabla """
        return item in self.classes

    def add(self, name, functions, *args):
        """ Añade una nueva entrada, asigna la superclase de ser necesario """
        if len(args) > 0:
            # Superclase
            parent_name = args[0]
            parent = self.classes[parent_name]
            entry = ClassEntry(name, functions, parent)
        else:
            entry = ClassEntry(name, functions)

        self.classes.update({name: entry})

    def describe(self, name):
        """ Enlista las funciones alcanzables desde la clase especificada """
        entry = self.classes[name]
        return entry.list_functions()

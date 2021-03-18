from typing import List, Tuple, Callable
from math import gcd
from itertools import permutations

# Representación de un Infinito. Puede incrementarse según sea necesario.
INF = 1 << 100


def lcm(a: int, b: int) -> int:
    ''' Minimo común múltiplo entre dos números'''
    return a // gcd(a, b) * b


class TypeManager:
    ''' Clase para representar el manejador de memoria '''

    def __init__(self):
        ''' Constructor de la clase'''
        self.simple_types = dict()
        self.composed_types = dict()

    def contains(self, name: str) -> bool:
        ''' Función para chequear si un tipo ha sido definido '''
        return name in self.simple_types or name in self.composed_types

    def insert_simple(self, name: str, size: int, allign: int):
        ''' Función para insertar un tipo atómico '''
        self.simple_types[name] = (allign, size)

    def insert_composed(self, name: str, names: List, datatype: int):
        ''' FUnción para insertar un struct o union '''
        self.composed_types[name] = (datatype, names)

    def describe(self, name: str):
        ''' Función para describir a un tipo determinado. Al momento de calcular el 
            desperdicio se ignora el posible desperdicio al final de el tipo que sólo
            podría ser calculado si se conociese el tamaño de la palabra '''
        print("Registros y registros variantes almacenados sin empaquetar:\n")
        (allign, size, waste) = self.unpacked_stats(name)
        print(f"Alineación: {allign}\nTamaño: {size}\nDesperdicio: {waste}\n")

        print("Registros y registros variantes empaquetados:\n")
        size = self.packed_stats(name)
        print(f"Alineación: Se ignora\nTamaño: {size}\nDesperdicio: 0\n")

        print("Registros y registros variantes reordenando campos:\n")
        (allign, size, waste) = self.optimal_stats(name)
        print(f"Alineación: {allign}\nTamaño: {size}\nDesperdicio: {waste}\n")

    def unpacked_stats(self, name: str) -> Tuple:
        ''' Función para obtener los valores (Alineación, tamaño y desperdicio)
            de un tipo determinado si los registros y registros variantes NO se almacenan
            con empaquetamiento'''
        if name in self.simple_types:
            # En caso de ser un tipo atómico, se retorna sus datos
            (allign, size) = self.simple_types[name]
            return (allign, size, 0)
        else:
            (datatype, names) = self.composed_types[name]
            # Se itera sobre el ordenamiento de tipos y se calcula su sestadísticas
            return self.current_order_stats(datatype, names, self.unpacked_stats)

    def optimal_stats(self, name: str) -> Tuple:
        ''' Función para calcular los valores (Alineación, tamaño y desperdicio) de
            un tipo determinado si el manejador reordenase de manera óptima los tipos '''
        if name in self.simple_types:
            # En caso de ser un tipo atómico, se retorna sus datos
            (allign, size) = self.simple_types[name]
            return (allign, size, 0)
        else:
            (datatype, names) = self.composed_types[name]
            allign = 1
            size = 0
            waste = INF
            if datatype:  # Union
                return self.current_order_stats(datatype, names, self.optimal_stats)
            else:  # Struct
                # Se prueban todas las distintas permutaciones de los tipos que contiene
                for order in permutations(names):
                    (a, s, w) = self.current_order_stats(datatype, order, self.optimal_stats)
                    if w < waste:
                        # Optimizamos tomando en cuenta el desperdicio
                        waste, allign, size = w, a, s
                return (allign, size, waste)

    def current_order_stats(self, datatype: bool, names: List, get_stats: Callable):
        ''' Función para iterar sobre un ordenamiento determinado de tipos, y calcular el tamaño
            total del tipo que los contiene, su desperdicio y la alineación que debería tener.
            Recibe el tipo de registro (variante o no), el ordenamiento de tipos, y la función
            a la que se debe llamar para resolver recursivamente cada uno de los tipos contenidos '''
        if datatype:  # Union

            # Llamada recursiva para generar las estadisticas de cada uno de los tipos contenidos
            stats = [get_stats(name) for name in names]
            # El tamaño es el máximo del tamaño de todos los tipos
            size = max(s for (_, s, _) in stats)
            allign = 1
            waste = INF
            # Se calcula la alineación y el desperdicio
            for (a, s, w) in stats:
                allign = lcm(allign, a)
                waste = min(waste, w + size - s)

            return (allign, size, waste)
        else:  # Struct

            allign = -1
            waste = 0
            size = 0
            for name in names:
                # Llamada recursiva para generar las estadisticas de cada uno de los tipos contenidos
                (a, s, w) = get_stats(name)

                # La alineación es la alineación del primero
                if allign == -1:
                    allign = a

                # Se calcula el offset que se deberá dejar como espacio para respetar las alineaciones
                offset = size % a

                # Se suma el desperdicio y tamaño a la respuesta
                waste += w
                size += s

                if offset:
                    # Si existe un offset, se aumenta el tamaño y el desperdicio
                    waste += a - offset
                    size += a - offset
            return (allign, size, waste)

    def packed_stats(self, name):
        ''' Función para obtener el tamaño de un tipo determinado si los registros 
            y registros variantes se almacenan con empaquetamiento. Notese que la 
            alineación no es importante para describir al tipo y el desperdicio será 0 
            si no se considera el desperdicio al final del tipo'''
        if name in self.simple_types:
            # Tipo simple
            (_, size) = self.simple_types[name]
            return size
        else:
            (datatype, names) = self.composed_types[name]
            if datatype:  # Union
                size = 0
                for name in names:
                    # Llamada recursiva sobre el tipo
                    size = max(size, self.packed_stats(name))
                return size
            else:  # Struct
                size = 0
                for name in names:
                    # Llamada recursiva sobre el tipo
                    s = self.packed_stats(name)
                    size += s
                return size

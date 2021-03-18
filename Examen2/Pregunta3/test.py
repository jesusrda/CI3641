import unittest
import sys
import io
from type_manager import TypeManager


class TestManager(unittest.TestCase):
    ''' Testing  function '''
    def setUp(self):
        self.manager = TypeManager()

    def test_insert_atom(self):
        self.manager.insert_simple("Int", 8, 8)
        self.manager.insert_simple("Char", 2, 8)
        self.assertTrue("Int" in self.manager.simple_types)
        self.assertTrue("Char" in self.manager.simple_types)
        self.assertEqual(self.manager.simple_types["Int"], (8, 8))
        self.assertEqual(self.manager.simple_types["Char"], (8, 2))
    
    def test_contains_atom_error(self):
        self.manager.insert_simple("Int", 8, 8)
        self.manager.insert_simple("Char", 2, 8)
        self.assertTrue(self.manager.contains("Int"))
        self.assertTrue(self.manager.contains("Char"))

    def test_insert_union(self):
        self.manager.insert_simple("Int", 8, 8)
        self.manager.insert_simple("Char", 2, 8)
        self.manager.insert_composed("Foo", ["Char", "Int"], 1)
        self.assertTrue("Foo" in self.manager.composed_types)
        self.assertEqual(self.manager.composed_types["Foo"], (1, ["Char", "Int"]))

    def test_contains_union(self):
        self.manager.insert_simple("Int", 8, 8)
        self.manager.insert_simple("Char", 2, 8)
        self.manager.insert_composed("Foo", ["Char", "Int"], 1)
        self.assertTrue(self.manager.contains("Foo"))

    def test_insert_struct(self):
        self.manager.insert_simple("Int", 8, 8)
        self.manager.insert_simple("Char", 2, 8)
        self.manager.insert_composed("Foo", ["Char", "Int"], 1)
        self.manager.insert_composed("Bar", ["Char", "Int", "Foo"], 0)
        self.assertTrue("Bar" in self.manager.composed_types)
        self.assertEqual(self.manager.composed_types["Bar"], (0, ["Char", "Int", "Foo"]))

    def test_contains_struct(self):
        self.manager.insert_simple("Int", 8, 8)
        self.manager.insert_simple("Char", 2, 8)
        self.manager.insert_composed("Foo", ["Char", "Int"], 1)
        self.manager.insert_composed("Bar", ["Char", "Int", "Foo"], 0)
        self.assertTrue(self.manager.contains("Bar"))


class TestDescribe(unittest.TestCase):
    ''' Test función de descripción '''
    def setUp(self):
        self.manager = TypeManager()
        self.output = io.StringIO()
        sys.stdout = self.output

    def tearDown(self):
        sys.stdout = sys.__stdout__
    
    def test_struct(self):
        
        self.manager.insert_simple("Bool", 1, 2)
        self.manager.insert_simple("Int", 4, 4)
        self.manager.insert_simple("Char", 2, 2)
        self.manager.insert_simple("Float", 8, 8)
        self.manager.insert_composed("Meta", ["Int", "Char", "Int", "Float", "Bool"], 0)
        self.manager.describe("Meta")
        output = self.output.getvalue()
        self.assertEqual("Registros y registros variantes almacenados sin empaquetar:\n\n"
                         + "Alineación: 4\nTamaño: 25\nDesperdicio: 6\n\n"
                         + "Registros y registros variantes empaquetados:\n\n"
                         + "Alineación: Se ignora\nTamaño: 19\nDesperdicio: 0\n\n"
                         + "Registros y registros variantes reordenando campos:\n\n"
                         + "Alineación: 4\nTamaño: 19\nDesperdicio: 0\n\n", output)
    
    def test_union(self):
        
        self.manager.insert_simple("Bool", 1, 2)
        self.manager.insert_simple("Int", 4, 4)
        self.manager.insert_simple("Float", 8, 6)
        self.manager.insert_composed("Meta", ["Bool", "Int", "Int"], 0)
        self.manager.insert_composed("Foo", ["Meta", "Int", "Float"], 1)
        self.manager.describe("Foo")
        output = self.output.getvalue()
        self.assertEqual("Registros y registros variantes almacenados sin empaquetar:\n\n"
                         + "Alineación: 12\nTamaño: 12\nDesperdicio: 3\n\n"
                         + "Registros y registros variantes empaquetados:\n\n"
                         + "Alineación: Se ignora\nTamaño: 9\nDesperdicio: 0\n\n"
                         + "Registros y registros variantes reordenando campos:\n\n"
                         + "Alineación: 12\nTamaño: 9\nDesperdicio: 0\n\n", output)
                          

if __name__ == '__main__':
    unittest.main()
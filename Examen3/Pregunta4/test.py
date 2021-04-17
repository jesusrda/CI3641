import unittest
from vtable import Vtable


class TestVtable(unittest.TestCase):
    ''' Testing  function '''
    def setUp(self):
        self.vtable = Vtable()

    def test_add(self):
        self.vtable.add("Nombre", ["1", "2"])
        self.assertTrue("Nombre" in self.vtable)
        self.assertEqual(["1", "2"], self.vtable.classes["Nombre"].functions)
        self.assertTrue(self.vtable.classes["Nombre"].parent is None)

    def test_add_with_super(self):
        self.vtable.add("Super", ["1", "2"])
        self.vtable.add("Nombre", ["1", "2"], "Super")
        self.assertTrue("Nombre" in self.vtable)
        self.assertTrue("Super" in self.vtable)
        self.assertEqual(["1", "2"], self.vtable.classes["Nombre"].functions)
        self.assertEqual(self.vtable.classes["Nombre"].parent.name, "Super")

    def test_describe(self):
        self.vtable.add("A", ["1", "2", "3"])
        self.vtable.add("B", ["2"], "A")
        self.vtable.add("C", ["3", "4"], "B")
        self.vtable.add("D", ["1", "2", "3", "4", "5"], "C")
        self.vtable.add("E", ["3", "5"], "C")
        self.assertEqual(self.vtable.describe("D"), "\n".join(["1 -> D :: 1",
                                                               "2 -> D :: 2",
                                                               "3 -> D :: 3",
                                                               "4 -> D :: 4",
                                                               "5 -> D :: 5"]))
        self.assertEqual(self.vtable.describe("E"), "\n".join(["1 -> A :: 1",
                                                               "2 -> B :: 2",
                                                               "3 -> E :: 3",
                                                               "4 -> C :: 4",
                                                               "5 -> E :: 5"]))


if __name__ == '__main__':
    unittest.main()

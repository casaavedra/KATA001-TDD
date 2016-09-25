from unittest import TestCase

from Numeros import Numeros

class NumerosTest(TestCase):
    # Iteración 1
    def test_numElementos(self):
        self.assertEqual(Numeros().numElementos(""), [0], "Cadena vacía")

    def test_numElementos_1(self):
        self.assertEqual(Numeros().numElementos("8"), [1], "Un elemento")

    def test_numElementos_2(self):
        self.assertEqual(Numeros().numElementos("8,2"), [2], "Dos elementos")

    def test_numElementos_N(self):
        self.assertEqual(Numeros().numElementos("8,2,9,0,5"), [5], "Cinco elementos")
        self.assertEqual(Numeros().numElementos("1,2,2,3,4,5"), [6], "Seis elementos")

    #Iteración 2
    def test_minimo(self):
        self.assertEqual(Numeros().minimo(""), [0, None], "No existe mínimo")

    def test_minimo_1(self):
        self.assertEqual(Numeros().minimo("1"), [1, 1], "Un elemento, 1 mínimo")

    def test_minimo_2(self):
        self.assertEqual(Numeros().minimo("8,2"), [2, 2], "Dos elementos, 2 mínimo")

    def test_minimo_N(self):
        self.assertEqual(Numeros().minimo("8,2,9,0,5"), [5, 0], "Cinco elementos, 0 mínimo")
        self.assertEqual(Numeros().minimo("1,2,2,3,4,5"), [6, 1], "Seis elementos, 1 mínimo")
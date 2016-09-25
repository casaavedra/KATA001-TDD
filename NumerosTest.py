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

    # Iteración 2
    def test_minimo(self):
        self.assertEqual(Numeros().minimo(""), [0, None], "No existe mínimo")

    def test_minimo_1(self):
        self.assertEqual(Numeros().minimo("1"), [1, 1], "Un elemento, 1 mínimo")

    def test_minimo_2(self):
        self.assertEqual(Numeros().minimo("8,2"), [2, 2], "Dos elementos, 2 mínimo")

    def test_minimo_N(self):
        self.assertEqual(Numeros().minimo("8,2,9,0,5"), [5, 0], "Cinco elementos, 0 mínimo")
        self.assertEqual(Numeros().minimo("1,2,2,3,4,5"), [6, 1], "Seis elementos, 1 mínimo")

    # Iteración 3
    def test_maximo(self):
        self.assertEqual(Numeros().maximo(""), [0, None, None], "No existe máximo")

    def test_maximo_1(self):
        self.assertEqual(Numeros().maximo("1"), [1, 1, 1], "Un elemento, 1 mínimo, 1 máximo")

    def test_maximo_2(self):
        self.assertEqual(Numeros().maximo("8,2"), [2, 2, 8], "Dos elementos, 2 mínimo, 8 máximo")

    def test_maximo_N(self):
        self.assertEqual(Numeros().maximo("8,2,9,0,5"), [5, 0, 9], "Cinco elementos, 0 mínimo, 9 máximo")
        self.assertEqual(Numeros().maximo("1,2,2,3,4,5"), [6, 1, 5], "Seis elementos, 1 mínimo, 5 máximo")

    # Iteración 4
    def test_promedio(self):
        self.assertEqual(Numeros().promedio(""), [0, None, None, None], "No existe promedio")

    def test_promedio_1(self):
        self.assertEqual(Numeros().promedio("1"), [1, 1, 1, 1], "Un elemento, 1 mínimo, 1 máximo, 1 promedio")

    def test_promedio_2(self):
        self.assertEqual(Numeros().promedio("8,2"), [2, 2, 8, 5], "Dos elementos, 2 mínimo, 8 máximo, 5 promedio")

    def test_promedio_N(self):
        self.assertEqual(Numeros().promedio("8,2,9,0,5"), [5, 0, 9, 4.8], "Cinco elementos, 0 mínimo, 9 máximo, 4.8 promedio")
        self.assertEqual(Numeros().promedio("1,2,2,3,4,6"), [6, 1, 6, 3.0], "Seis elementos, 1 mínimo, 6 máximo, 3 promedio")
from unittest import TestCase

from Numeros import Numeros

class NumerosTest(TestCase):
    def test_numElementos(self):
        self.assertEqual(Numeros().numElementos(""),[0],"Cadena vacía")

    def test_numElementos_1(self):
        self.assertEqual(Numeros().numElementos("8"), [1], "Un elemento")

    def test_numElementos_2(self):
        self.assertEqual(Numeros().numElementos("8,2"), [2], "Dos elementos")

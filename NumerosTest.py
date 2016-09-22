from unittest import TestCase

import Numeros

class NumerosTest(TestCase):
    def test_numElementos(self):
        self.assertEqual(Numeros().numElementos(""),[0],"Cadena vacía")

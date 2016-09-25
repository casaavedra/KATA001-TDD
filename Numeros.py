class Numeros:
    def numElementos(self, cadena):
        if cadena == "":
            return [0]
        else:
            return [len(cadena.split(','))]

    def minimo(self, cadena):
        array = []
        array = self.numElementos(cadena)

        if cadena == "":
            array.append(None)
            return array
        else:
            array.append(1)
            return array
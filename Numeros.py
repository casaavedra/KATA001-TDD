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
        elif "," in cadena:
            numeros = cadena.split(',')
            if numeros[0] < numeros[1]:
                array.append(int(numeros[0]))
            else:
                array.append(int(numeros[1]))
            return array
        else:
            array.append(int(cadena))
            return array
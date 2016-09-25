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

            for i in range(0, len(numeros)):
                if i == 0:
                    minimo = numeros[0]
                else:
                    if numeros[i] < minimo:
                        minimo = numeros[i]
            array.append(int(minimo))
            return array
        else:
            array.append(int(cadena))
            return array
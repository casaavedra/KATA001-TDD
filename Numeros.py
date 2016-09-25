class Numeros:
    def numElementos(self, cadena):
        if cadena == "":
            return [0]
        else:
            return [len(cadena.split(','))]

    def minimo(self, cadena):
        array = self.numElementos(cadena)

        if cadena == "":
            array.append(None)
        elif "," in cadena:
            numeros = cadena.split(',')

            for i in range(0, len(numeros)):
                if i == 0:
                    minimo = numeros[0]
                else:
                    if numeros[i] < minimo:
                        minimo = numeros[i]
            array.append(int(minimo))
        else:
            array.append(int(cadena))

        return array

    def maximo(self, cadena):
        array = self.minimo(cadena)

        if cadena == "":
            array.append(None)
        else:
            array.append(1)
        return array
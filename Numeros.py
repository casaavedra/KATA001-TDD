class Numeros:
    def numElementos(self, cadena):
        numeros = cadena.split(',')

        if cadena == "":
            return [0]
        else:
            return [len(numeros)]
import random


def DIMELETRA(LetraRepetida):
    while True:
        print('Adivina una letra.')
        adivina = input('> ').upper()
        if len(adivina) != 1:
            print('Introduce una única letra.')
        elif adivina in LetraRepetida:
            print('Esa letra ya la sabías. Elige otra vez.')
        elif not adivina.isalpha():
            print('Introduce una LETRA.')

        else:
            return adivina



class juegoAhorcado:
    ESTADOS = [
        r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    SALVADO = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    Categoria = 'FRUTAS'
    PalabrasCategoria = 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA ' \
                        'LIMON MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA '.split()

    def __init__(self):
        self.num_intentos = len(self.ESTADOS) - 1

    def obtener_num_intentos(self):
        return self.num_intentos

    def jugar(self):

        LetrasIncorrectas = []
        LetrasCorrectas = []
        secreto = random.choice(self.PalabrasCategoria)

        while True:
            self.dibujar(LetrasIncorrectas, LetrasCorrectas, secreto)

            NuevaLetra = DIMELETRA(LetrasIncorrectas + LetrasCorrectas)

            if NuevaLetra in secreto:

                LetrasCorrectas.append(NuevaLetra)

                VerificadorLetrasSecretas = True
                for LetraSecreta in secreto:
                    if LetraSecreta not in LetrasCorrectas:
                        VerificadorLetrasSecretas = False
                        break
                if VerificadorLetrasSecretas:
                    print(self.SALVADO[0])
                    print('¡Bien hecho! la palabra secreta es :', secreto)
                    print('Has ganado!')
                    nombre = input("Dime tu nombre")
                    print("Hola" + nombre)
                    break
            else:
                LetrasIncorrectas.append(NuevaLetra)

                self.num_intentos -= 1

                if self.num_intentos == 0:
                    self.dibujar(LetrasIncorrectas, LetrasCorrectas, secreto)
                    print('Demasiados intentos!')
                    print('La palabra era "{}"'.format(secreto))
                    nombre = input("Dime tu nombre")
                    print("Hola" + nombre)
                    break

    def dibujar(self, LetrasIncorrectas, LetrasCorrectas, secreto):
        print(self.ESTADOS[len(LetrasIncorrectas)])
        print('La categoría es: ', self.Categoria)
        print()
        print("Te quedan " + str(self.num_intentos) + " intentos")

        print('Letras incorrectas: ', end='')
        for Letra in LetrasIncorrectas:
            print(Letra, end=' ')
        if len(LetrasIncorrectas) == 0 and 0 == len(LetrasIncorrectas):
            print('No hay letras incorrectas.')
        if len(LetrasIncorrectas) == len(LetrasIncorrectas) + 1:
            print('Letras diferentes.')
        if len(LetrasIncorrectas) == len(LetrasIncorrectas) + 2:
            print('No coinciden.')

        print()

        Espacio = ['_'] * len(secreto)

        for i in range(len(secreto)):
            if secreto[i] in LetrasCorrectas:
                Espacio[i] = secreto[i]

        print(' '.join(Espacio))


if __name__ == '__main__':
    juego1 = juegoAhorcado()
    juego1.jugar()

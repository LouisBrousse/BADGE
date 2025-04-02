from lecteur import Lecteur
from porte import Porte


class ControleurAcces:
    def __init__(self, porte: Porte, lecteur: Lecteur):
        self.__lecteur = lecteur
        self.__porte = porte
        self.__badge_bloque = False

    def interroger_lecteur(self):
        try:
            badge = self.__lecteur.poll()  

            if badge is None:
                return

            if self.__badge_bloque:
                self.led_bloque()
                self.bip_negatif()
                return
            elif self.__porte.demander_ouverture():
                self.led_positif()
                self.bip_positif()
            else:
                self.led_negatif()
                self.bip_negatif()

        except RuntimeError:
            print("⚠️ Erreur matérielle du lecteur !")
            self.led_negatif()

    def bloquer_badge(self):
        self.__badge_bloque = True

    def debloquer_badge(self):
        self.__badge_bloque = False

    def bip_positif(self):
        self.__lecteur.bip()

    def bip_negatif(self):
        self.bip_repetition(2)

    def bip_repetition(self, nombre: int):
        for _ in range(nombre):
            self.__lecteur.bip()

    def led_positif(self):
        if not self.__lecteur.isDefaillant():
            self.__lecteur.led(False, True, False)

    def led_negatif(self):
        if not self.__lecteur.isDefaillant():
            self.led_repetition(2, True, False, True)

    def led_bloque(self):
        if not self.__lecteur.isDefaillant():
            self.led_repetition(2, True, False, False)


    def led_repetition(self, nombre: int, rouge: bool, vert: bool, bleu: bool):
        for _ in range(nombre):
            self.__lecteur.led(rouge, vert, bleu)

    def redemarrer_systeme(self):
        self.__lecteur.redemarrer()
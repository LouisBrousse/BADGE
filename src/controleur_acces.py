from lecteur import Lecteur
from porte import Porte


class ControleurAcces:
    def __init__(self, porte: Porte, lecteur: Lecteur):
        self.__lecteur = lecteur
        self.__porte = porte

    def interroger_lecteur(self):
        try:
            badge = self.__lecteur.poll()  

            if badge is None:
                self.led_aucun()
                return

            if self.__lecteur.isBadgeBlocked():
                self.led_bloque()
                self.bip_negatif()
            elif self.__porte.demander_ouverture():
                self.led_positif()
                self.bip_positif()
            else:
                self.led_negatif()
                self.bip_negatif()

        except RuntimeError:
            print("⚠️ Erreur matérielle du lecteur !")
            self.led_negatif()

    def bip_positif(self):
        self.__lecteur.bip()

    def bip_negatif(self):
        self.bip_repetition(2)

    def bip_repetition(self, nombre: int):
        for _ in range(nombre):
            self.__lecteur.bip()

    def led_positif(self):
        self.__lecteur.led(False, True, False)

    def led_negatif(self):
        self.led_repetition(2, True, False, True)

    def led_bloque(self):
        self.led_repetition(2, True, False, False)

    def led_aucun(self):
        self.__lecteur.led(False, False, False)

    def led_repetition(self, nombre: int, rouge: bool, vert: bool, bleu: bool):
        for _ in range(nombre):
            self.__lecteur.led(rouge, vert, bleu)

    def redemarrer_systeme(self):
        self.__lecteur.redemarrer()
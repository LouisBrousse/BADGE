from lecteur import Lecteur
from porte import Porte


class ControleurAcces:
    def __init__(self, porte: Porte, lecteur: Lecteur):
        self.__lecteur = lecteur
        self.__porte = porte

    def interroger_lecteur(self):
        if self.__lecteur.poll() is not None:
            try:
                self.__porte.demander_ouverture()
                self.led_positif()  # Lumière verte
                self.bip_positif()  # Lumière verte
                
            except Exception:
                self.led_negatif()  # Lumière violette
                self.bip_negatif()
        else:
            self.led_aucun()  # Lumière éteinte
                
    
    def bip_positif(self):
        self.__lecteur.bip()

    def bip_negatif(self):
        for i in range(2):
            self.__lecteur.bip()
    
    def led_positif(self):
        self.__lecteur.led(False, True, False)

    def led_negatif(self):
        for i in range(2):
            self.__lecteur.led(True, False, True)
    
    def led_aucun(self):
        self.__lecteur.led(False, False, False)
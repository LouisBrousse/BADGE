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
                self.__lecteur.led(False, True, False)  # Lumière verte
                self.__lecteur.bip()
            except Exception:
                for i in range(2):
                    self.__lecteur.led(True, False, True)  # Lumière violette
                    self.__lecteur.bip()
                raise
        
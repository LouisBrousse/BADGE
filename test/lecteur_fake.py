from lecteur import Lecteur


class Lecteurfake(Lecteur):
  
    def led(self, r: bool, g: bool, b: bool):
        self.couleur_affiches.add((r, g, b))

    
    def bip(self):
        self.__nombre_appels_bip +=1
        pass
    
    def __init__(self):
        self.__numero_badge_detecte = None
        self.__nombre_appels_bip =0
        self.couleur_affiches = []

    def poll(self) -> int | None:
        numero_detecte = self.__numero_badge_detecte
        self.__numero_badge_detecte = None
        return numero_detecte

    def simuler_presentation_badge(self):
        self.__numero_badge_detecte = 0

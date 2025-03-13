from lecteur import Lecteur

class Lecteurfake(Lecteur):
  
    def led(self, r: bool, g: bool, b: bool):
        if self.defaillance_led:
            raise Exception("Signal Lumineux défaillant")
        self.couleur_affiches.append((r, g, b))
    
    def simuler_defaillance_led(self) -> None:
        self.defaillance_led = True
    
    def bip(self) -> int | None:
        if self.defaillance_bip:
            raise Exception("Signal Sonore défaillant")
        self.nombre_appels_bip += 1
    
    def simuler_defaillance_bip(self) -> None:
        self.defaillance_bip = True
    
    def __init__(self) -> None:
        self.__numero_badge_detecte = None
        self.nombre_appels_bip = 0
        self.couleur_affiches = []
        self.defaillance_led = False
        self.defaillance_bip = False

    def poll(self) -> int | None:
        numero_detecte = self.__numero_badge_detecte
        self.__numero_badge_detecte = None
        return numero_detecte

    def simuler_presentation_badge(self) -> int | None:
        self.__numero_badge_detecte = 0
    


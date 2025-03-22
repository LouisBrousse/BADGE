from lecteur import Lecteur

class Lecteurfake(Lecteur):
  
    def __init__(self) -> None:
        self.__numero_badge_detecte = None
        self.nombre_appels_bip = 0
        self.couleur_affiches = []
        self.defaillance_led = False
        self.defaillance_bip = False
        self.badgebloque = False

    def poll(self) -> int | None:
        numero_detecte = self.__numero_badge_detecte
        self.__numero_badge_detecte = None 
        return numero_detecte

    def isBadgeBlocked(self):
        return self.badgebloque
    
    def bip(self) -> int | None:
        if self.defaillance_bip:
            return
        self.nombre_appels_bip += 1
    
    def led(self, r: bool, g: bool, b: bool):
        if self.defaillance_led:
            self.couleur_affiches.append((False, False, False))
            return
        self.couleur_affiches.append((r, g, b))
    
    def simuler_defaillance_led(self) -> None:
        self.defaillance_led = True
    
    def simuler_defaillance_bip(self) -> None:
        self.defaillance_bip = True

    def simuler_badge_bloque(self) -> None:
        self.badgebloque = True

    def simuler_presentation_badge(self) -> None:
        self.__numero_badge_detecte = 0
    
    def redemarrer(self):
        self.__numero_badge_detecte = None 
        self.defaillance_led = False
        self.defaillance_bip = False
        self.badgebloque = False

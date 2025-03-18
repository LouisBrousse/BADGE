from lecteur import Lecteur
from badge import Badge

class Lecteurfake(Lecteur, Badge):
  
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
        self.badge_bloque_admin = False

    def poll(self) -> int | None:
        numero_detecte = self.__numero_badge_detecte
        self.__numero_badge_detecte = None
        return numero_detecte

    def simuler_presentation_badge(self, badge: Badge) -> int | None:
        self.__numero_badge_detecte = badge.numero
        self.badge_bloque_admin = badge.bloque_admin

    def controle_admin(self) -> bool:
        return self.badge_bloque_admin
from lecteur import Lecteur

class LecteurDummy(Lecteur):
  
    def __init__(self) -> None:
        self.nombre_appels_bip = 0
        self.couleur_affiches = []
        self.badgebloque = False

    def poll(self) -> int | None:
        raise RuntimeError()

    def isBadgeBlocked(self) -> bool:
        return False

    def bip(self) -> int | None:
        return None

    def led(self, r:bool, g:bool, b:bool):
        return self.couleur_affiches.append((r, g, b))
    
    def simuler_presentation_badge(self):
        self.poll()

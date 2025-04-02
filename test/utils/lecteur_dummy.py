from lecteur import Lecteur

class LecteurDummy(Lecteur):
  
    def __init__(self) -> None:
        self.nombre_appels_bip = 0
        self.couleur_affiches = []
        self.defaillance_led = False
        self.defaillance_bip = False

    def poll(self) -> int | None:
        raise RuntimeError()

    def bip(self) -> int | None:
        return None

    def led(self, r:bool, g:bool, b:bool):
        return self.couleur_affiches.append((r, g, b))
    
    def simuler_presentation_badge(self):
        self.poll()

    def isDefaillant(self) -> bool:
        return self.defaillance_led or self.defaillance_bip
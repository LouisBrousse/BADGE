from porte import Porte


class PorteSpy(Porte):
    def __init__(self):
        self.signal_ouverture_reçu = False

    def demander_ouverture(self):
        self.signal_ouverture_reçu = True
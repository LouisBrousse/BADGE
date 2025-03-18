import abc

class Lecteur(abc.ABC):
    # Renvoie le numéro du badge détecté, None sinon. Seul un badge cryptographiquement valide sera détecté.
    @abc.abstractmethod
    def poll(self) -> int | None:
        pass

    @abc.abstractmethod
    def bip(self) -> int | None:
        pass

    @abc.abstractmethod
    def led(self, r:bool, g:bool, b:bool):
        pass

    @abc.abstractmethod
    def simuler_presentation_badge(self, Badge) -> bool:
        pass

    @abc.abstractmethod
    def controle_admin(self) -> bool:
        pass
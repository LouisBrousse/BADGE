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
    def isDefaillant(self) -> bool:
        pass
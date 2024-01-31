from abc import ABC, abstractmethod

class Langue(ABC):
    @abstractmethod
    def bien_dit(self) -> str:
        pass

    @abstractmethod
    def dit_bonjour(self, moment) -> str:
        pass

    @abstractmethod
    def au_revoir(self, moment) -> str:
        pass
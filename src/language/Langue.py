from abc import ABC, abstractmethod

class Langue(ABC):
    @abstractmethod
    def bien_dit(self) -> str:
        pass

    @abstractmethod
    def dit_bonjour(self) -> str:
        pass
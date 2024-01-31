from src.language.Langue import Langue


class LangueSpy(Langue):
    __bien_dit = False

    def bien_dit(self):
        self.__bien_dit = True
        return ""

    def bien_dit_appel(self):
        return self.__bien_dit

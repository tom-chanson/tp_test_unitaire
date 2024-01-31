from src.language.Langue import Langue


class LangueSpy(Langue):
    __bien_dit = False
    __dit_bonjour = False

    def bien_dit(self):
        self.__bien_dit = True
        return ""

    def bien_dit_appel(self):
        return self.__bien_dit
    
    def dit_bonjour(self):
        self.__dit_bonjour = True
        return ""
    
    def dit_bonjour_appel(self):
        return self.__dit_bonjour
    


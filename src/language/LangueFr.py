import src.language.Langue as Langue
from src.moment import Moment


class LangueFr(Langue.Langue):
    def bien_dit(self):
        return "Bien dit"
    
    def dit_bonjour(self):
        return "Bonjour"
    
    def au_revoir(self):
        return "Au revoir"
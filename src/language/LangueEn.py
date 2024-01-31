import src.language.Langue as Langue
from src.moment import Moment

class LangueEn(Langue.Langue):
    def bien_dit(self):
        return "Well said"
    
    def dit_bonjour(self, moment):
        match moment:
            case Moment.MATIN:
                return "Good morning"
            case Moment.APRES_MIDI:
                return "Good afternoon"
            case Moment.SOIR:
                return "Good evening"
            case Moment.NUIT:
                return "Good night"
            case _:
                return "Hello"
    
    def au_revoir(self):
        return "Goodbye"
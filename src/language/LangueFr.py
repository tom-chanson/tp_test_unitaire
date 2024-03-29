import src.language.Langue as Langue
from src.moment import Moment


class LangueFr(Langue.Langue):
    def bien_dit(self):
        return "Bien dit"
    
    def dit_bonjour(self, moment):
        match moment:
            case Moment.MATIN:
                return "Bonjour"
            case Moment.APRES_MIDI:
                return "Bon après-midi"
            case Moment.SOIR:
                return "Bonsoir"
            case Moment.NUIT:
                return "Bonne nuit"
            case _:
                return "Salut"
    
    def au_revoir(self, moment):
        match moment:
            case Moment.MATIN:
                return "Au revoir_AM"
            case Moment.APRES_MIDI:
                return "Au revoir_PM"
            case Moment.SOIR:
                return "Au revoir_SOIR"
            case Moment.NUIT:
                return "Au revoir_NUIT"
            case _:
                return "Au revoir"
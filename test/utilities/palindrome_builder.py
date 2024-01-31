from src.palindrome import Palindrome
from test.utilities.LangueStub import LangueStub



class PalindromeBuilder:
    __langue = LangueStub()

    def build(self):
        return Palindrome(self.__langue)
    
    def set_langue(self, langue):
        self.__langue = langue
        return self

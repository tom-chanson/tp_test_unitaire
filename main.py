from src.palindrome import Palindrome

if __name__ == '__main__':
    palindrome = Palindrome.defaultConstructeur()
    print(palindrome.palindrome("kayak"))
    print(palindrome.palindrome("bonjour"))
    print(palindrome.palindrome("radar"))
    print(palindrome.palindrome("ressasser"))
    print(palindrome.palindrome("rotor"))
    print(palindrome.palindrome("sagas"))
    print(palindrome.palindrome("solo"))
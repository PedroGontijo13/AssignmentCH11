#Define a class and a static method that receives a string (word) and reverses it and returns
#it.

import string

class Words:
    def __init__(self, word):
        self._word = word
    def reverseWord(self):
        size = len(self._word)
        size = self._word[size::-1]
        self._word = size
        return self._word

def main():
    word = str(input("Digit a word: "))
    Word1 = Words(word)
    reverse1 = Word1.reverseWord()
    print(reverse1)
main()
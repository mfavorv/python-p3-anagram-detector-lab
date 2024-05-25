# your code goes here!
class Anagram:
    def __init__(self, word):
      self.word = word  

    def match(self, possible_anagrams):
        anagrams = []
        for  a in  possible_anagrams:
            letters = [letter for letter in a]
            init_letters = (l for l in self.word)
            if sorted(letters) == sorted(init_letters):
                  anagrams.append(a)

        if len(anagrams) > 0 :
            print(anagrams)
            return anagrams
        else : return []

listen = Anagram("listen")
listen.match(['enlists', 'google', 'inlets', 'banana'])
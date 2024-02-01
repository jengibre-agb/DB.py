import nltk
from nltk.corpus import words

nltk.download('words')

def find_anagrams(word):
  
    anagrams = []
    for w in words.words():
        if sorted(word) == sorted(w):
            anagrams.append(w)

    return anagrams



#Don´t remember what we were doing here
"""
def main():

  word = input("Enter a word: ")
  anagrams = find_anagrams(word)
  if anagrams:
    print("Anagrams of", word, "are:", ", ".join(anagrams))
  else:
        print("No anagrams found for " + word)
if __name__ == "__main__":
      main()
"""

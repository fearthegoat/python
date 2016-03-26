# -*- coding: utf-8 -*-
# Bilingual dictionary: take a phrase in one
# language and translate it one word at a time
# into another. In this case, we're using:
# Spanish
#

translations = {
  "merry":"feliz",
  "christmas":"navidad",
  "and":"y",
  "happy":"feliz",
  "new":"nuevo",
  "year":"año"
}

def convert_input(phrase):
  split_phrase = phrase.split()
  for word in split_phrase:
    if word.lower() in translations:
      print(translations[word.lower()], end=" ")
    else:
      print(word, end=" ")
  print()

user_said = input("Please enter a phrase:")

convert_input(user_said)

# for word in split_phrase:
#   spanish_word = translations.get(word.lower(),word)
#   spanish_phrase.append(spanish_word)
# spanish_phrase = " ".join(spanish_phrase)
# print("In Spanish, that's:", spanish_phrase)
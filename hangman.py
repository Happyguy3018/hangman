import random
import string
import re

WORDLIST_FILENAME = "words.txt"


def sort(get_available_letters):
  '''
  У данному випадку сортує набір букв
  '''
  get_available_letters=list(get_available_letters)
  get_available_letters.sort()
  get_available_letters=''.join(get_available_letters)
  return get_available_letters



def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist
def my_load_words():
    '''
    Все те саме тільки на виході str
    '''
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    wordlist=str(wordlist)
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, my_word):#YEP В кінці
  secret_word=list(secret_word)
  my_word=list(my_word)
  if secret_word==my_word:
    return True
  else:
    return False


def get_available_letters(my_word='', small_eng=set(string.ascii_lowercase)):#YEP
  #ПОВЕРТАЄ МНОЖИНУ БЕЗ ПОРЯДКУ #ПОВЕРТАЄ МНОЖИНУ БЕЗ ПОРЯДКУ#ПОВЕРТАЄ МНОЖИНУ БЕЗ ПОРЯДКУ#ПОВЕРТАЄ МНОЖИНУ БЕЗ ПОРЯДКУ
    my_word=set(my_word)
    return small_eng.difference(my_word)


def get_guessed_word(secret_word, letters_guessed, my_word):# YEP
  secret_word=list(secret_word)
  letters_guessed=list(letters_guessed)
  my_word=list(my_word)
  for i in range(0, len(secret_word)):
    if secret_word[i]==letters_guessed[0]:
      my_word.pop(i)
      my_word.insert(i, letters_guessed[0])
  while len(my_word)>len(secret_word):
    my_word.remove(my_word[-1])
  my_word=''.join(my_word)
  secret_word=''.join(secret_word)
  letters_guessed=''.join(letters_guessed)
  return my_word
        



      

def hangman_hard(secret_word, my_word, letters_counter, lives, warnings):
      if is_word_guessed(secret_word, my_word)==True:
        print("Congratulations, you won! Your total score for this game is:", lives*len(secret_word))
        return
      correct_word=False
      print("You have {} warnings left.".format(warnings))
      print("You have {} guesses left.".format(lives))
      while correct_word==False:
        if warnings<=0 and lives!=0:
          lives-=1
          warnings+=3
        if lives<0:
          return print("Sorry, you ran out of guesses. The word was else")
        if warnings<0:
          return print("Sorry, you ran out of guesses. The word was else")
        letters_guessed=str(input("Please guess a letter: "))
        letters_guessed=re.sub(r'\s+', '', letters_guessed)
        if len(letters_guessed)>1:
          warnings-=1 
          my_word=''.join(my_word)
          print("Oops! That is not a valid letter. You have {} warnings left".format(warnings), my_word)
          print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
          continue
        if letters_guessed not in string.ascii_lowercase:
          warnings-=1 
          my_word=''.join(my_word)
          print("Oops! That is not a valid letter. You have {} warnings left:".format(warnings), my_word)
          print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
          continue
        if letters_guessed in my_word:
          warnings-=1
          print("You have {} warnings left.".format(warnings))
          print("You have {} guesses left.".format(lives))
          print("Available letters: {}".format(sort((get_available_letters(letters_counter)))))
          print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
          continue
        if letters_guessed not in secret_word and letters_guessed in ['a', 'e', 'y', 'i', 'o']:
          letters_counter.append(letters_guessed)
          lives-=2
          my_word=''.join(my_word)
          print("Oops! That letter is not in my word: ", my_word)
          print("Available letters: {}".format(sort((get_available_letters(letters_counter)))))
          print("You have {} guesses left.".format(lives))
          print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
          continue
        elif letters_guessed not in secret_word:
          letters_counter.append(letters_guessed)
          lives-=1
          my_word=''.join(my_word)
          print("Oops! That letter is not in my word: ", my_word)
          print("Available letters: {}".format(sort((get_available_letters(letters_counter)))))
          print("You have {} guesses left.".format(lives))
          print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
          continue
        else:
          letters_counter.append(letters_guessed)
          letters_guessed=str(letters_guessed)
          correct_word=True
        print("Good guess: ", get_guessed_word(secret_word, letters_guessed, my_word))
        print("Available letters: {}".format(sort((get_available_letters(letters_counter)))))
        print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
        return hangman_hard(secret_word, get_guessed_word(secret_word, letters_guessed, my_word), letters_counter, lives, warnings)


        



def match_with_gaps(my_word,other_word):
    my_word, other_word = list(my_word), list(other_word)
    if len(my_word)!=len(other_word):
        return False
    for i in range(len(my_word)):
        if my_word[i]==other_word[i] or other_word[i]=='_ ' or other_word[i]=='_':
            return True
    return False


def show_possible_matches(my_word):
  '''
  створює шаблон і за ним підбирає слова для підказки
  '''
  my_word=list(my_word)
  for i in range(len(my_word)):
      if my_word[i]=='_':
          my_word.pop(i)
          my_word.insert(i, ' \\w ')
  my_word.insert(0, '[^\w]') 
  my_word.append('[^\w]')
  my_word=''.join(my_word)
  my_word=re.sub(r'\s+', '', my_word)
  possible_words=re.findall(my_word, my_load_words())
  possible_words=set(possible_words)
  possible_words=' '.join(possible_words)
  return print(possible_words)


def hangman_simple(secret_word, my_word, letters_counter, lives, warnings):
  correct_word=False
  while correct_word==False:
    if is_word_guessed(secret_word, my_word)==True:
      print("Congratulations, you won! Your total score for this game is:", lives*len(secret_word))
      return
    print("You have {} warnings left.".format(warnings))
    print("You have {} guesses left.".format(lives))
    if warnings<=0 and lives!=0:
      lives-=1
      warnings+=3
    if lives<0:
      return print("Sorry, you ran out of guesses. The word was else")
    if warnings<0:
      return print("Sorry, you ran out of guesses. The word was else")
    letters_guessed=str(input("Please guess a letter: "))
    if letters_guessed=='help':
      show_possible_matches(my_word)
      letters_guessed=str(input("Please guess a letter: "))
    letters_guessed=re.sub(r'\s+', '', letters_guessed)
    if len(letters_guessed)>1 or len(letters_guessed)<1:
      warnings-=1 
      my_word=''.join(my_word)
      print("Oops! That is not a valid letter. You have {} warnings left".format(warnings), my_word)
      print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
      continue
    if letters_guessed=='help':
      print(show_possible_matches(my_word))
    if letters_guessed not in string.ascii_lowercase:
      warnings-=1 
      my_word=''.join(my_word)
      print("Oops! That is not a valid letter. You have {} warnings left:".format(warnings), my_word)
      print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
      continue
    if letters_guessed in my_word:
      warnings-=1
      print("You have {} warnings left.".format(warnings))
      print("You have {} guesses left.".format(lives))
      print("Available letters: {}".format(sort((get_available_letters(letters_counter)))))
      print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
      continue
    if letters_guessed not in secret_word and letters_guessed in ['a', 'e', 'y', 'i', 'o']:
      letters_counter.append(letters_guessed)
      lives-=2
      my_word=''.join(my_word)
      print("Oops! That letter is not in my word: ", my_word)
      print("Available letters: {}".format(sort((get_available_letters(letters_counter)))))
      print("You have {} guesses left.".format(lives))
      print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
      continue
    elif letters_guessed not in secret_word:
      letters_counter.append(letters_guessed)
      lives-=1
      my_word=''.join(my_word)
      print("Oops! That letter is not in my word: ", my_word)
      print("Available letters: {}".format(sort((get_available_letters(letters_counter)))))
      print("You have {} guesses left.".format(lives))
      print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
      continue
    else:
      letters_counter.append(letters_guessed)
      letters_guessed=str(letters_guessed)
      correct_word=True
    print("Good guess: ", get_guessed_word(secret_word, letters_guessed, my_word))
    print("Available letters: {}".format(sort((get_available_letters(letters_counter)))))
    print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
    get_guessed_word(secret_word, letters_guessed, my_word)
    return hangman_simple(secret_word, get_guessed_word(secret_word, letters_guessed, my_word), letters_counter, lives, warnings)

# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.

def hangman(secret_word):
  my_word, letters_counter=[], []
  n=len(secret_word)
  while n>0:#Ствоює слово у якому будть позначатись вгадані літери
    my_word.append('_')
    n-=1
  lives, warnings=6, 3
  print("Welcome to the game Hangman!")
  print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
  print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
  print("You have 6 guesses left.")
  print("Available letters: {}".format(string.ascii_lowercase))
  return hangman_hard(secret_word, my_word, letters_counter, lives, warnings)

def hangman_with_hints(secret_word):
  my_word, letters_counter=[], []
  n=len(secret_word)
  while n>0:#Ствоює слово у якому будть позначатись вгадані літери
    my_word.append('_')
    n-=1
  lives, warnings=6, 3
  print("Welcome to the game Hangman with hints!")
  print("I am thinking of a word that is {} letters long.".format(len(secret_word)))
  print("_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ ")
  print("Print 'help'for take list of possible words ")
  print("You have 6 guesses left.")
  print("Available letters: {}".format(string.ascii_lowercase))
  return hangman_simple(secret_word, my_word, letters_counter, lives, warnings)

if __name__ == "__main__":
  x=input("Enter '1' for handman and enter whatever you want for handman with hints ")
  secret_word = choose_word(wordlist)
  if x=='1':
    hangman(secret_word)
  else:
    hangman_with_hints(secret_word)

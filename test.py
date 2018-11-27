import random
import re
import string
WORDLIST_FILENAME = "words.txt"
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
    wordlist=str(wordlist)
    return wordlist

def show_possible_matches(my_word):
    my_word=list(my_word)
    for i in range(len(my_word)):
        if my_word[i] == '_' or my_word[i]=='_ ':
            my_word.pop(i)
            my_word.insert(i, ' \\w ')
     for word in line.split():
        print(type(word))
    my_word.insert(0, '[^\w]') 
    my_word.append('[^\w]')
    my_word=''.join(my_word)
    my_word=re.sub(r'\s+', '', my_word)
    possible_words=re.findall(my_word, load_words())
    possible_words=set(possible_words)
    possible_words=' '.join(possible_words)
    return possible_words
my_word=input()
d=input()
if d=='help':
    print(show_possible_matches(my_word))

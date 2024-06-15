# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
# import randon function used to words in random choose
import random
import string

WORDLIST_FILENAME = "words.txt"


def load_words():
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
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


def is_word_guessed(secret_word, letters_guessed):
    for i in secret_word:
       if i not in letters_guessed:
        return (False)
    return (True)
def get_guessed_word(secret_word, letters_guessed):
    J = ""
    for i in secret_word:
      if i in letters_guessed:
        J+=i
      else:
         J+="_ "
    return J
# this function is used available letter 
def get_available_letters(letters_guessed):
    
    storage_of_string=string.ascii_lowercase
    for i in letters_guessed:
      storage_of_string=storage_of_string.replace(i,"")
    return storage_of_string

# main function
def hangman(secret_word):
  letters_guessed=[]
  print ("welcome to the game hangman!")
  
  guess=6
  warning=3
  vowel="aeiou"
  # print(secret_word)
  print("available letters:" ,get_available_letters(letters_guessed))
  print("word that is",len(secret_word),"letters long")
  print("you have",guess," guesses")
  print("you have 3 warning")
  print("if you guess a vowel and it is not in my word i will decrease 2 guesses")
  print("if you guess a non alphabatic key you will lose 1 warning")
  while guess>0:
    if guess<2:
       print("press * to get hint")
      #  i called word guessed function
    if is_word_guessed(secret_word, letters_guessed):
      print("🎉"*10,"You Won The Game","🎉"*10)
      num=0
      arun=string.ascii_lowercase
      # this function appand the string 
      for i in arun:
        if(i in secret_word):
           num+=1
           total=num*guess
      print("your score is:",total)
    print("available letters:" ,get_available_letters(letters_guessed))
    print("_"*46)
    # user input 
    user=input("enter a guess letter : ")
    if user.isalpha():
        user=user.lower()
        # user input the letter is not in guessed word 
        if user in letters_guessed:
          print("oops the letter is already exist : ",user)
          warning=warning-1
          print("you have a warning : ",warning)
        letters_guessed.append(user)
        # user input is correct run this if statement
        if user in secret_word:
            print(get_guessed_word(secret_word, letters_guessed))
            print ("your guess is correct")
        else:
          # user input the letter is vowel
          if user in vowel:
            print ("oops you entered a wrong letter : ",user)
            guess=guess-2
            print("your guess is : ",guess)
            if guess==0:
               print("better luck next time")
               print(secret_word)
          #  the guess is grate then 1 print this function 
          elif guess>=1:
            print("oops you entered a wrong letter : ",user)
            guess=guess-1
            print("your guess is : ",guess)
            if guess==0:
               print("better luck next time")
               print("the secret word is : ",secret_word)
          #  user not won the game print this function
          else:
             print("better luck next time")
             print("the secret word is : ",secret_word)
    else:
      # user give the hint function 
      if(user =="*"):
         print(show_possible_matches(get_guessed_word(secret_word,letters_guessed)))
      
      print("oops you enterd a non alphabet letter")
      # warning is grate then 0 print this function
      if warning>0:
         print("you have ",warning-1,"warnings")
      else:
      # warning is less then or equal 0 print this function
         if warning<=0:
          guess=guess-1
          print("your guess is : ",guess)
      warning=warning-1
      
      
# this function is replace the space 
def match_with_gaps(my_word, other_word):
    my_word = my_word.replace(" ","")
    if(len(my_word)==len(other_word)):
      # this "for" condition check the my word  
        for i in range(len(my_word)):
          if(my_word[i]=="_"):
            pass
          else:
            if(my_word[i]!=other_word[i]):
              return False 
        return True
# the user hint function
def show_possible_matches(my_word):
    lists=[] 
  # this "for" condition check the wordlist
    for ch in wordlist:
      # this if condition is call the match_with_gaps function 
      if(match_with_gaps(my_word,ch)):
        lists.append(ch)
    return lists











def hangman_with_hints(secret_word):
    hangman(secret_word)



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)


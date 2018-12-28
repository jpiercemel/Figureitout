from __future__ import print_function #Print function that allows to print to screen.
'''This code is designed to Figure out how Github works to collaborate
December 28, 2018.  Westhill Schools John Pierce'''

def figure_it_out():
    wordy = str(raw_input ('Enter a word to guess letters:    '))
    guess = str(raw_input ('Guess the letters in the secrect word.'))
    for letter in wordy:
        if letter in guess:
                print (letter, end="") 
        else:
            if letter == " ":
                    print(" ",end="")
            else:
                    print ("-",end="")
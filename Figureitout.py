from __future__ import print_function #Print function that allows to print to screen.
'''This code is designed to Figure out how Github works to collaborate
December 28, 2018.  Westhill Schools John Pierce'''

def figure_it_out():
    wordy = str(raw_input ('Enter a word to guess letters:    '))
    guess = str(raw_input ('Guess the letters in the secrect word.'))
    score = 0
    wrong = 0
    for letter in wordy:
        if letter in guess:
            score += 1
            print (letter, end="") 
            
        else:
            wrong +=1
            if letter == " ":
                print(" ",end="")
            else:
                print ("-",end="")
    print ('Your score is ', score, '!')
    print ('The number of wrong letters is ',wrong, '.') 
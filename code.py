#Modules
import random
import time

#Functions
def secretWord():
    
    '''
    Function will access a file filled with common english words
    A random number will be generated and the word it corresponds to is saved
    '''
    
    words = open('hiddenWords.txt') #Opens the words file

    wordList = words.readlines() #Allows the code to read the lines of the file
    
    secretNumber = random.randint(0,len(wordList)) #Generates a random number
    
    importantWord = wordList[secretNumber].replace('\n', '') #Removes the extra character from the end of the line
    
    return importantWord #Saves the word pulled
    
def hangmanImage(number):
    
    '''
    Saves ascii images in a list and will return whatever ascii image is called
    '''
    
    #List of images
    #Taken from chrishorton/hangmanwordbank.py
    
    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    
    return HANGMANPICS[number]


#Introduction to Game

print('Welcome to Hangman!\n')

#Rules
print('The rules are simple:\n')

print('''
Your aim is to guess the hidden word
You can guess one letter per turn
You have up to six incorrect guesses to work with\n
Each turn you have the opportunity to guess the entire word
However, if your guess is wrong, it will count as an incorrect guess
''')

print('Have fun!\n')

print(hangmanImage(0),"\n") #Calls first hangman ascii image

#Gameplay format

while True: #Continuous loop

    keyWord = [] #The word that will be displayed
    
    letterBank = [] #The number of words guessed
    
    incorrectGuesses = 0 #Number of incorrect guesses
    
    hangmanWord = list(secretWord()) #The hidden word is chosen as a list to easily iterate
    
    for letter in hangmanWord:#Sets up keyword by adding the correct amount of spaces as they correspond to the length of the hangmanWord
    
        keyWord.append('_')
    
    print('Choosing word...\n')
    
    try: #Pauses to emulate thinking, code block is used throughout program
    
        time.sleep(1)
        
    except KeyboardInterrupt:
        
        print("\nDon't interrupt me!\n")
    
    print(' '.join(keyWord)) #Presents the word
    
    while incorrectGuesses < 6: #Loops until user runs out of guesses or wins
        
        while True: #Ensures user guesses each letter once
            
            while True: #Forces the user to enter a letter not a number
            
                try:
                
                    userGuess = (input('\nEnter a letter: ')) #User guesses a letter
                    
                    if userGuess.isalpha() == False: #Doesn't allow numbers or special characters
                        
                        raise Exception('Only letters!')
                    
                    if len(userGuess) > 1: #Only allows a single letter to be guessed
                        
                        raise Exception('Only single letters!')
                    
                    break
                    
                except KeyboardInterrupt:
                    
                    print('\nDo not interrupt me!')
                
                except Exception as e:
                    
                    print(e)
            
            if userGuess in letterBank: #Runs if the user has already guessed a letter
                
                print('Letter already guessed')
                
            else:
                
                break
            
        letterBank.append(userGuess) #Adds the users guess to the word
        
        for letter in range(0, len(hangmanWord)): #Will iterate through every letter in the hidden word
            
            if hangmanWord[letter] == userGuess: #If the guess matches a letter in the word
                
                keyWord[letter] = userGuess #The correct guessed letter replaces the letter position of the keyWord
        
        try:
    
            time.sleep(1)
        
        except KeyboardInterrupt:
        
            print("\nDon't interrupt me!\n")
        
        if userGuess not in hangmanWord: #If it is not in the word
            
            print('Letter is not in word')
            
            incorrectGuesses += 1 #If the user enters the wrong letter, the flag increases by 1
        
        print(' '.join(keyWord)) #Shows the current status of the word
        
        print(' '.join(letterBank)) #Shows the letters guessed
        
        print('\nNumber of incorrect guesses:',incorrectGuesses) #Running counter
        
        print(hangmanImage(incorrectGuesses)) #Displays the newest state of the hangman image
        
        try:
    
            time.sleep(1)
        
        except KeyboardInterrupt:
        
            print("\nDon't interrupt me!\n")
        
        if incorrectGuesses < 6 and ''.join(keyWord) != ''.join(hangmanWord): #Allows users to guess the full word as long as they have less than 6 incorrect guesses
        
            while True:
            
                try:
                
                    userFullGuess = input('\nWould you like to guess the entire word? (y/n): ').lower() #Asks if they want to guess the full word
                    
                    if userFullGuess == 'y':
                        
                        break
                    
                    elif userFullGuess == 'n':
                        
                        break
                    
                    else:
                        
                        raise Exception('Only y or n!')
                    
                except KeyboardInterrupt:
                            
                            print('\nDo not interrupt me!')
                        
                except Exception as e:
                    
                    print(e)
            
            try:
    
                time.sleep(1)
        
            except KeyboardInterrupt:
        
                print("\nDon't interrupt me!\n")
            
            if userFullGuess == 'y':
                
                while True:
                    
                    try:
                
                        fullWord = input('\nEnter your full word guess: ').lower() #Asks for their guess
                        
                        if fullWord.isalpha() == False:
                            
                            raise Exception('Only letters!')
                        
                        break
                    
                    except KeyboardInterrupt:
                        
                        print('\nDo not interrupt me!')
                    
                    except Exception as e:
                        
                        print(e)
                
                try:
    
                    time.sleep(1)
        
                except KeyboardInterrupt:
        
                    print("\nDon't interrupt me!\n")
                
                if fullWord == ''.join(hangmanWord):
                    
                    print('\nYou correctly guessed the word! Congratulations!') #If they guess the word correctly the game ends
                    
                    break
                
                else:
                    
                    print('That wasn\'t right') #If they guess the word incorrectly the game continues
                    
                    incorrectGuesses += 1
                    
                    try:
    
                        time.sleep(1)
        
                    except KeyboardInterrupt:
        
                        print("\nDon't interrupt me!\n")
                    
                    print('Number of incorrect guesses:',incorrectGuesses)
                    
                    print(hangmanImage(incorrectGuesses))
                    
                    pass
            
            elif userFullGuess == 'n':
                
                pass
        
        if ''.join(keyWord) == ''.join(hangmanWord): #If the user guesses all the letters correctly, they win and the game ends
                
                try:
    
                    time.sleep(1)
        
                except KeyboardInterrupt:
        
                    print("\nDon't interrupt me!\n")
                
                print('\nYou correctly guessed the word! Congratulations!')
                
                break
            
    if incorrectGuesses >= 6: #Only runs when user fails
        
        print("\nYou Lose!\nThe correct word was:",''.join(hangmanWord)) #Shows word
        
    while True:
        
            try:
            
                userContinue = input('\nWould you like to play again? (y/n): ').lower() #Asks user whether they want to continue playing
                
                if userContinue == 'y':
                    
                    break
                
                elif userContinue == 'n':
                    
                    break
                
                else:
                    
                    raise Exception('Only y or n!')
                
            except KeyboardInterrupt:
                        
                        print('\nDo not interrupt me!')
                    
            except Exception as e:
                
                print(e)
    
    if userContinue == 'y':
        
        continue
    
    else:
        
        break

#Ending Screen
print('\nThank You For Playing!')

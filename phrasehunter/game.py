import random
from phrasehunter.phrase import Phrase


# Create your Game class logic in here.
class Game:
    def __init__ (self):
        self.lives = 5
        self.phrases = [
            Phrase("Truth always reveals itself"),
            Phrase("Learning to code is challenging"),
            Phrase("My brain is melting"),
            Phrase("I should have been a computer science major"),
            Phrase("You live and you learn")
        ]
        self.active_phrase = random.choice(self.phrases)
        self.guesses = [" "]


    def welcome(self):
        print("""
        ***********************************************
        Welcome to the Phrase Hunter Guessing Game!!!!!
        ***********************************************
        """)


    def start(self):    
        while self.lives > 0 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"Lives remaining: {self.lives}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.check_guess(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.lives -= 1
            if self.lives > 0 and self.active_phrase.check_complete(self.guesses) == True:
                print("Congratulations! You won!!\n")
                self.play_more()
            elif self.lives == 0 and self.active_phrase.check_complete(self.guesses) == False:
                print('Game over, BREAUX! You LOST!!!\n')
                self.play_more()


    def get_guess(self):
        while True:
            try:
                user_guess = input("Guess a letter in the phrase!: ").lower()
                if not user_guess.isalpha() or len(user_guess) != 1:
                    raise ValueError
                return user_guess
            except ValueError:
                print('\nNot a valid entry, try again Breaux-ham-megeline\n')
                self.lives -= 1
                print(f"Lives remaining: {self.lives}")
                self.active_phrase.display(self.guesses)
                if self.lives == 0 and self.active_phrase.check_complete(self.guesses) == False:
                    print('Game over, BREAUX! You LOST!!!\n')
                    break
        self.play_more()
                    
    def play_more(self):
        while True:
            try:
                play_again = input("Would you like to play again? (Y)es or (N)o: ").lower()
                if play_again == 'y':
                    self.reset()
                elif play_again == 'n':
                    print("\nThanks for playin', Breaux-HAM\n")
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Not a valid entry, TRY AGAIN")

                
    def reset(self):
        self.guesses.clear()                    
        self.active_phrase = random.choice(self.phrases)
        self.lives = 5
        self.guesses = [" "]
        print("""\n
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        Welcome BACK to the greatest PHRASE HUNTER game of all time!
        ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        \n""")
        self.start()
    





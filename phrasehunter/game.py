import random
from phrasehunter.phrase import Phrase


# Create your Game class logic in here.
class Game:
    def __init__ (self):
        self.missed = 0
        self.phrases = [
            Phrase("Obesity is the leading cause of covid deaths in america"),
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
        self.welcome()
        while self.missed < 5 and self.active_phrase.check_complete(self.guesses) == False:
            print(f"Number missed: {self.missed}")
            self.active_phrase.display(self.guesses)
            user_guess = self.get_guess()
            self.guesses.append(user_guess)
            self.active_phrase.check_guess(user_guess)
            if not self.active_phrase.check_guess(user_guess):
                self.missed += 1
        self.game_over()
            
        
    
    def get_guess(self):
        user_guess = input("Guess a letter in the phrase!")
        return user_guess

    def game_over(self):
        if self.missed == 5:
            print("OOPS! Looks like you lost, BREAUX!")
        else:
            print("Congratulations! You won!!")




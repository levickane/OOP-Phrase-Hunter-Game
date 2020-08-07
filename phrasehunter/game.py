import random
from phrasehunter.phrase import Phrase


# Create your Game class logic in here.
class Game:
    def __init__ (self):
        self.lives = 5
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
                play_again = input("Would you like to play again? (Y)es or (N)o: ").lower()
                if play_again == 'y':
                    self.guesses.clear()
                    self.active_phrase = random.choice(self.phrases)
                    self.lives = 5
                    print("\nWelcome back to the greatet PHRASE HUNTER game of all time!\n")
                    continue
                else:
                    print("\nThanks for playin', Breaux-ham\n")
                break

            elif self.lives == 0 and self.active_phrase.check_complete(self.guesses) == False:
                print('Game over, BREAUX! You LOST!!!\n')
                play_again = input("Would you like to play again? (Y)es or (N)o: ").lower()
                if play_again == 'y':
                    self.guesses.clear()                    
                    self.active_phrase = random.choice(self.phrases)
                    self.lives = 5
                    print("\nWelcome back to the greatest PHRASE HUNTER game of all time!\n")
                    continue
                else:
                    print("\nThanks for playin', Breaux-ham\n")
                break

        
            

    def get_guess(self):
        user_guess = input("Guess a letter in the phrase!: ").lower()
        return user_guess


    def game_over(self):
        if self.lives == 0:
            print("OOPS! Looks like you lost, BREAUX!")
        else:
            print("Congratulations! You won!!")




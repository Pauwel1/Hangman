
import random

class Hangman:
    def __init__(self):
        self.display = ""
        
    @property
    def possible_words(self):
        """The words that can be selected for the game"""
        list_of_words = ["becode", "learning", "mathematics", "sessions"]
        return list_of_words

    @property
    def word_to_find(self):
        """Seperate letters of a randomly selected word from the list"""
        random_word = random.choice(self.possible_words)
        return random_word
        
    
    def start_game(self):
        """
        - The correctly guessed letters replace the underscore in the displayed quiz
        - The guessed letters are shown below
        - Counters are adapted (turns, letters, errors, lives)
        """
        word = self.word_to_find
        correctly_guessed_letters = "_" * len(word)
        complete = False
        wrongly_guessed_letters = []
        guessed_letters = [wrongly_guessed_letters]
        lives_left = 5
        turn_count = 0
        error_count = 0
        print(correctly_guessed_letters)
        while complete == False and lives_left > 0:
            guess = input("Guess a letter (one letter only): ").lower()
            turn_count += 1
            if len(guess) != 1 or guess == int:
                print("Only a single letter is allowed.")
            elif len(guess) == 1 and guess.isalpha():
                if guess in guessed_letters:
                    print("Letter has already been used.")
                elif guess not in word:
                    print("This letter does not appear in the word.")
                    lives_left -= 1
                    error_count += 1
                    wrongly_guessed_letters.append(guess)
                elif guess in word:
                    print("Yes! Correct!")
                    guessed_letters.append(guess)
                    new_display = list(correctly_guessed_letters)
                    letters = [i for i, letter in enumerate(word) if letter == guess]
                    for letter in letters:
                        new_display[letter] = guess
                        correctly_guessed_letters = "".join(new_display)
                    if "_" not in correctly_guessed_letters:
                        complete = True
                        print(f"Well played! The word was {word}!" \
                              f" You found it in {turn_count} turns and made {error_count} errors")
            print(correctly_guessed_letters)
            print(f"You have already tried: {wrongly_guessed_letters}")
            print(f"You have {lives_left} lives left!")
            print(f"Turns: {turn_count}")
            print(f"Mistakes made: {error_count}")
        if lives_left == 0:
            print(f"Game over... The word was {word}.")
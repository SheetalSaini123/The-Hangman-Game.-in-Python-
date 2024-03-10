import random

class Hangman:
    def __init__(self, words):
        self.words = words
        self.word = random.choice(words)
        self.hidden_word = ['_'] * len(self.word)
        self.attempts_left = 6
        self.guessed_letters = []

    def display_word(self):
        return ' '.join(self.hidden_word)

    def display_hangman(self):
        stages = [
            """
             _______
            |       |
            |       O
            |      /|\\
            |       |
            |      / \\
            -
            """,
            """
             _______
            |       |
            |       O
            |      /|\\
            |       |
            |      /
            -
            """,
            """
             _______
            |       |
            |       O
            |      /|\\
            |       |
            |
            -
            """,
            """
             _______
            |       |
            |       O
            |      /|
            |       |
            |
            -
            """,
            """
             _______
            |       |
            |       O
            |       |
            |       |
            |
            -
            """,
            """
             _______
            |       |
            |       O
            |
            |
            |
            -
            """,
            """
             _______
            |       |
            |
            |
            |
            |
            -
            """
        ]
        return stages[self.attempts_left]

    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            print("You already guessed this letter.")
            return

        self.guessed_letters.append(letter)
        
        if letter in self.word:
            for i in range(len(self.word)):
                if self.word[i] == letter:
                    self.hidden_word[i] = letter
            print("Correct guess!")
        else:
            self.attempts_left -= 1
            print("Incorrect guess!")
        
        print("Attempts left:", self.attempts_left)
        print("Current word:", self.display_word())
        print(self.display_hangman())

    def is_game_over(self):
        if '_' not in self.hidden_word:
            print("Congratulations🎉🎉! You guessed the word:", self.word)
            return True
        elif self.attempts_left <= 0:
            print("Game over🙁! You ran out of attempts. The word was:", self.word)
            return True
        return False

# Predefined list of words
words = ["hangman", "python", "programming", "computer", "game","ice","goggle","parents","brother","pizz"]

# Create an instance of Hangman game using constructor function
hangman_game = Hangman(words)

print("Welcome to Hangman Game🥰🥰!")
print("Guess the word:", hangman_game.display_word())

# Main game loop
while not hangman_game.is_game_over():
    guess = input("Guess a letter: ").lower()
    hangman_game.guess_letter(guess)

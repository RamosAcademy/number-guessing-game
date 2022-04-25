"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------


[X] Make sure your script runs without errors. Catch exceptions and report errors to the user in a meaningful way.
[X] As a player of the game, I should see a some kind of text header, welcome or game intro message.
[X] A random number should be chosen that is within the range.
[X] As a player of the game, I should be continuously prompted for a guess until I get it right.
[X] As a player of the game, my guess should be within the number range. If my guess is outside the guessing range I should be told to try again.
[X] As a player of the game, after an incorrect guess I should be told if my answer is higher or lower than the answer, so that I can narrow down my guesses.
[X] As a player of the game, after the game ends I should be shown my number of attempts at guessing.
[X] As a player of the game, after I guess correctly I should be prompted if I would like to play again.
[X] As a player of the game, at the start of each game I should be shown the current high score (least amount of points) so that I know what I am supposed to beat.
[X] Every time a player decides to play again, the random number to guess is updated so players are guessing something new each time.
[X] When the game ends, an ending message is shown to the player.


"""

from random import randrange

WELCOME_MESSAGE = "Hello, beautiful person! Welcome to the Guessing Game!"
HIGH_OF_RANGE = 10
high_score = 0


# sauce: https://gist.github.com/garrettdreyfus/8153571
def yes_or_no(prompt: str):
    reply = str(input(prompt)).lower().strip()
    if reply[0] == 'y':
        return True
    if reply[0] == 'n':
        return False
    else:
        return yes_or_no("Please choose 'y' for Yes or 'n' for No --> ")


def set_high_score(old_score: int, attempts: int) -> int:
    new_score = HIGH_OF_RANGE - (attempts - 1)
    if old_score >= new_score:
        return old_score
    else:
        return new_score


def start_game(score: int):
    """INITIALIZATION"""
    attempts = 0
    user_guess = False
    number_message = f"Guess an integer between 1 and {HIGH_OF_RANGE} --> "
    error_message = f"Oops! I only understand whole numbers between 1 and {HIGH_OF_RANGE}\n" \
                    f"Don't worry, typos aren't counted against you :)"

    """1. Display an intro/welcome message to the player."""
    if score == 0:
        print(WELCOME_MESSAGE)
    else:
        print(f"Welcome back! Current high score is: ", score)

    """2. Store a random number as the answer/solution."""
    number = randrange(HIGH_OF_RANGE) + 1

    """3. Continuously prompt the player for a guess."""
    while user_guess != number:

        try:
            user_guess = int(input(number_message))
            if user_guess < 1 or user_guess > HIGH_OF_RANGE:
                raise ValueError(error_message)
        except ValueError:
            print(error_message)
        else:

            attempts += 1

            if user_guess == number:
                print("Congrats! You got it")  # 4. Once the guess is correct, stop looping, inform the user they "Got it"
                new_high_score = set_high_score(score, attempts)
                print("HIGH SCORE: ", new_high_score)
                print("Number of attempts: ", attempts)  # and show how many attempts it took them to get the correct number

                new_game = yes_or_no("Would you like to play again? (Y/N) ")
                if new_game:
                    start_game(new_high_score)
                else:
                    """ 5. Let the player know the game is ending, or something that indicates the game is over. """
                    print("HIGH SCORE: ", new_high_score)
                    print("Thanks for playing, see you soon!")
            elif user_guess < number:  # 3.b. If the guess is less than the solution, display to the player "It's higher".
                number_message = "Try guessing higher --> "
            elif user_guess > number:  # 3.a. If the guess greater than the solution, display to the player "It's lower".
                number_message = "Try guessing lower --> "
            else:
                print("Sorry, try another number!")


# Kick off the program by calling the start_game function.
start_game(high_score)

from random import randint
from time import time

line = "*" * 70


def main() -> None:
    intro()
    number_of_digits = how_many_digits()

    total_rounds, total_points, total_time, total_attempts = 0, 0, 0, 0
    active = True

    while active:
        round_points, round_time, round_attempts = game_round(number_of_digits)
        total_rounds += 1
        total_points += round_points
        total_time += round_time
        total_attempts += round_attempts
        active = another_round()

    game_statistics(total_points, total_time, total_attempts, total_rounds)


def intro() -> None:
    """Welcomes user and prints the rules"""
    print(line)
    print("Welcome to Bulls and Cows!".upper())
    print("Try to guess a random number I'm thinking of!")
    print(line)
    print("RULES:")
    print("If you guess the right digit and its position, you get 1 bull.")
    print("If you guess only the digit but not its position, you get 1 cow.")


def how_many_digits() -> int():
    """Asks user how long should be in the secret number"""
    print(line)
    print("How long numbers would you like to guess?")
    dig = 0
    while dig not in range(1, 10):
        try:
            dig = int(input("Enter a number of digits (1-9): "))
        except ValueError:
            print("Invalid input! Please enter only numbers.")
    return dig


def game_round(num_of_digits: int):
    """Performs 1 round - user is guessing 1 random number"""
    secret_number = generate_number(num_of_digits)
    # print(f"Secret number: {secret_number}")
    attempts = 0
    start_time = time()
    while True:
        give_up, user_tip = get_user_tip(num_of_digits)
        if give_up:
            r_time = time() - start_time
            points = 0
            print_looser_info(attempts, r_time, secret_number)
            break
        attempts += 1
        if user_tip == secret_number:
            r_time = time() - start_time
            points = 1
            print_winner_info(attempts, r_time)
            break
        else:
            check_bulls_cows(user_tip, secret_number)

    return points, r_time, attempts


def generate_number(num_of_digits: int) -> str():
    """Returns a random number with specified number of digits"""
    list_of_digits = []
    while len(list_of_digits) < num_of_digits:
        new_digit = str(randint(0, 9))
        if new_digit not in list_of_digits:
            list_of_digits.append(new_digit)
    number = ''.join(list_of_digits)
    print(line)
    print(f"I'm thinking of a secret {num_of_digits}-digit number...")
    return number


def get_user_tip(num_of_digits: int):
    """Asks user for a tip with a correct number of digits"""
    while True:
        tip = (input("\tEnter a number (or 'gu' to give up): "))
        if tip.lower() == 'gu':
            return True, None
        elif tip.isdigit() and (len(tip) == num_of_digits):
            return False, tip
        else:
            print(f"\t\tPlease enter a NUMBER with {num_of_digits} digits!")


def check_bulls_cows(tip: str, number: str) -> None:
    """Checks user's tip and prints number of bulls and cows"""
    bulls = 0
    cows = 0
    for digit in tip:
        if digit in number and (tip.index(digit) == number.index(digit)):
            bulls += 1
        elif digit in number:
            cows += 1
    if bulls == 1:
        print(f"\t\tYou have got {bulls} bull ", end='')
    else:
        print(f"\t\tYou have got {bulls} bulls ", end='')
    if cows == 1:
        print(f"and {cows} cow. Go on!")
    else:
        print(f"and {cows} cows. Go on!")


def print_looser_info(at: int, t: float, num: str) -> None:
    """Prints looser info, correct number and round statistics"""
    print(line)
    print(f"SORRY! The secret number was {num}!")
    print(f"\tAttempts: {at}")
    print(f"\tTime: {int(t)} seconds")


def print_winner_info(at: int, t: float) -> None:
    """Prints winner info and round statistics"""
    print(line)
    print("CORRECT! You have guessed the right number!")
    print(f"\tAttempts: {at}")
    print(f"\tTime: {int(t)} seconds")


def another_round() -> bool():
    """Asks user if he wants to play another round and returns True/False"""
    answer = (input("Would you like to continue with another number? (Yes/No): "))
    return answer.lower() == 'yes'


def game_statistics(t_points: int, t_time: float, t_attempts: int, t_rounds: int) -> None:
    """Prints statistics for all rounds"""
    print(line)
    print("FINAL STATISTICS")
    print(f"\tYou have guessed {t_points} numbers of {t_rounds}!")
    print(f"\tTotal number of attempts: {t_attempts}")
    print(f"\tTotal time: {int(t_time/60)} min {int(t_time%60)} s")
    print(line)


main()
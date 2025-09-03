# Exercise 0: Example
def print_greeting():
    python_is_fun = True
    if python_is_fun:
        print("Python is fun!")

print_greeting()


# Exercise 1: Vowel or Consonant
def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ").lower()

    if len(letter) != 1 or not letter.isalpha():
        print("Invalid input. Please enter a single letter.")
        return

    vowels = "aeiou"
    if letter in vowels:
        print(f"The letter {letter} is a vowel.")
    else:
        print(f"The letter {letter} is a consonant.")

check_letter()


# Exercise 2: Old enough to vote?
def check_voting_eligibility():
    try:
        age = int(input("Please enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        else:
            voting_age = 18
            if age >= voting_age:
                print("You are eligible to vote!")
            else:
                print("You are not eligible to vote yet.")
    except ValueError:
        print("Invalid input. Please enter a number.")

check_voting_eligibility()


# Exercise 3: Calculate Dog Years
def calculate_dog_years():
    try:
        dog_age = int(input("Input a dog's age: "))
        if dog_age < 0:
            print("Age cannot be negative.")
            return

        if dog_age <= 2:
            dog_years = dog_age * 10
        else:
            dog_years = 20 + (dog_age - 2) * 7

        print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a number.")

calculate_dog_years()


# Exercise 4: Weather Advice
def weather_advice():
    cold = input("Is it cold? (yes/no): ").lower()
    raining = input("Is it raining? (yes/no): ").lower()

    if cold == "yes" and raining == "yes":
        print("Wear a waterproof coat.")
    elif cold == "yes" and raining == "no":
        print("Wear a warm coat.")
    elif cold == "no" and raining == "yes":
        print("Carry an umbrella.")
    elif cold == "no" and raining == "no":
        print("Wear light clothing.")
    else:
        print("Invalid input. Please answer with yes or no.")

weather_advice()


# Exercise 5: What's the Season?
def determine_season():
    month = input("Enter the month of the year (Jan - Dec): ").capitalize()
    try:
        day = int(input("Enter the day of the month: "))
    except ValueError:
        print("Invalid day. Please enter a number.")
        return

    if month not in ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]:
        print("Invalid month entered.")
        return

    season = ""
    if (month == "Dec" and day >= 21) or month in ["Jan","Feb"] or (month == "Mar" and day <= 19):
        season = "Winter"
    elif (month == "Mar" and day >= 20) or month in ["Apr","May"] or (month == "Jun" and day <= 20):
        season = "Spring"
    elif (month == "Jun" and day >= 21) or month in ["Jul","Aug"] or (month == "Sep" and day <= 21):
        season = "Summer"
    elif (month == "Sep" and day >= 22) or month in ["Oct","Nov"] or (month == "Dec" and day <= 20):
        season = "Fall"

    print(f"{month} {day} is in {season}.")

determine_season()


# Exercise 6: Number Guessing Game (Challenge)
import random
def guess_the_number():
    number = random.randint(1, 10)
    guess = None

    while guess != number:
        try:
            guess = int(input("Guess a number between 1 and 10: "))
            if guess < number:
                print("Too low! Try again.")
            elif guess > number:
                print("Too high! Try again.")
            else:
                print("Congratulations! You guessed it!")
        except ValueError:
            print("Invalid input. Please enter a number.")

guess_the_number()

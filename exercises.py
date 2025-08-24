# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.

def check_letter():
    check_letter = input('enter a letter (a-z or A-Z): ').lower()
    if check_letter == 'a' or check_letter == 'e'or check_letter == 'i' or check_letter == 'o' or check_letter == 'u':
        print(f'the letter {check_letter} is a vowel')
    else:
        print(f'the letter {check_letter} is a constsnt')

# Call the function
check_letter()


# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.

def check_voting_eligibility():
    age = int(input('enter your age: '))
    if age >= 21:
        print('you are eligible to vote')
    elif age <= 20 and age > 0:
        print('you are not eligible to vote')
    else:
        print('enter a valid age')
        
# Call the function
check_voting_eligibility()


# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.

def calculate_dog_years():
    dog_age = int(input('enter the dogs age: '))
    
    if dog_age <= 2:
        age = dog_age * 10
        print(f'dogs age: {age}')
    else:
        age = (2 * 10) + ((dog_age-2)*7)
        print(f'dogs age: {age}')

# Call the function
calculate_dog_years()


# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.

def weather_advice():
    weather = input('enter if it is cold (yes/no)?').lower()
    raining = input('is it raining (yes/no)?').lower()
    
    if weather == 'yes' and raining == 'yes':
        print('Wear a waterproof coat.')
    elif weather == 'yes' and  raining == 'no':
        print('Wear a warm coat.')
    elif raining == 'yes' and  weather  == 'no':
         print('Carry an umbrella.')
    elif raining and weather  == 'no':
        print('Wear light clothing.')
    else:
        print('invalid input')

# Call the function
weather_advice()




# Write a Python script named `fizz_buzz` that prints numbers from 1 to 50, but:
# - For multiples of 3, print "Fizz" instead of the number.
# - For multiples of 5, print "Buzz" instead of the number.
# - For multiples of BOTH 3 and 5, print "FizzBuzz".
#
# Requirements:
# - Use a loop to iterate through numbers from 1 to 50.
# - Use conditional statements to check divisibility.
# - Print each result on a new line.
#
# Hints:
# - Use the modulo operator `%` to check if a number is divisible by another.
# - Check for multiples of BOTH 3 and 5 first to avoid missing them.
#
def fizz_buzz():
    for i in range(1,50):
        if i %3 == 0 and not i %5 == 0:
            print('fizz')
        elif i %5 == 0 and not i %3 == 0:
            print('buzz')
        elif i %3 == 0 and i %5 == 0:
            print('fizz-buzz')

# Call the function
fizz_buzz()

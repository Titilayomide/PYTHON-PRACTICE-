#LESSON 1 DAY 1 - PRINTING
print('A "single quote" inside a double quote')
print('A "double quote" inside a single quote')
print("Alternatively you can just \"escape\" the quote")


#LESSON 2 DAY 1 - DEBUGGING PRACTICE

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')

# Answer part 3. Extra indentation removed
#   print('e.g. print("Hello " + "world")')
print('e.g. print("Hello " + "world")')

SOLUTION TO LESSON 2
# print(Day 1 - String Manipulation")
print("Day 1 - String Manipulation")

# Answer part 2. Outer double quotes changed to single quotes.
# print("String Concatenation is done with the "+" sign.")
print('String Concatenation is done with the "+" sign.')

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')

# Answer part 3. Extra indentation removed
#   print('e.g. print("Hello " + "world")')
print('e.g. print("Hello " + "world")')

print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')

# Answer part 4. Extra ( in print function removed.
# print(("New lines can be created with a backslash and n.")
print("New lines can be created with a backslash and n.")


LESSON 3 DAY 1 - INPUT FUNCTION
Demo
Without changing the code, try clicking submit.
If a student didn't complete the coding exercise, then the extra tests should catch this.
For example in this case 6 is the correct answer for the visible inputs. But behind the scenes when you submit the code we are also passing in 5 and 5.
5 x 5 = 25
while
2 x 3 = 6
So the only way for the student to pass all the tests in the evaluation is to write the correct code.
This is how we ensure you're doing the right things and test your understanding of the programming concepts. It's like having a teacher next to you checking your code.

SOLUTION:
num1 = int(input())
num2 = int(input())

print(num1*num2)

LESSON 4 DAY 1 - VARIABLES
Instructions
This program takes two inputs. The first input is stored in a variable called a. The second input is stored in a variable called b.
Write a program that switches the values stored in the variables a and b.
Warning . You don't need to print anything. The print statement is already in the template code. However, your program should work for different inputs. e.g. any value of a and b.
Example Input 1
29
41
Example Output 1
a: 41
b: 29
Example Input 2
Hello
World
Example Output 2
a: World
b: Hello

SOLUTION:
# There are two variables, a and b from input
a = input()
b = input()
# 🚨 Don't change the code above ☝️
####################################
# Write your code below this line 👇
c = a
a = b
b = c

Day 1 Project: Band Name Generator
#1. Create a greeting for your program.
print("welcome beautiful, to band name generator")

#2. Ask the user for the city that they grew up in.
name_of_city = input("what city did you grow up in?")

#3. Ask the user for the name of a pet.
pet = input("what's your pet's name?")
#4. Combine the name of their city and pet and show them their band name.
print("your band name is" + " " + name_of_city + pet)

#5. Make sure the input cursor shows on a new line:

# Solution: https://replit.com/@appbrewery/band-name-generator-end

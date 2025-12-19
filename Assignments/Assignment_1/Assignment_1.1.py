#Variables and Input
# Create a variable my_age and assign your age to it. Print a message using this variable.
my_age=20
print("My age is ",my_age)

# Ask the user to enter their favorite food and print a message incorporating this input.
favorite_food = input("Enter your favorite food: ")
print(f"{favorite_food} is very popular!")


#Type conversion
# 1.Convert the string "42" to an integer and print the result.
num = int("42")
print("Converted integer is:", num)

# 2.Convert the floating-point number 3.14159 to a string and print the result.
string_pi = str(3.14159)
print("Converted string is:", string_pi)


#Strings
# Concatenate the strings "Hello" and "World!" and print the result.
concat="Hello " + "world!!!!"
print(concat)

# Use string indexing to extract the third character from the string "Python".
string="Python"
print("Third character:", string[2])

# Take a sentence as input and print only the first five words.
sentence = input("Enter a sentence: ")
words = sentence.split()
first_five_words = ' '.join(words[:5])
print("First five words:", first_five_words)


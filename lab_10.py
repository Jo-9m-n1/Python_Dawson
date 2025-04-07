# Question 1
'''
Open your story file from class for reading.
(a) Print the story (only the story) for the user to read
(b) Count the total number of words in the story
(c) Count the frequency of each word in the story.  Then sort all the available words
    in the story according to their frequence from highest to lowest. Display the results.
'''

input_file = open('story.txt', 'r')
input_file_read = input_file.read()
input_file_contents = input_file_read.split()
d = {}
for i in input_file_contents:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)


# Question 2
'''
Make two files: cats.txt and dogs.txt.  Store at least three names of cats in the first
file and three names of dogs in the second file.  Write a program that tries to read
these files and print the contents of each file to the screen.  

(a) Wrap your code in a try-except block to catch the FileNotFoundError and print a 
    friendly message if a file is missing.  To test your code, move one of the files 
    to a different location on your system, and make sure that the code in the except 
    block executes properly.  
(b) Modify your previous code to fail silently if either file is missing
'''

# Question 3
'''
A common problem when prompting for numerical input occurs when providing text 
instead of numbers.  In such a case, when trying to convert the input to int, a
ValueError occurs.  Write a program that prompts the user for two numbers, add
them together and print the result.  Catch the ValueError if either input value is
not a number, and print a friendly error message.  Test your program by entering two
numbers and then by entering some text instead of a number.  
'''
try:
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    num1 = int(num1)
    num2 = int(num2)
    result = num1 + num2
    print(f"The result is: {result}")

except ValueError:
    print("Error: Please enter valid numbers.")

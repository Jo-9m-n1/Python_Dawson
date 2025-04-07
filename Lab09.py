# Question 1
'''
From your accounts.txt file (from last class) read each line and create 
a dictionary of dictionaries.  The outer dictionary key is the account 
number.  The inner dictionary key is the last name and the value in 
the inner dictionary is the balance.  Print the final dictionary.  
'''

output_file = open('accounts.txt', 'r')
d = {}
for line in output_file:
    account_number, name, balance = line.split()
    if account_number not in d:
        d[account_number] = {}
        d[account_number][name] = balance
    else:
        d[account_number][name] = balance
output_file.close()
print(d)
# Question 2
'''
(a) Open a file called grades.txt for writing that will hold student 
    grade information.  This information will be read from the user.  
    Each input line given by the user is of the form: 
    firstname, lastname, exam1grade, exam2grade, exam3grade.  
    Read grade information for 10 students and write that information 
    to your grades.txt file.  Make sure to close the file after 
    writing to it.  

(b) Once your grades.txt file is populated, read and store the infomration
    from the file. Determine what data structure (e.g. lists, dictionaries, 
    sets, etc.) would best suit for storing the data in the file.  Once 
    your data is stored, compute the following: 
    (i) the minimum, maximum and average of exam1grade, exam2grade, exame3grade
        for each student and print this information
    (ii) the minimum, maximum and average of exam1grade across all students.
         Do this for exam2grade and exam3grade as well.  
    (iii) the average of the average of all 3 exams for all students.  
'''

output_fie = open('grades.txt', 'w')
for i in range(10):
    grades = input('Enter student information: ')
    output_fie.write(grades + '\n')
output_fie.close()

output_fie = open('grades.txt', 'r')
new_dict = {}
exam1, exam2, exam3 = [], [], []
for line in output_fie:
    firstname, lastname, exam1grade, exam2grade, exam3grade = line.split()
    new_dict[firstname + ' ' + lastname] = [exam1grade, exam2grade, exam3grade]
    exam1.append(int(exam1grade))
    exam2.append(int(exam2grade))
    exam3.append(int(exam3grade))
output_fie.close() 

# Question 3
'''
Download into your folder the words.txt file on Lea.  You will notice that each
word in the words.txt file is on a new line.  
(a) Open a new file called words_updated.txt with writing mode, and write all the
    words from the words.txt file continuously one after the other only separated
    by a space.  Make sure that you strip all the white space after each word
    that you read from the words.txt file.  Once you are done, make sure you
    close all files that you had opened.  

(b) Create an integer num_words that will hold the number of words that you have
    in your words_updated.txt (or words.txt) file.  Now prompt the user to read
    an integer k (between 1 and 80) from the user.  Make sure to do input 
    validation so to be assured that the user abides the constraints on k.  

    Open a new file called result.txt with writing mode, and read the words 
    from your words_updated.txt file and write them in result.txt such that
    the number of characters on each line of result.txt is at most k (not
    counting the spaces between the words).  That is, if the next word 
    begin considered fits on the current line, add it to the current line
    (make sure to include a space between each pair of words on the line). 
    Otherwise, put this word on a new line (which will become the new
    current line).

    One you finish writing to your result.txt file, print the content of
    your file.  Make sure to close all files that you have opened.  
'''

words_file = open('words_updated.txt', 'r')
words = open('words.txt', 'w')
for line in words:
    words_file.write(line.strip() + ' ')
words_file.close()
words.close()

words_file = open('words_updated.txt', 'w')
num_words = len(words.readlines())
k = int(input('Enter an integer between 1 and 80: '))
words_updated = open('words_updated.txt', 'r')
result = open('result.txt', 'w')
while k < 1 or k > 80:
    print('Invalid input.')

'''
Consider cities and states in the US. Each state is giving two letter abbreviation. 
You are tasked to read n cities and states from the user and determine the number
of special pairs.
Here is an example of a special pair:
SCRATION PA and PARKERS SC.
This is a special pair since the first two characters of each city gives the abbreviation for
the other city's state. That is, SC PA and PA SC.
A pair of cities is speical if they meet this proeprty and are not in the same state. Your task is to determine the number 
of sepical pairs of cities in the efficient data structures.
INPUT SEPECIFICATION:
--> First line is an integer n (n is large), the number of cities.
--> Next n lines: one per city. Each line gives the name of a cite in uppercase, a space, and its state'e abbreviation in uppercase.
    Note that the same city name can exist in multiple states but will not appear moret han once in the same state.
OUTPUT SEPCEIFICATION:
Output the numbeer of speical pairs of cities.

Sample input:
12
SCRANTON PA
MANISTEE MI
NASHUA NH
PARKER SC
LAFAYETTE CO
WASHOUGAL WA
MIDDLEBOROUGH MA
MASDISON MI
MILFORD MA
MIDDLETON MA
COVINGTON LA
LAKEWOOD CO

Sample output:
9

Read 5 different sample inputs from the user and write this to a file.
an empty line between any two sample inputs
'''

n = int(input('Enter the number of cities: '))
d = {}
for i in range(n):
    city, state = input('Enter city and state: ').split()
    if state not in d:
        d[state] = []
    d[state].append(city)
print(len(d))
'''
What is the output of this code snippet?
'''

file = open("data.txt", "w")
file.write("Hello!\n")
file.write("I am a student in Dawson.\n")
file.close()

file = open("data.txt", "w")
file.write("I love science.\n")
file.close()

file = open("data.txt", "r")
content = file.read()
file.close()

print(content)

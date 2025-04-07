file_name = 'book.txt'
try:
    input_file = open('file_name', 'r')
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
    output_file = open(file_name, 'w')
else:
    for line in input_file:
        print(line.strip())

input_file = open('words.txt', 'r')
words_lst = input_file.readlines()
output_file.writelines(words_lst)
input_file.close()
output_file.close()
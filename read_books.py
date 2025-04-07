from urllib.request import urlopen

def readFileURLString(url):
    data = urlopen(url)
    html_data = data.read()
    encoding = data.headers.get_content_charset('utf-8')
    decoded_html = html_data.decode(encoding)
    return decoded_html

data_str = readFileURLString('https://short-story.me/stories/horror-stories/1844-photo-album-for-a-ghost')
print(data_str)

output_file = open('output.txt', 'w')
output_file.close()

input_file = open('Photo_Album_for_a_Ghost.txt', 'r')


'''
--> Pick 5 books
--> Read 4 of the 5 books
--> Write each of the books into a separate file, automate this process
    as much as possible
--> The 5th book title keep in mind, but don't read/write it

Using try-except block, to do the following:
--> Read the numeber of words of the story only
--> Find the frequence of each word in the file
--> Number of paragraphs
--> Number of sentences
--> Length of smallest and longest word, average length
--> Most common vowel
--> What is the average usage of puncation
'''
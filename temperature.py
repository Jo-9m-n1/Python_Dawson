# Jongmin Lee, 2432787

def toCelsius(F):
    celcius = (F - 32) * (5/9)
    return round(celcius, 2)

input_file = open('data.txt', 'r')
temp_dict = {}
for i in range(4):
    input_file.readline()
for line in input_file:
    one_line = (line.strip().split())
    year = int(one_line[0])
    value = one_line[1:]
    celcius = list(map(toCelsius, map(float, value)))
    temp_dict[year] = celcius

def avgTempYear(d, year):
    try:
        for i in d[year]:
            sum += i
            avg = sum/len(d[year])
            rounded_avg = round(avg, 2)
            return (rounded_avg)
    except:
          print('No data has been found for the selected year')

def topThreeYears(d):
    lst = []
    top3 = []
    for key in d:
        lst.append(avgTempYear(d, key))
    for i in range(3):
        maximum = max(lst)
        lst.pop(maximum)
        top3.append(maximum)

def avgTempMonth(d):
    month_dict = {}
    lst = []
    top3 = []
    for key, element in d.items():
        for i in range(len(element)):
            month_dict[i+1] = element[i]
    for key, element in month_dict.items():
        lst.append(element)
    for i in range(3):
        maximum = max(lst)
        lst.pop(maximum)
        top3.append(maximum)

def belowFreezing(d):
    below = []
    for key, element in d.items():
        for i in range(len(element)):
            if element[i] < 0:
                below.append((key, i+1))
    return below

output_file = open('data_celsius.txt', 'w')
input_file.close()
input_file = open('data.txt', 'r')
for i in range(4):
    line = input_file.readline()
    output_file.write(line)

for key, value in temp_dict.items():
    output_file.write(str(key) + '   ' + '  \t'.join(map(str, value)) + '\n')

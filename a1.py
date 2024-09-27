L = input('Enter your number of the completed Lab: ')
Q = input('Enter your number of the quizzes completed: ')
A1 = input('Enter your first grade of the assignment: ')
A2 = input('Enter your second grade of the assignment: ')
A3 = input('Enter your third grade of the assignment: ')
A4 = input('Enter your fourth grade of the assignment: ')
M1 = input('Enter your first grade of the Mid-term: ')
M2 = input('Enter your second grade of the Mid-term: ')
FI = input('Enter your grade of the Final: ')
MF = input('Enter your grade of the Mid-term & Final Preparation: ')

if int(L) >= int(6):
    L_G = int(100)
else:
    L_G = int((int(L) / 6) * 100)
    
if int(Q) >= int(6):
    Q_G = int(100)
else:
	Q_G = int((int(Q) / 6) * 100)

print('Your grade is: ', int((int(L_G)) * 0.20) + (int(Q_G) * 0.15) + ((((float(A1) + float(A2) + float(A3) + float(A4)) / 4) * 0.16) + (((float(M1) + float(M2)) / 2) * 0.25) + ((float(FI)) * 0.18) + ((float(MF)) * 0.06)))

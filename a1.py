Lab = input ('Enter your number of the completed Lab: ')
Quiz = input ('Enter your number of the quizzes completed: ')
As_1 = input ('Enter your first grade of the assignment: ')
As_2 = input ('Enter your second grade of the assignment: ')
As_3 = input ('Enter your third grade of the assignment: ')
As_4 = input ('Enter your fourth grade of the assignment: ')
MT_1 = input ('Enter your first grade of the Mid-term: ')
MT_2 = input ('Enter your second grade of the Mid-term: ')
FI = input ('Enter your grade of the Final: ')
MF = input ('Enter your grade of the Mid-term & Final Preparation: ')
print ('Your grade is: ', (int((((int(Lab)) / 6) *100) * 0.20) + (((int(Quiz) / 6) * 100) * 0.15) + ((((int(As_1) + int(As_2) + int(As_3) + int(As_4)) / 4) * 0.16) + (((int(MT_1) + int(MT_2)) / 2) * 0.25) + ((int(FI)) * 0.18) + ((int(MF)) * 0.06))))





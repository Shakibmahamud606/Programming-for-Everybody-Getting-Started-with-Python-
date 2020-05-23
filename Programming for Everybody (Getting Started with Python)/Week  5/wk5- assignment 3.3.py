


# 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the score is out of range, print an error. If the score is between 0.0 and 1.0, print a grade using the following table:
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# If the user enters a value out of range, print a suitable error message and exit. For the test, enter a score of 0.85.




score = input("Enter Score: ")
try:
    score=float(score)

except:
    print('Give a number between 0 to 1')
    quit()

if score>=.9 and score<=1:
    print('A')
elif score>=.8 and score<.9:
    print('B')
elif score>=.7 and score<.8:
    print('C')
elif score>=.6 and score<.7:
    print('D')
elif score>=0 and score<.6:
    print('F')
else:
    print("Error!")

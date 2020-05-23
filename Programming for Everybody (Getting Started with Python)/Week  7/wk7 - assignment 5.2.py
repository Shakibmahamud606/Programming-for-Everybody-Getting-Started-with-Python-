# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#  Enter 7, 2, bob, 10, and 4 and match the output below.





lg = 0
sm = 0
while True:
    num = input("Enter a number: ")
    if num == 'done':
      break
    try:
        num = int(num)
    except:
        print ("Invalid input")
        continue
    if lg == 0 and sm==0:
        lg = num
        sm = num
    elif lg < num:
        lg = num
    elif sm > num:
        sm = num


print ("Maximum is", lg)
print ("Minimum is", sm)

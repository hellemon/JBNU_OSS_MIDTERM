# Program make a simple calculator
import Calculation as c
import sys
import os.path 
import datetime

date_time_now = datetime.datetime.now()
# make error_log object

if os.path.isfile("cal_log.txt"):
    cal_log = open('cal_log.txt', 'a')
else:
    cal_log = open('cal_log.txt', 'w')
if os.path.isfile('error_log.txt'):
    error_log = open('error_log.txt', 'a')
else:
    error_log = open('error_log.txt', 'w')

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide") 

while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '4' and num2 == 0:
            print("Don't put a zero in the denominator")
            print("{}\nDon't put a zero in the denominator user input num1 = {}, num2 = {} ".format(date_time_now,num1, num2), file=error_log)
            continue
        c.choice_cal(choice, num1, num2)

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = ""
        True_exit = ""
        while True:
            next_calculation = input("Let's do next calculation? (yes/no): ")
            # Change to Lowercase to Troubleshoot
            next_calculation = next_calculation.lower()
            if next_calculation == "no":
                while True:
                    True_exit = input("Are you sure? (yes/no): ")
                    True_exit = True_exit.lower()
                    if True_exit == "yes":
                        break
                    elif True_exit == "no":
                        break
                    else:
                        continue                   
                break
            elif next_calculation == "yes":
                break
            else:
                continue

        if True_exit == "yes" and next_calculation == "no":
            break
            

    else:
        print("Invalid Input")
        print("{}Invalid Input user input num1 = {}, num2 = {}".format(date_time_now, num1, num2))

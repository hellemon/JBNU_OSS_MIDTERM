import os
import datetime

date_time_now = datetime.datetime.now()

if os.path.isfile("cal_log.txt"):
    cal_log = open('cal_log.txt', 'a')
else:
    cal_log = open('cal_log.txt', 'w')

# This function adds two numbers
def add(x, y):
    return x + y

# This function subtracts two numbers
def subtract(x, y):
    return x - y

# This function multiplies two numbers
def multiply(x, y):
    return x * y

#Need to define divide function.
def divide (x,y):
    return x/y

def choice_cal(choice, num1, num2):
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
        print(str(date_time_now),"\n"+"add_function" , num1, "+", num2, "=", add(num1, num2), file = cal_log)

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
        print(str(date_time_now),"\n"+"subtract_function", num1, "-", num2, "=", subtract(num1, num2), file = cal_log)

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
        print(str(date_time_now),"\n"+"multiply_function", num1, "*", num2, "=", multiply(num1, num2), file = cal_log)
            
    elif choice =='4':
        print(num1, "/", num2, "=", divide(num1,num2))
        print(str(date_time_now),"\n"+"divide_function", num1, "/", num2, "=", divide(num1,num2), file = cal_log)
            
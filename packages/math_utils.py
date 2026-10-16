from datetime import datetime
import time
import math
import random
from uuid import uuid4
import string

def date_time_operation():
     while True:
        print()
        print("--- Datetime and Time Operations --- ")
        print()
        print("1. Display current date and time")
        print("2. Calculate difference between two dates / times")
        print("3. Format date and time")
        print("4. Stopwatch")
        print("5. Countdown timer")
        print("6. Back to main menu")
        print()
        choice = int(input("Enter your choice (1-6): "))
        print()

        if choice == 1:
            current_time = datetime.now()
            print(f"Current date and time: {current_time}")

        elif choice == 2:
            date1 = input("Enter the first date (YYYY-MM-DD): ")
            date2 = input("Enter the second date (YYYY-MM-DD): ")

            d1 = datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.strptime(date2, "%Y-%m-%d")
            gap = abs(d1 - d2)
            print("Difference between the two dates:", gap)

        elif choice == 3:
            current_date_time = datetime.now()
            print("Select an option: ")
            print("1. For date")
            print("2. For time")
            print("3. For Both")
            print()
            choice = int(input("Enter your choice (1-3): "))
            print()

            if choice == 1:
                print(current_date_time.strftime("%Y/%m/%d"))
            elif choice == 2:
                print(current_date_time.strftime("%H:%M:%S"))
            elif choice == 3:
                print(current_date_time)
            else:
                print("Invalid Input")

        elif choice == 4:
            start_time = time.time()
            stop = input("\nPress Enter to Stop")
            stop_time = time.time()

            print(f"Your time is: {stop_time - start_time} seconds")

        elif choice == 5:
            n = int(input("Enter the countdown time in seconds: "))
            print()
            while n > 0:
                print(n)
                time.sleep(1)
                n = n - 1

            print("Countdown finished!")

        elif choice == 6:
            print()
            break


def maths_operation():
    while True:
        print()
        print("--- Mathematical operation ---")
        print()
        print("1. Calculating Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area og Geometric Shapes")
        print("5. Back to main menu")
        print()
        choice = int(input("Enter your choice: "))
       

        if choice == 1:
            num = int(input("Enter a number for calculating factorial: "))
            fact = math.factorial(num)
            print(f"Factorial of {num} is {fact}.")
           
        elif choice == 2:
            money = int(input("\nEnter principal amount: "))
            rate = int(input("Enter rate of interest (in %): "))
            year = int(input("Enter time (in years): "))

            CI = money * (1 + rate / 100) ** year
            print(f"Compound Interest :{CI}")
        
        elif choice == 3:
            value = int(input("Enter the value: "))
            radian = math.radians(value)
            print(f"Sin is: {math.sin(radian)}")
            print(f"Cosin is: {math.cos(radian)}")
       
        elif choice == 4:
            print("\nSelect an option: ")
            print("1. Area of Circle")
            print("2. Area of Rectangle")
            print()
            choice = int(input("Enter your choice: "))

            if choice == 1:
                radius = float(input("\n Enter the radious of Circle: "))
                Area = math.pi * radius * radius
                print(f"Area of Circle is {Area}")

            elif choice == 2:
                length = float(input("\nEnter the length of rectangle: "))
                width = float(input("Enter the breadth of rectangle: "))
                Rectangle = length * width
                print(f"Area of Rectangle is {Rectangle}")

            else:
                print("Invalid choice")

        elif choice == 5:
            break
        else:
            print("Invalid Input")
            print()

def random_opration():
    while True:
        print()
        print("Select an option: ")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            number = random.randint(1, 10)
            print(number, "\n")

        elif choice == 2:
            list = [19, 32, 7, 91, 40, 25]
            random.shuffle(list)
            print(list, "\n")

        elif choice == 3:
            len = int(input("Enter password length: "))
            character = string.ascii_letters + string.punctuation + string.digits
            password = "".join(random.choices(character, k=len))
            print(f"Generated Password: {password}\n")

        elif choice == 4:
            otp = random.randrange(100000, 999999)
            print(otp, "\n")

        elif choice == 5:
            break

        else:
            print("Invalid Input")
            print()


def uuid_operation():
    print("\nGenerate Unique Identifiers: ")
    print(f"Generated UUID:" , uuid4())
    print()

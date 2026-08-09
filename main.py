import datetime
import math
import random
import string
import uuid
import time
import file_operations

def datetime_menu():

    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                now = datetime.datetime.now()
                print("\nCurrent Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))

            case 2:
                date1 = input("\nEnter the first date (YYYY-MM-DD): ")
                date2 = input("Enter the second date (YYYY-MM-DD): ")

                d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
                d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

                difference = abs((d1 - d2).days)

                print("Difference:", difference, "days")

            case 3:
                date = input("\nEnter date (YYYY-MM-DD): ")

                d = datetime.datetime.strptime(date, "%Y-%m-%d")

                print("Formatted Date:", d.strftime("%d-%m-%Y"))

            case 4:
                print("\nStopwatch started...")
                input("Press Enter to stop stopwatch.")

                print("Stopwatch stopped.")

            case 5:
                seconds = int(input("\nEnter countdown seconds: "))

                while seconds > 0:
                    print("Time remaining:", seconds)
                    time.sleep(1)
                    seconds = seconds - 1

                print("Time's up!")

            case 6:
                break
            
            case _:
                print("Invalid choice!")

def mathematical_menu():

    while True:
        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                n = int(input("\nEnter a number: "))
                factorial = 1
                for i in range(1, n + 1):
                    factorial = factorial * i
                print("Factorial:", factorial)

            case 2:
                principal = float(input("\nEnter the amount"))
                rate = float(input("Enter the rate (%): "))
                time_years = float(input("Enter time:"))
                amount = principal * (1 + rate / 100) ** time_years
                print("Compound Interest:", format(amount, ".2f"))

            case 3:
                angle = float(input("\nEnter angle in degrees: "))
                radian = math.radians(angle)
                print("Sin:", math.sin(radian))
                print("Cos:", math.cos(radian))
                print("Tan:", math.tan(radian))

            case 4:
                print("\nGeometric Shapes:")
                print("1. Circle")
                print("2. Rectangle")
                print("3. Square")
                print("4. Triangle")

                shape = int(input("Enter your choice: "))

                match shape:
                    case 1:
                        r = float(input("Enter radius: "))
                        area = math.pi * r * r
                        print("Area of Circle:", area)

                    case 2:
                        length = float(input("Enter length: "))
                        width = float(input("Enter width: "))
                        area = length * width
                        print("Area of Rectangle:", area)

                    case 3:
                        side = float(input("Enter side: "))
                        area = side * side
                        print("Area of Square:", area)

                    case 4:
                        base = float(input("Enter base: "))
                        height = float(input("Enter height: "))
                        area = 0.5 * base * height
                        print("Area of Triangle:", area)

                    case _:
                        print("Invalid choice!")
            case 5:
                break

            case _:
                print("Invalid choice!")


def random_menu():

    while True:
        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                number = random.randint(1, 100)
                print("\nRandom Number:", number)

            case 2:
                n = int(input("\nEnter list size: "))

                numbers = []

                for i in range(n):
                    numbers.append(random.randint(1, 100))

                print("Random List:", numbers)

            case 3:
                length = int(input("\nEnter password length: "))

                characters = string.ascii_letters + string.digits

                password = ""
                for i in range(length):
                    password = password + random.choice(characters)
                print("Generated Password:", password)
            case 4:
                otp = random.randint(100000, 999999)
                print("\nGenerated OTP:", otp)

            case 5:
                break
            case _:
                print("Invalid choice!")


def generate_uuid():

    unique_id = uuid.uuid4()

    print("\nGenerated UUID:", unique_id)


def file_menu():

    while True:

        print("\nFile Operations (Custom Module):")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = int(input("Enter your choice: "))

        match choice:

            case 1:
                filename = input("\nEnter file name: ")

                file_operations.create_file(filename)

            case 2:
                filename = input("\nEnter file name: ")
                data = input("Enter data to write: ")

                file_operations.write_file(filename, data)

            case 3:
                filename = input("\nEnter file name: ")

                file_operations.read_file(filename)

            case 4:
                filename = input("\nEnter file name: ")
                data = input("Enter data to append: ")

                file_operations.append_file(filename, data)

            case 5:
                break

            case _:
                print("Invalid choice!")

def explore_module():

    print("\nExplore Module")

    module_name = input("Enter module name to explore: ")

    match module_name:
        case "math":
            print("\nAvailable Attributes in math module:")
            print(dir(math))

        case "random":
            print("\nAvailable Attributes in random module:")
            print(dir(random))

        case "datetime":
            print("\nAvailable Attributes in datetime module:")
            print(dir(datetime))
        case "string":
            print("\nAvailable Attributes in string module:")
            print(dir(string))
        case _:
            print("Module not available!")


while True:

    print("\n========================")
    print("Welcome to Multi-Utility Toolkit")
    print("========================")
    print("Choose an option:")
    print("1. Datetime and Time Operations")
    print("2. Mathematical Operations")
    print("3. Random Data Generation")
    print("4. Generate Unique Identifiers (UUID)")
    print("5. File Operations (Custom Module)")
    print("6. Explore Module Attributes (dir())")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            datetime_menu()

        case 2:
            mathematical_menu()

        case 3:
            random_menu()

        case 4:
            generate_uuid()

        case 5:
            file_menu()

        case 6:
            explore_module()

        case 7:
            print("Thank you for using the Multi-Utility Toolkit!")
            break

        case _:
            print("Invalid choice!")  
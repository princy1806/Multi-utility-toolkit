from packages.math_utils import date_time_operation,maths_operation,uuid_operation,random_opration
from packages.explore_module import explore_module
from packages.file_utils import file_operation

def main():
    while True:
        print("=============================================")
        print("Welcome To Multi-Utility Toolkit")
        print("=============================================")
        print()
        print("Select an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathemetical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers(UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes(dir())")
        print("7. Exit")
        print()

        choice = int(input("Enter your choice: "))

        if choice == 1:
            date_time_operation()
           
        elif choice == 2:
            maths_operation()

        elif choice == 3:
            random_opration()

        elif choice == 4:
            uuid_operation()

        elif choice == 5:
            file_operation()

        elif choice == 6:
            explore_module()
            print()

        elif choice == 7:
            print("===============================")
            print("Thank you for using the Multi-Utility Toolkit!")
            print("===============================")
            break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
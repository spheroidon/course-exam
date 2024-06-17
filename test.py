from tools.numbers.simp import add, subtract
from tools.numbers.comp import sum_of_digits, is_palindrome
from tools.col import myzip

def display_menu():
    print("\nSelect an option:")
    print("1. Add two numbers")
    print("2. Subtract two numbers")
    print("3. Sum of digits of a number")
    print("4. Check if a number is a palindrome")
    print("5. Zip two collections")
    print("6. Exit")

def main():
    simp_called = False

    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        try:
            if choice == '1':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print(f"Result: {add(a, b)}")
                simp_called = True

            elif choice == '2':
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print(f"Result: {subtract(a, b)}")
                simp_called = True

            elif choice == '3':
                if not simp_called:
                    raise Exception("You must call at least one function from the simp module before using comp functions.")
                number = int(input("Enter a number: "))
                print(f"Sum of digits: {sum_of_digits(number)}")

            elif choice == '4':
                if not simp_called:
                    raise Exception("You must call at least one function from the simp module before using comp functions.")
                number = int(input("Enter a number: "))
                print(f"Is palindrome: {is_palindrome(number)}")

            elif choice == '5':
                it1 = input("Enter first collection (comma-separated): ").split(',')
                it2 = input("Enter second collection (comma-separated): ").split(',')
                print(f"Zipped result: {myzip(it1, it2)}")

            elif choice == '6':
                print("Exiting...")
                break

            else:
                print("Invalid choice. Please try again.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

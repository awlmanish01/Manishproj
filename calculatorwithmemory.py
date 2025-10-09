def calc_memory():
    memory = 0     # Initialize memory variable
    result = None  # To store last calculation result

    while True:
        print("\nEnter options:")
        print("1. ADD")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Store last result in memory")
        print("6. Recall memory")
        print("7. Clear memory")
        print("8. Exit")

        choice = input("Enter your choice: ")

        # Arithmetic operations
        if choice in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == "1":
                    result = num1 + num2
                elif choice == "2":
                    result = num1 - num2
                elif choice == "3":
                    result = num1 * num2
                elif choice == "4":
                    if num2 == 0:
                        raise ValueError("Cannot divide by 0")
                    result = num1 / num2

                print("Result:", result)

            except ValueError as e:
                print("Error:", e)

        # Store result in memory
        elif choice == "5":
            if result is not None:
                memory = result
                print("Last result has been stored in memory.")
            else:
                print("No result to store in memory.")

        # Recall memory
        elif choice == "6":
            print("The value stored in memory is:", memory)

        # Clear memory
        elif choice == "7":
            memory = 0
            print("Your memory has been cleared.")

        # Exit
        elif choice == "8":
            print("Exiting the calculator.")
            break

        else:
            print("Invalid input, please try again.")

# Run the calculator
calc_memory()




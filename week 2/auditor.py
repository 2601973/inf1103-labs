inventory = 0
while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit):")

    if user_input.lower() == "quit":
        print("Goodbye, exiting program.")
        break
    
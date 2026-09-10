inventory = 0
while True:
    user_input = input("Enter stock quantity (or type 'quit' to exit):")

    if user_input.lower() == "quit":
        print("Goodbye, exiting program.")
        break
    if not user_input.isdigit():
        print("Error: That is not a valid number.")
        continue
    stock = int(user_input)
    inventory += stock
    
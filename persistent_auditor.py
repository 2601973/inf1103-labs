def load_inventory():
    try:
        with open("inventory.txt", "r") as file:
            inventory = int(file.readline().strip())
            return inventory
    except FileNotFoundError:
        return 0

def get_valid_input():
    user_input = input(
        "Enter stock quantity (or type 'quit' to exit): "
    ).strip()

    if user_input.lower() == "quit":
        return "quit"

    if not user_input.isdigit():
        print("Error: That is not a valid number.")
        return None

    return int(user_input)


def process_delivery(current_total, new_value):
    return current_total + new_value


def calculate_tax(amount):
    return amount * 0.10


def generate_report(total_units, failed_attempts):
    print(
        f"\nTotal Units Processed: {total_units}"
        f"\nNumber of Failed Entries: {failed_attempts}"
    )

inventory = load_inventory()
failed_entries = 0
deliveries_processed = 0
transaction_history = []

while True:
    stock = get_valid_input()

    if stock == "quit":
        print("Goodbye, exiting program.")
        break

    if stock is None:
        failed_entries += 1
        continue

    inventory = process_delivery(inventory, stock)
    transaction_history.append(stock)
    tax = calculate_tax(stock)
    deliveries_processed += 1

    print(f"Tax for this delivery: {tax:.2f}")

    if inventory > 500:
        print(
            "Inventory has exceeded the 500 unit limit! "
            f"Current inventory: {inventory}"
        )
    elif inventory == 500:
        print("Inventory has reached exactly 500 units.")
    else:
        print(f"Current Total: {inventory}")


generate_report(inventory, failed_entries)
print(f"Total Deliveries Processed: {deliveries_processed}")
import time
from datetime import datetime

# Global data set
staffdatapassword = "122"
staffdatausername = "staff"
data_list = {}
receipt_counter = 1

# Intro
def greet():
    print("========== WATER REFILLING SALES RECORD AND RECEIPT =============")


# Staff log in portal
def log_in_S():
    print("\n--- STAFF LOG IN ---")
    usernameS = input("Enter username: ").strip()
    passwordS = input("Enter password: ").strip()

    if usernameS == staffdatausername and passwordS == staffdatapassword:
        print("Redirecting to staff menu.......")
        time.sleep(1)
        staff()
    else:
        print("Invalid credentials! Try again.\n")
        log_in_S()


# Customer view portal
def log_in_C():
    print("\n--- CUSTOMER LOG IN ---")

    while True:
        customer_name = input( "Enter your registered full name (or 'back' to return): ").strip()

        if customer_name.lower() == "back":
            menu()
            return

        if not customer_name:
            print("Invalid input! Name cannot be empty.")
            continue

        if customer_name not in data_list:
            print("Customer not registered.")
            continue


        break

    record = data_list[customer_name]

    while True:
        password_input = input("Enter your password (or 'back' to return): ").strip()

        if password_input.lower() == "back":
            menu()
            return

        if password_input != record["customer_password"]:
            print("Incorrect password! Try again.")
            continue


        break

    print("\nLogin Success!")
    total_price_str = f"P{record['total']:.2f}"

    print("\n========================================================")
    print("         DEEP SOURCE WATER REFILLING STATION            ")
    print("          152 Lirio St, Cagayan de Oro City             ")
    print("              Contact No. 0918-642-9196                 ")
    print("========================================================")
    print(f"Receipt No.  : {record['receipt_no']}")
    print(f"Date/Time    : {record['date'].strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Customer     : {customer_name}")
    print("--------------------------------------------------------")
    print(f"{'Item':<18}{'Quantity':<12}{'Price':<12}{'Total':<12}")
    print("--------------------------------------------------------")
    print(f"{'Water Refill':<18}{record['quantity']:<12}{'P25.00':<12}{total_price_str:<12}")
    print("--------------------------------------------------------")
    print(f"TOTAL AMOUNT : P{record['total']:.2f}")
    print(f"Amount Paid  : P{record['cash']:.2f}")
    print(f"Change       : P{record['change']:.2f}")
    print("========================================================")
    print("             THANK YOU FOR PURCHASING                   ")
    print("========================================================")
    input("\nPress Enter to return to main menu...")
    menu()

# Staff main menu
def staff():
    global receipt_counter
    print("\n--- STAFF MENU ---")
    choices = [
        "1: View registered customers",
        "2: Register customer",
        "3: View total earnings",
        "4: Update registered customers",
        "5: Log out"
    ]
    print(*choices, sep="\n")
    choice = input("Input choice: ").strip()

    if choice == "1":
        print("\n--- REGISTERED CUSTOMERS ---")
        if not data_list:
            print("No customers registered yet.")
            input("\nPress Enter to return to staff menu...")
            return staff()

        for record in data_list.values():
            print(f"Customer ID: {record['customer_id']}")

        while True:
            customer_id = input(
                "\nEnter Customer ID to view details "
                "(or enter (back) to exit): "
            ).strip().lower()

            if not customer_id:
                print("Invalid input! Customer ID cannot be empty.")
                continue
            elif customer_id == "back":
                return staff()
            try:
                customer_id = int(customer_id)
            except ValueError:
                print("Invalid input! Enter numbers only.")
                continue

            record = None
            username = ""

            for name, details in data_list.items():
                if details["customer_id"] == customer_id:
                    record = details
                    username = name
                    break

            if record:
                break
            else:
                print("Customer not registered.")

        if record:
            total_price_str = f"P{record['total']:.2f}"

            print("\n========================================================")
            print("         DEEP SOURCE WATER REFILLING STATION            ")
            print("          152 Lirio St, Cagayan de Oro City             ")
            print("              Contact No. 0918-642-9196                 ")
            print("========================================================")
            print(f"Receipt No.  : {record['receipt_no']}")
            print(f"Date/Time    : {record['date'].strftime('%Y-%m-%d %H:%M:%S')}")
            print(f"Customer     : {username}")
            print("--------------------------------------------------------")
            print(f"{'Item':<18}{'Quantity':<12}{'Price':<12}{'Total':<12}")
            print("--------------------------------------------------------")
            print(f"{'Water Refill':<18}{record['quantity']:<12}{'P25.00':<12}{total_price_str:<12}")
            print("--------------------------------------------------------")
            print(f"TOTAL AMOUNT : P{record['total']:.2f}")
            print(f"Amount Paid  : P{record['cash']:.2f}")
            print(f"Change       : P{record['change']:.2f}")
            print("========================================================")
            print("             THANK YOU FOR PURCHASING                   ")
            print("========================================================")

        input("\nPress Enter to return to staff menu...")
        staff()

    elif choice == "2":
        print("\n========== CUSTOMER REGISTER PORTAL ==========")

        while True:
            print("\nEnter Full Name")

            while True:
                first_name = input("First Name (type 'back' to go back): ").strip()

                if first_name.lower() == "back":
                    return staff()
                elif first_name == "":
                    print("First name cannot be empty.")
                elif not first_name.replace(" ", "").isalpha():
                    print("Invalid first name! Letters only.")
                else:
                    first_name = first_name.upper()
                    break

            while True:
                middle_initial = input("M.I. (type 'exit' to go back): ").strip().rstrip(".").upper()

                if middle_initial.lower() == "exit":
                    return staff()
                if middle_initial == "":
                    print("M.I. cannot be empty.")
                elif not middle_initial.isalpha():
                    print("Invalid M.I.! Letters only.")
                elif len(middle_initial) != 1:
                    print("Invalid M.I.! Enter only one letter.")
                else:
                    break

            while True:

                last_name = input("Last Name (type 'exit' to go back): ").strip()
                if last_name.lower() == "exit":
                    return staff()
                if last_name == "":
                    print("Last name cannot be empty.")
                elif not last_name.replace(" ", "").isalpha():
                    print("Invalid last name! Letters only.")
                else:
                    last_name = last_name.upper()
                    break

            name = f"{first_name} {middle_initial}. {last_name}"

            if name in data_list:
                print("Error: Name already registered!")
                continue

            while True:
                customer_password = input("Create password: ").strip()

                if not customer_password:
                    print("Invalid input! Password cannot be empty.")
                    continue
                break

            break

        while True:
            try:
                order = int(input("Enter number of refills (P25 per refill): "))
                if order > 0:
                    break
                print("Invalid input! Quantity must be greater than 0.")
            except ValueError:
                print("Invalid input! Enter a whole number.")

        while True:
            try:
                total = print(f"Total amount: P", order * 25)
                cash = float(input("Enter cash amount: P").strip())
                if cash < 0:
                    print("Invalid input! Cash cannot be negative.")
                elif cash >= order * 25:
                    change = cash - (order * 25)
                    break
                else:
                    print(f"Insufficient cash! Total cost is P{order * 25:.2f}.")
            except ValueError:
                print("Invalid input! Enter a valid cash amount.")

        print("\n===== Customer Details =====")
        print(f"Full Name: {name}")
        print(f"Refills Sold: {order}")
        print(f"Total: P{order * 25:.2f}")
        print(f"Total cash rendered:P",cash)
        print(f"Change: P{change:.2f}")

        while True:
            confirmation = input(
                "Proceed with the registration/transaction? "
                "(yes/no/cancel): "
            ).strip().lower()

            if confirmation == "yes":
                formatted_receipt = f"{receipt_counter:04d}"
                customer_id = len(data_list) + 1
                data_list[name] = {
                     "customer_id": customer_id,
                    "customer_password": customer_password,
                    "quantity": order,
                    "total": order * 25,
                    "cash": cash,
                    "change": change,
                    "date": datetime.now(),
                    "receipt_no": formatted_receipt
                }
                receipt_counter += 1
                print(f"Successfully registered {name}! Receipt No.: {formatted_receipt}")
                return staff()

            elif confirmation == "no":
                print("Registration not saved.")
                return staff()

            elif confirmation == "cancel":
                print("Registration canceled.")
                return staff()

            else:
                print("Invalid choice! Enter yes, no, or cancel.")

    elif choice == "3":
        print("\n--- TOTAL SALES & EARNINGS ---")
        print(f"Date/Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        if not data_list:
            print("No sales recorded yet.")
            return staff()

        total_earnings = sum(record["total"] for record in data_list.values())
        total_refills = sum(record["quantity"] for record in data_list.values())
        print(f"Total Refills Sold: {total_refills}")
        print(f"Grand Total Earnings: P{total_earnings:.2f}")

        input("\nPress Enter to return to staff menu...")
        staff()

    elif choice == "4":

       while True:
        print("\n--- UPDATE REGISTERED CUSTOMER ---")
        if not data_list:
            print("No customers registered yet.")
            return staff()

        for registered_name, record in data_list.items():
            print(f"- {registered_name}")

        while True:
            username = input( "Enter full name to update (or type 'back' to return): ").strip()

            if username.lower() == "back":
                return staff()

            if not username:
                print("Invalid input! Customer name cannot be empty.")
                continue

            if not username.replace(" ", "").replace(".", "").isalpha():
                print("Invalid input! Letters only.")
                continue

            if username not in data_list:
                print("Customer not registered.")
                continue

            break

        record = data_list[username]
        print(f"\n--- Choose what to update for {username} ---")
        print("1. Update name")
        print("2. Update password")
        print("3. Add refills")
        print("4. Back")
        edit_choice = input("Input choice: ").strip()

        if edit_choice == "1":

            while True:
                new_first = input(
                    "First Name (type 'back' to go back): "
                ).strip()

                if new_first.lower() == "back":
                    return staff()
                elif new_first == "":
                    print("First name cannot be empty.")
                elif not new_first.replace(" ", "").isalpha():
                    print("Invalid first name! Letters only.")
                else:
                    new_first = new_first.upper()
                    break

            while True:
                new_middle = input("M.I. (one letter only): ").strip().rstrip(".").upper()

                if new_middle == "":
                    print("M.I. cannot be empty.")
                elif not new_middle.isalpha():
                    print("Invalid M.I.! Letters only.")
                elif len(new_middle) != 1:
                    print("Invalid M.I.! Enter only one letter.")
                else:
                    break

            while True:
                new_last = input("Last Name: ").strip()

                if new_last == "":
                    print("Last name cannot be empty.")
                elif not new_last.replace(" ", "").isalpha():
                    print("Invalid last name! Letters only.")
                else:
                    new_last = new_last.upper()
                    break

            new_name = f"{new_first} {new_middle}. {new_last}"

            if new_name in data_list and new_name != username:
                print("Error: Name already registered!")
                return staff()

            data_list[new_name] = data_list.pop(username)
            print(f"Name updated to {new_name}.")

            input("\nPress Enter to return to update menu...")
            continue

        elif edit_choice == "2":
            new_pass = input("Enter new password (or type 'back'): ").strip()
            if new_pass.lower() == "back":
                return staff()
            if not new_pass:
                print("Invalid input! Password cannot be empty.")
                return staff()
            record["customer_password"] = new_pass
            print("Password updated.")

        elif edit_choice == "3":
            try:
                additional_refills = int(input("Enter additional refills (or type 0 to go back): "))
                if additional_refills == 0:
                    return staff()
                if additional_refills < 0:
                    print("Invalid input! Quantity must be greater than 0.")
                    return staff()

                added_cost = additional_refills * 25
                while True:
                    try:
                        add_cash = float(input(f"Enter cash paid (P{added_cost:.2f} due): P"))
                        if add_cash < added_cost:
                            print("Insufficient cash.")
                        elif add_cash < 0:
                            print("Invalid input! Cash cannot be negative.")
                        else:
                            add_change = add_cash - added_cost
                            record["quantity"] += additional_refills
                            record["total"] += added_cost
                            record["cash"] += add_cash
                            record["change"] = record["cash"] - record["total"]
                            print(f"Change for added refills: P{add_change:.2f}")
                            print(f"New total refills: {record['quantity']}")
                            print(f"New total amount: P{record['total']:.2f}")
                            break
                    except ValueError:
                        print("Invalid input! Enter a valid cash amount.")
            except ValueError:
                print("Invalid input! Enter a whole number.")

        elif edit_choice == "4":
            return staff()
        else:
            print("Invalid choice.")

        input("\nPress Enter to return to update menu...")
        continue

    elif choice == "5":
        print("Logging out........")
        time.sleep(1)
        menu()
    else:
        print("Invalid option.")
        staff()


# Main menu
def menu():
    print("\n--- Sales record system ---")
    print("\n--- MAIN MENU ---")
    choices = ["1. Staff", "2. Customer", "3. Exit"]
    print(*choices, sep="\n")
    choice = input("Input choice: ").strip()

    if choice == "1":
        print("Redirecting to staff.....")
        time.sleep(1)
        log_in_S()
    elif choice == "2":
        print("Redirecting to Customer......")
        time.sleep(1)
        log_in_C()
    elif choice == "3":
        print("Thank you for using the system!")
        exit()
    else:
        print("Invalid choice.")
        menu()

greet()
menu()
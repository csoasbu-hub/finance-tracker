history = []  # Our data storage

while True:
    print("\n1 - Add Expense, 2 - Show History, 3 - Exit, 4 - Search")
    choice = input("Select an option: ")
    
    if choice == "1":
        item = input("What did you buy? ")
        price = int(input("How much did it cost? "))
        new_entry = {"item": item, "price": price}
        history.append(new_entry)
        print("Successfully saved!")

    elif choice == "2":
        print("\n--- YOUR EXPENSES ---")
        total_sum = 0
        for record in history:
            total_sum += record['price']
            print(f"Item: {record['item']} | Price: {record['price']}")
        print("-" * 20)
        print(f"TOTAL SPENT: {total_sum}")

    elif choice == "4":
        search_input = input("Write what you search: ")
        print(f"\n--- Search results for '{search_input}' ---")
        found = False
        for record in history:
            # Сравниваем в нижнем регистре, чтобы 'Apple' и 'apple' были равны
            if search_input.lower() == record['item'].lower():
                print(f"Found: {record['item']} | Price: {record['price']}")
                found = True
        if not found:
            print("Nothing found.")

    elif choice == "3":
        print("Exiting. Goodbye!")
        break
history = []  # Our data storage

while True:
    print("\n1 - Add Expense, 2 - Show History, 3 - Exit")
    choice = input("Select an option: ")
    
    if choice == "1":
        # Input data
        item = input("What did you buy? ")
        price = int(input("How much did it cost? "))
        
        # Create a dictionary and add it to the list
        new_entry = {"item": item, "price": price}
        history.append(new_entry)
        print("Successfully saved!")

    elif choice == "2":
            print("\n--- YOUR EXPENSES ---")
            total_sum = 0
            for record in history:
                # Считаем сумму (теперь ключ в кавычках)
                total_sum += record['price']
                # Выводим только товар
                print(f"Item: {record['item']} | Price: {record['price']}")
            
            # Выводим ИТОГ один раз в самом конце
            print("-" * 20)
            print(f"TOTAL SPENT: {total_sum}")

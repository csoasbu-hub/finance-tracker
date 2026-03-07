
history = []  # Наш список-склад

while True:
    print("\n1 - Add (Добавить), 2 - Show (Показать), 3 - Exit (Выход)")
    choice = input("Выбери действие: ")
    
    if choice == "1":
        # 1. Спроси название (item)
        item = input("Что купил? ")
        # 2. Спроси цену (price) и преврати в int()
        price = int(input("Сколько стоит? "))
        
        # 3. Создай словарь и добавь его в список
        new_entry = {"item": item, "price": price}
        history.append(new_entry)
        print("Сохранено!")

    elif choice == "2":
        print("--- Твои расходы ---")
        # 4. Напиши цикл for, чтобы вывести всё из history
        for record in history:
            print(record)

    elif choice == "3":
        print("Выход...")
        break
        
         

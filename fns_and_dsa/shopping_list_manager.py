def display_menu():
    print()
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            add_item = input("Enter the item to add: ").strip().lower()
            shopping_list.append(add_item)
            print(f"'{add_item}' has been added to your shopping list.")
        elif choice == '2':
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                remove_item = input("Enter the item to remove: ")
                if remove_item in shopping_list:
                    shopping_list.remove(remove_item)
                    print(f"'{remove_item}' has been removed from your shopping list.")
                else:
                    print(f"'{remove_item}' is not in your shopping list.")
        elif choice == '3':
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                print("Your shopping list:")
                for item in shopping_list:
                    print(item)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

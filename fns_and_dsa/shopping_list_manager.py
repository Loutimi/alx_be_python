def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []

    while True:
        display_menu()
        choice = int(input("Enter your choice: "))

        if choice == 1:
            item = input("Enter item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to your shopping list.")
        elif choice == 2:
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                item = input("Enter item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' is not in your shopping list.")
        elif choice == 3:
            if len(shopping_list) == 0:
                print("Your shopping list is empty.")
            else:
                print("Your shopping list:")
                for item in shopping_list:
                    print(item)
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")

if __name__ == "__main__":
    main()

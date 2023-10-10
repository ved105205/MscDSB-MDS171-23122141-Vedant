# petstoremain.py
from petstore import PetStore

def admin_menu(pet_store):
    while True:
        print("\nAdmin Menu:")
        print("1. Add a new pet")
        print("2. List all pets")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            price = float(input("Enter pet price: "))
            pet_store.store_pet(name, species, price)
            print(f"{name} has been added to the store.")
        elif choice == '2':
            pets = pet_store.list_all_pets()
            if pets:
                print("\nList of all pets:")
                for pet in pets:
                    print(f"Name: {pet['name']}, Species: {pet['species']}, Price: {pet['price']}")
            else:
                print("No pets available in the store.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

def user_menu(pet_store):
    while True:
        print("\nUser Menu:")
        print("1. Search for a pet")
        print("2. Buy a pet")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter pet name to search: ")
            pet = pet_store.search_pet(name)
            if pet:
                print(f"Name: {pet['name']}, Species: {pet['species']}, Price: {pet['price']}")
            else:
                print("Pet not found.")
        elif choice == '2':
            name = input("Enter pet name to buy: ")
            pet = pet_store.sell_pet(name)
            if pet:
                print(f"You have bought {pet['name']} for ${pet['price']}.")
            else:
                print("Pet not found or out of stock.")
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    pet_store = PetStore()
    
    while True:
        print("\nWelcome to the Pet Store")
        print("1. Admin")
        print("2. User")
        print("3. Exit")
        role = input("Enter your role (1/2/3): ")

        if role == '1':
            admin_menu(pet_store)
        elif role == '2':
            user_menu(pet_store)
        elif role == '3':
            break
        else:
            print("Invalid choice. Please try again.")

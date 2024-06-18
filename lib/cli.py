from models.dog import Dog
from models.adopter import Adopter
from models.adoption import Adoption

def main():
    Dog.create_table()
    Adopter.create_table()
    Adoption.create_table()

    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            print("Exiting the program...")
            break
        elif choice == "1":
            create_dog()
        elif choice == "2":
            create_adopter()
        elif choice == "3":
            create_adoption()
        elif choice == "4":
            show_items()
        elif choice == "5":
            delete_item()
        else:
            print("Invalid choice. Please select a valid option.")

def menu():
    print("\nPlease select an option:")
    print("0. Exit the program")
    print("1. New dog rescued")
    print("2. Adopter's information")
    print("3. Make an appointment for adoption")
    print("4. Show adoption centre information")
    print("5. Remove a dog that has been adopted")

def create_dog():
    print("\nRescue a new dog:")
    name = input("Enter the dog's name: ")
    breed = input("Enter the dog's breed: ")
    age = int(input("Enter the dog's age: "))
    gender = input("Enter the dog's gender: ")
    vaccinated = input("Is the dog vaccinated? (y/n): ").lower() == "y"
    dog = Dog.create(name, breed, age, gender, vaccinated)
    print(f"\nDog '{dog.name}' rescued successfully with ID {dog.id}")

def create_adopter():
    print("\nAdd adopter's information:")
    name = input("Enter the adopter's name: ")
    contact = input("Enter the adopter's contact: ")
    adopter = Adopter.create(name, contact)
    print(f"\nAdopter '{adopter.name}' added successfully with ID {adopter.id}")

def create_adoption():
    print("\nMake an appointment for adoption:")
    dog_id = int(input("Enter the ID of the dog: "))
    adopter_id = int(input("Enter the ID of the adopter: "))
    adoption_date = input("Enter the adoption date (YYYY-MM-DD HH:MM:SS): ")
    adopted = input("Has the dog been adopted? (y/n): ").lower() == "y"
    adoption = Adoption.create(dog_id, adopter_id, adoption_date, adopted)
    print(f"\nAppointment for adoption created successfully with ID {adoption.id}")

def show_items():
    print("\nSelect the item type to show:")
    print("1. Dogs")
    print("2. Adopters")
    print("3. Adoptions")
    item_type = input("Enter your choice: ")
    if item_type == "1":
        list_dogs()
    elif item_type == "2":
        list_adopters()
    elif item_type == "3":
        list_adoptions()
    else:
        print("Invalid choice. Please select a valid option.")

def list_dogs():
    dogs = Dog.select_dogs()
    for dog in dogs:
        print(f"ID: {dog.id}, Name: {dog.name}, Breed: {dog.breed}, Age: {dog.age}, Gender: {dog.gender}, Vaccinated: {dog.vaccinated}")

def list_adopters():
    adopters = Adopter.select_adopters()
    for adopter in adopters:
        print(f"ID: {adopter.id}, Name: {adopter.name}, Contact: {adopter.contact}")

def list_adoptions():
    adoptions = Adoption.select_adoptions()
    for adoption in adoptions:
        print(f"ID: {adoption.id}, Dog ID: {adoption.dog_id}, Adopter ID: {adoption.adopter_id}, Adoption Date: {adoption.adoption_date}, Returned: {'Yes' if adoption.returned else 'No'}")


def delete_item():
    print("\nSelect the item type to delete:")
    print("1. Dog")
    item_type = input("Enter your choice: ")
    if item_type == "1":
        delete_dog()
  
        print("Invalid choice. Please select a valid option.")

def delete_dog():
    try:
        dog_id = int(input("Enter the ID of the dog to delete: "))
    except ValueError:
        print("Invalid input. Please enter a numeric ID.")
        return
    
    dog = Dog.find_by_id(dog_id)
    if dog:
        dog.delete()
        print(f"\nDog '{dog.name}' deleted successfully")
    else:
        print("\nDog not found")



if __name__ == "__main__":
    main()

from models.dog import Dog
from models.adopter import Adopter
from models.adoption import Adoption

def main():
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
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Create a dog")
    print("2. Create an adopter")
    print("3. Create an adoption")

def create_dog():
    name = input("Enter dog's name: ")
    breed = input("Enter dog's breed: ")
    age = int(input("Enter dog's age: "))
    gender = input("Enter dog's gender: ")
    vaccinated = input("Is the dog vaccinated? (y/n): ").lower() == "y"
    # You can add more attributes as needed
    dog = Dog.create(name, breed, age, gender, vaccinated)
    print(f"Dog '{dog.name}' created successfully with ID {dog.id}")

def create_adopter():
    name = input("Enter adopter's name: ")
    contact = input("Enter adopter's contact: ")
    # You can add more attributes as needed
    adopter = Adopter.create(name, contact)
    print(f"Adopter '{adopter.name}' created successfully with ID {adopter.id}")

def create_adoption():
    dog_id = int(input("Enter dog's ID: "))
    adopter_id = int(input("Enter adopter's ID: "))
    adoption_date = input("Enter adoption date (YYYY-MM-DD HH:MM:SS): ")
    returned = input("Has the dog been returned? (y/n): ").lower() == "y"
    # You can add more attributes as needed
    adoption = Adoption.create(dog_id, adopter_id, adoption_date, returned)
    print(f"Adoption created successfully with ID {adoption.id}")

if __name__ == "__main__":
    main()

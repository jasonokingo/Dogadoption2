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
        show_dogs()
    elif item_type == "2":
        show_adopters()
    elif item_type == "3":
        show_adoptions()
    else:
        print("Invalid choice. Please select a valid option.")

def show_dogs():
    dogs = Dog.find_all()
    if dogs:
        print("\nAvailable dogs for adoption:")
        for dog in dogs:
            print(f"ID: {dog.id}, Name: {dog.name}, Breed: {dog.breed}, Age: {dog.age}, Gender: {dog.gender}, Vaccinated: {'Yes' if dog.vaccinated else 'No'}")
    else:
        print("\nNo dogs found for adoption")

def show_adopters():
    adopters = Adopter.find_all()
    if adopters:
        print("\nList of adopters:")
        for adopter in adopters:
            print(f"ID: {adopter.id}, Name: {adopter.name}, Contact: {adopter.contact}")
    else:
        print("\nNo adopters found")

def show_adoptions():
    adoptions = Adoption.find_all()
    if adoptions:
        print("\nAppointments for adoption:")
        for adoption in adoptions:
            print(f"ID: {adoption.id}, Dog ID: {adoption.dog_id}, Adopter ID: {adoption.adopter_id}, Adoption Date: {adoption.adoption_date}, Adopted: {'Yes' if adoption.adopted else 'No'}")
    else:
        print("\nNo appointments for adoption found")

def delete_item():
    print("\nSelect the item type to delete:")
    print("1. Dog")
    print("2. Adopter")
    print("3. Adoption")
    item_type = input("Enter your choice: ")
    if item_type == "1":
        delete_dog()
    elif item_type == "2":
        delete_adopter()
    elif item_type == "3":
        delete_adoption()
    else:
        print("Invalid choice. Please select a valid option.")

def delete_dog():
    dog_id = int(input("Enter the ID of the dog to delete: "))
    dog = Dog.find_by_id(dog_id)
    if dog:
        dog.delete()
        print(f"\nDog '{dog.name}' deleted successfully")
    else:
        print("\nDog not found")

def delete_adopter():
    adopter_id = int(input("Enter the ID of the adopter to delete: "))
    adopter = Adopter.find_by_id(adopter_id)
    if adopter:
        adopter.delete()
        print(f"\nAdopter '{adopter.name}' deleted successfully")
    else:
        print("\nAdopter not found")

def delete_adoption():
    adoption_id = int(input("Enter the ID of the adoption to delete: "))
    adoption = Adoption.find_by_id(adoption_id)
    if adoption:
        adoption.delete()
        print(f"\nAdoption deleted successfully")
    else:
        print("\nAdoption not found")

if __name__ == "__main__":
    main()

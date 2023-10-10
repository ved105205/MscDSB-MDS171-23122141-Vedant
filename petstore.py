#create a petstore class where you have the details of pets availibile and their details .
#the class will have method
#store a new pet details
#sell a pet
#list all pets 
#importing your petstore class, create, a petstoremain file, where you will implement a menu driven programfor admin- who will manage the storeuser who will see pets and buy pets.

# petstore.py

# petstore.py

class PetStore:
    def __init__(self):
        self.pets = []

    def store_pet(self, name, species, price):
        pet = {'name': name, 'species': species, 'price': price}
        self.pets.append(pet)

    def search_pet(self, name):
        for pet in self.pets:
            if pet['name'] == name:
                return pet
        return None

    def sell_pet(self, name):
        pet = self.search_pet(name)
        if pet:
            self.pets.remove(pet)
            return pet
        return None

    def list_all_pets(self):
        return self.pets

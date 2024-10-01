import json

class DuplicateNameError(Exception):
    pass
class NonExistentPet(Exception):
    pass

class NeighborhoodPets:
    def __init__(self) -> None:
        self._all_pets = {} #{pet_name: (species, pet_owner)}

    def add_pet(self, pet_name, species, pet_owner):
        if pet_name in self._all_pets:
            raise DuplicateNameError(f"{pet_name} is similar to the name of an existing pet!")
        else:
            self._all_pets[pet_name] = {
                "species" : species, 
                "owner": pet_owner
            }

    def delete_pet(self, pet_name):
        if pet_name in self._all_pets:
            del self._all_pets[pet_name]
        else:
            raise NonExistentPet("Pet doesn't exist")

    def get_owner(self, pet_name):
        if pet_name in self._all_pets:
            return self._all_pets[pet_name]["owner"]
        else:
            raise NonExistentPet('Pet does not exist.')
        
    def save_as_json(self, file_name):
        with open(file_name, 'w') as outfile:
            json.dump(self._all_pets, outfile)

    def read_json(self, file_name):
        with open(file_name, 'r') as infile:
            self._all_pets = json.load(infile)
            print(self._all_pets)

    def get_all_species(self):
        all_species = []
        for pet_data in self._all_pets.values():
            all_species.append(pet_data["species"])
        return set(all_species)

np = NeighborhoodPets()
try:
    np.add_pet("Fluffy", "gila monster", "Oksana")
    np.add_pet("Tiny", "stegasaurus", "Rachel")
    np.add_pet("Spot", "zebra", "Farrokh")
except DuplicateNameError:
    print('You tried to enter a pet with the same name as another pet.')
np.save_as_json("pets.json")
np.delete_pet("Tiny")
# spot_owner = np.get_owner("Spot")
# # np.read_json("pets.json")  # where other_pets.json is a file it saved in some previous session
# species_set = np.get_all_species()
# print(species_set)
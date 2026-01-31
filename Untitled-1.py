class Dog:
    # Class variable (shared by all instances)
    # Represents the common species for all dogs created using this class
    species = "Canis familiaris"

    def __init__(self, name, breed):
        # Instance variables (unique to each instance)
        self.name = name
        self.breed = breed

    def display_details(self):
        """Method to display the details of the dog instance."""
        print(f"Name: {self.name}")
        print(f"Breed: {self.breed}")
        print(f"Species: {Dog.species}") # Accessing the class variable
        print("-" * 20)

# Create two instances (objects) of the Dog class
dog1 = Dog("Buddy", "Labrador Retriever")
dog2 = Dog("Charlie", "German Shepherd")

# Display details for both dogs
print("Details of the first dog:")
dog1.display_details()

print("Details of the second dog:")
dog2.display_details()

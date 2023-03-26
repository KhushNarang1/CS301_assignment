class CulturalDestination:
    def __init__(self, name, location, heritage, platform):
        self.name = name
        self.location = location
        self.heritage = heritage
        self.platform = platform

    def display_info(self):
        print(f"Welcome to {self.name}, located in {self.location}.")
        print(f"Our cultural destination celebrates the heritage of {self.heritage} and provides a platform for emerging talents through {self.platform} technology solutions.")

# Prompt the user for information about the cultural destination
name = input("Enter the name of the cultural destination: ")
location = input("Enter the location of the cultural destination: ")
heritage = input("Enter the heritage celebrated by the cultural destination: ")
platform = input("Enter the digital technology solutions used by the cultural destination: ")

# Create an instance of the CulturalDestination class
new_destination = CulturalDestination(name, location, heritage, platform)

# Display information about the cultural destination
new_destination.display_info()

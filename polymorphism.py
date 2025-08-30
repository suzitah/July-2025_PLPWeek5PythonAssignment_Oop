class Car:
    def move(self):
        print("🚗 The car is driving on the road.")

class Plane:
    def move(self):
        print("✈️ The plane is flying in the sky.")

class Boat:
    def move(self):
        print("🚤 The boat is sailing on the water.")

class Dog:
    def move(self):
        print("🐕 The dog is running on the ground.")


# Create a list of objects
objects = [Car(), Plane(), Boat(), Dog()]

# Loop through each object and call move()
for obj in objects:
    obj.move()
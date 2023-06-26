class herbivores():
    def eats(self):
        print("Eats plants")
class carnivores():
    def eats(self):
        print("Eats flesh")
def func(obj):
    obj.eats()
h1=herbivores()
c1=carnivores()
func(h1)
func(c1)
class animal:
    def speaks(self):
        print("...")
class cat(animal):
    def eats(self):
        print("Eats plants")
    def speaks(self):
        print("Meows")
class lion(animal):
    def eats(self):
        print("Eats flesh")
    def speaks(self):
        print("Roars")
animals=[cat(),lion()]
def func(obj):
    obj.eats()
# h1=herbivores()
# c1=carnivores()
for animal in animals:
    animal.speaks()

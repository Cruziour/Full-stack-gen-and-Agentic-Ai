class Chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    

cup = Chaicup()
print(cup.describe())
print(Chaicup.describe(cup)) # Chaicup.describe() missing 1 required positional argument: 'self'

cup_two = Chaicup()
cup_two.size = 100
# print(cup_two.describe())
print(Chaicup.describe(cup_two))
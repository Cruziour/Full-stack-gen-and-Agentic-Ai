class Chai:
    temperature = 'hot'
    strength = 'Strong'

cutting_chai = Chai()

print(cutting_chai.temperature)

cutting_chai.temperature = 'Mild'
cutting_chai.cup = "small"

print("After chaning:", cutting_chai.temperature)
print("Cup size is:", cutting_chai.cup)
print("Direct look into the class:", Chai.temperature)

del cutting_chai.temperature
# del cutting_chai.cup
print(cutting_chai.temperature)
# print(cutting_chai.cup)
class Chai:
    origin = 'India' # properities

print(Chai.origin)

Chai.is_hot = True
print(Chai.is_hot)

# creating objects from class Chai

masala = Chai()
print(f"Masala: {masala.origin}")
print(f"Masala: {masala.is_hot}")

masala.is_hot = False

print(f'Class value: {Chai.is_hot}')
print(f"Masala: {masala.is_hot}")

masala.flavor = 'Masala'

print(masala.flavor)

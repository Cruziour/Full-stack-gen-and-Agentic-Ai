# value = 13
# remainder = value % 5

# if remainder:
#     print(f"Not divisible, remainder is {remainder}")

# Walrus operator
value = 13

if (remainder := value % 5):
    print(f"Not divisible, remainder is {remainder}")


available_sized = ['small', 'medium', 'large']

# if (requested_size := input('Enter your chai cup size: ')) in available_sized:
#     print(f'Serving {requested_size} chai')
# else:
#     print(f'Size is unavailable - {requested_size}')

flavors = ['masala', 'ginger', 'lemon','mint']
print(f'Available flavors - {flavors}')

while (flavor := input('Choose your flavor: ')) not in flavors:
    print(f'Sorry, {flavor} is not available')
    print(f'You choose {flavor} chai')
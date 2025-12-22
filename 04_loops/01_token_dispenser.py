# for token in range(1, 11):
#     print(f'Serving chai to token #{token}')

# for batch in range(1,5):
#     print(f'Preparing chai for batch #{batch}')

orders = ['Rupesh', 'Kumar', "Raushan",'Rohan']

# for name in orders:
#     print(f'Order ready for {name}')

menu = ['Green Tea', 'Lemon', 'Spiced', 'Mint']

# for m in menu:
#     print(f'Menu item is {m}')

# for idx, item in enumerate(menu, start=1):
#     print(f'{idx} : {item} chai')

# output
# 1 : Green Tea chai
# 2 : Lemon chai
# 3 : Spiced chai
# 4 : Mint chai

names = ['Rupesh','Jyoti','ALi','Sohan']
bills = [50,70,100,75]

# for name, amount in zip(names, bills):
#     print(f'{name} paid {amount} rupees.')

temperature = 40

# while temperature < 100:
#     print(f"Current temperature: {temperature}")
#     # temperature = temperature + 15
#     temperature += 15
#     # print(f"Current temperature: {temperature}")

# print(f'The tea is ready to serve')

flavours = ['Ginger', 'Out of Stock','Lemon', 'Discontinued', 'Tlsi']

# for flavour in flavours:
#     if flavour == 'Out of Stock':
#         continue
#     if flavour == 'Discontinued':
#         print(f'{flavour} item found')
#         break
#     print(f'{flavour} item found')
# print(f"Out side of loop")

staff = [('Amit', 16),("Zara", 25), ('Raj', 15)]

for name, age in staff:
    if age >= 18:
        print(f'{name} is eligible to mange the staff')
        break
else:
    print(f'No one is eligible to mange the staff')
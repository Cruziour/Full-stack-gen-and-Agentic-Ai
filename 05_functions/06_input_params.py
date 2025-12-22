# chai = 'Ginger chai'

# def prepare_chai(order):
#     print(f'Preparing: {chai}')

# prepare_chai(chai)
# print(chai)



chai = [1,2,3] #list is mutable
def edit_chai(cup):
    cup[1] = 42

edit_chai(chai)

print(chai)

def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai('Darjeeling','Yes', 'Low') # positional
make_chai(tea='Green', sugar='Medium', milk='NO') # keyword

def special_chai(*ingredients, **extras):
    print(f"Ingredients: {ingredients}")
    print(f"Extras: {extras}")

special_chai('Cinnamon', 'Cardamom', sweetener='Honey', foam='yes')

# def chai_order(order=[]):
#     order.append('Masala Chai')
#     print(order)

def chai_order(order=None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()



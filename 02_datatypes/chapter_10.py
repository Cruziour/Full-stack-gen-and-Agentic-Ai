# Dictionary
chai_order= dict(type='Masala Chai', size='Large', sugar=2)
print(f'Chai order: {chai_order}')

chai_recipe = {}
chai_recipe['base'] = 'black tea'
chai_recipe['liquid'] = 'milk'

print(f'Recipe base: {chai_recipe['base']}')
print(f'Recipe base: {chai_recipe}')
del chai_recipe['liquid']
print(f'After deleting Recipe base: {chai_recipe}')

print(f'Is sugar in the order? {'sugar' in chai_order}')


chai_order= dict(type='Masala Chai', size='Medium', sugar=1)
# print(f'Order details (keys): {chai_order.keys()}')
# print(f'Order details (values): {chai_order.values()}')
# print(f'Order details (items): {chai_order.items()}')

last_item = chai_order.popitem()
print(f'Remove last itme: {last_item}')

extra_spices = {'cardamom':'crushed','ginger':'sliced'}
chai_recipe.update(extra_spices)
print(f'Updated chai recipe: {chai_recipe}')

chia_size = chai_order['size']
print(f' chai size: {chia_size}')

customer_note = chai_order.get('customer note', 'NO Note')
print(f'Customer note: {customer_note}')
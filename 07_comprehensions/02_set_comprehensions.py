# set comprehensions

favourite_chais = [
    "Masala Chai",
    "Green Tea",
    "Masala Chai",
    "Lemon Tea",
    "Green Tea",
    "Elaichi Chai"
]

unique_chai = {chai for chai in favourite_chais}
# unique_chai = {chai for chai in favourite_chais if len(chai) > 8}
# unique_chai = {chai for chai in favourite_chais if len(chai) < 8}

print(unique_chai)

recipes = {
    "Masala Chia": ['ginger', 'cardamom', 'clove'],
    "Elachie Chia": ['cardamom', 'milk'],
    "Spicy Chia": ['ginger', 'black pepper', 'clove'],
}

# unique_spices = {_____ for ingredients in recipes.values() for spice in ingredients}
unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)
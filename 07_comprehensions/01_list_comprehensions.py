# List Comprehensions

menu = [
    "Masala Chai",
    "Iced Lemon Tea",
    "Green Tea",
    "Iced Peach Tea",
    "Ginger Tea",
]

# [expression for item in iterable of condition]

iced_tea = [tea for tea in menu if 'Iced' in tea]
# iced_tea = [my_tea for tea in menu if 'Iced' in tea]
# iced_tea = [my_tea for my_tea in menu if 'Iced' in tea]
tea_len = [my_tea for my_tea in menu if len(my_tea) > 10]
print(iced_tea)
print(tea_len)
# Output 
# ['Iced Lemon Tea', 'Iced Peach Tea']
# ['Masala Chai', 'Iced Lemon Tea', 'Iced Peach Tea']
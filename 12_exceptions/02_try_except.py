chai_menu = {
    "Masala": 3.00,
    "Ginger": 3.50,
}

# chai_menu['Eleichi']
try:
    chai_menu['Eleichi']
except KeyError:
    print("That type of chai is not available.")

print("Program continues...")# The above line would raise a KeyError since 'Eleichi' is not in the chai_menu dictionary. 
# The try-except block catches the KeyError and prints a message instead of crashing the program.

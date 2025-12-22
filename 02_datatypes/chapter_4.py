is_boiling = True
stri_count = 5
total_actions = stri_count + is_boiling # upcasting
print(f'Total actions: {total_actions}')

milk_present = 0 # no milk
print(f'IS there milk? {bool(milk_present)}')

milk_present = None # no milk
print(f'IS there milk? {bool(milk_present)}')

water_hot = True
tea_add = False

can_server = water_hot and tea_add
print(f'Can server Chai? {can_server}')
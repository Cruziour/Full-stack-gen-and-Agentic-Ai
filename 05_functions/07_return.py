def make_chai():
    # return 'Here is your Masala Chai'
    print('Here is your masala chai')

return_value = make_chai()
print(return_value)
#  None -> Implicitly returns none 

def sold_cups():
    return 120

total = sold_cups()
print(total)

def chai_status(cups_left):
    if cups_left == 0:
        return 'Sorry, chai over'
    return 'Chai is ready'

print(chai_status(5))

def chai_report():
    return 100, 20 # sold, remaining
    # return 100, 20, 30 # sold, remaining

sold, remaining, _ = chai_report()
# sold, remaining, _ = chai_report() # avoiding this 
print(f'Sold: {sold}, Remaining: {remaining}')

def chai_flavor(flavor='masala'):
    # chai='ginger'
    """Return the flavor of chai."""
    chai='ginger'
    return flavor

print(chai_flavor.__doc__)
print(chai_flavor.__name__)
print(chai_flavor.__annotate__)
help(len)

def generate_bill(chai=0, samosa=0):
    """
    Docstring for generate_bill
    
    :param chai: Number of chai cups (1) rupees each chai
    :param samosa: Number od samosa (15 rupees for each)
    :return: (total amount, thank you message)
    """
    total = chai*10 + samosa*15
    return total, 'Thank you for visiting.'

print(generate_bill.__doc__)
print(generate_bill.__name__)

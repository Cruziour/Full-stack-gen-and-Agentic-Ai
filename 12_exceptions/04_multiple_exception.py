def process_order(item, quantity):
    try:
        price = {"masala": 20}[item]
        cost = price * quantity
        print(f"Total cost for {quantity} {item}(s): {cost}")
    except KeyError:
        print(f"Error: '{item}' is not available in the menu.")
    except TypeError:
        print("Error: Quantity must be a number.")

# Example usage
process_order("ginger", 3)     # KeyError case
process_order("masala", 'two')      # Valid case
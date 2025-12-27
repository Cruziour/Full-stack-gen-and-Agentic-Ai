class OutOfIngredientsError(Exception):
    """Custom exception raised when ingredients are out of stock."""
    pass

def make_tea(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngredientsError("Cannot make tea: Out of milk or sugar.")
    print("Tea is ready!")

make_tea(0, 2)  # This will raise the custom exception
# Output:
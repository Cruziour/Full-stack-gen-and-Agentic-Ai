class InvalidChaiError(Exception):
    """Raised when the chai type is invalid."""
    pass

def bill(flavor, cups):
    menu = {
        "vanilla": 4.00,
        "chocolate": 4.50,
        "matcha": 5.00,
        "chai": 3.50
    }
    try:
        if flavor not in menu:
            raise InvalidChaiError(f"Invalid chai flavor: {flavor}")
        if not isinstance(cups, int) or cups <= 0:
            raise TypeError("Number of cups must be a positive integer.")
        total = menu[flavor] * cups
        print(f"Your total for {cups} cup(s) of {flavor} chai is: ${total:.2f}")
    except InvalidChaiError as e:
        print(e)
    except TypeError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("Thank you for visiting our chai shop!")

# Example usage:
bill("vanilla", 2)  # Valid order
bill("strawberry", 'Two')  # Invalid flavor
bill("chai", -1)  # Invalid number of cups
bill("matcha", 3)  # Valid order

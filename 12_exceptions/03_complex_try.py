def serve_chai(flavor):
    try:
        print(f"Serving {flavor} chai.")
        # Simulate an error for a specific flavor
        if flavor == 'unknown':
            raise ValueError("Unknown chai flavor!")
    except ValueError as ve:
        print(f"Error: {ve}")
    else:
        print(f"{flavor} chai served successfully.")
    finally:
        print("Thank you for visiting our chai shop!")

# Test the function with different flavors
serve_chai("Masala")
serve_chai("unknown")
# In this code, we define a function `serve_chai` that attempts to serve a specified flavor of chai. If the flavor is 'unknown', it raises a ValueError.
# The try block contains the code
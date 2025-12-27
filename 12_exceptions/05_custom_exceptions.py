def brew_chai(flavor):
    if flavor not in ["masala", "ginger", "cardamom"]:
        raise ValueError(f"Unsupported flavor: {flavor}....")
    print(f"Brewing a cup of {flavor} chai!")


brew_chai("vanilla")# Output:
# Traceback (most recent call last):
# file = open("order.txt", "w")
# try:
#     file.write("1x Coffee\n2x Donut\n")
# finally:
#     file.close()

with open("order.txt", "w") as file:
    file.write("1x Coffee\n2x Donut\n")
# The 'with' statement automatically handles closing the file.
# After the 'with' block, the file is automatically closed.
# You can verify that the file is closed by trying to write to it again:
# file.write("This will raise an error because the file is closed.")
# Uncommenting the line below will raise a ValueError
# print(file.closed)  # This will print True, indicating the file is closed.
# The 'with' statement is preferred for file handling as it ensures proper resource management.

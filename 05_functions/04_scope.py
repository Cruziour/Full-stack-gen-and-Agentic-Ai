def serve_chai():
    chai_type = 'Masala Chai' # local scope
    print(f'Inside function {chai_type}')

chai_type = 'lemon'
serve_chai()
print(f'Outside funtion: {chai_type}')

def chai_counter():
    chai_order = 'Lemon' # Enclosing scope
    def print_order():
        chai_order = 'Ginger'
        print(f'Inner: {chai_order}')
    print_order()
    print(f'Outer: {chai_order}')

chai_order = 'Tusli' # Global scope
chai_counter()
print(f'Global: {chai_order}')
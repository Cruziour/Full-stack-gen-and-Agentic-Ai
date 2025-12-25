class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data['tea_type'],        
            order_data['sweetness'],        
            order_data['size'],        
        )
    
    @classmethod
    def from_string(cls, order_data):
        tea_type, sweetness, size = order_data.split("-")
        return cls(tea_type, sweetness, size)
    

class ChaiUtils:
    @staticmethod
    def is_valid_size(size): 
        return size in ['Small','Medium','Large']

print(ChaiUtils.is_valid_size("Medium"))

order_one = ChaiOrder.from_dict({'tea_type':"Masala","sweetness":"medium","size":"Large"})
order_two = ChaiOrder.from_string('Ginger-Low-Small')
order_three = ChaiOrder('Lemon',"High","Medium")

# print(f"Order two: {order_two}")
# print(f"Order one: {order_one}")
# print(f"Order three: {order_three}")
print(f"Order two: {order_two.__dict__}")
print(f"Order one: {order_one.__dict__}")
print(f"Order three: {order_three.__dict__}")

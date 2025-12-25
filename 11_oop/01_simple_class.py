class Chai:
    pass

class ChaiTime:
    pass


print(type(Chai))

ginger_tea = Chai() # create object and class is also a object 

print(type(ginger_tea))
print(type(ginger_tea) is Chai)
print(type(ginger_tea) is ChaiTime)
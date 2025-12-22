# def update_order():
#     chai_type = 'Elaichi'
#     def kitchen():
#         nonlocal chai_type
#         chai_type = 'Kesar'
#     kitchen()
#     print(f'After kitchen update: {chai_type}')

# update_order()

## Global scope
chai_type = 'Pain'

def front_desk():
    def kitchen():
        global chai_type
        # nonlocal chai_type
        chai_type= 'Irnai'
    kitchen()

front_desk()
print(f'Final global chai: {chai_type}')
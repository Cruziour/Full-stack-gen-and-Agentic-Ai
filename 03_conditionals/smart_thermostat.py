# device_status = 'active'
# temperature = 38

# if device_status == 'active':
#     if temperature > 35:
#         print(f'High temperature alert!')
#     else:
#         print(f'Temperature is normal.')
# else:
#     print(f'Device is offline')

# order_amount = int(input('Enter the order amount: '))
# # print(f'Order amount: {type(order_amount)}')

# delivery_fees = 0 if order_amount > 300 else 30

# print(f'Delivery fees is {delivery_fees}')

seat_type = input('Enter seat type (Sleeper/ AC/ General/ Luxury): ').lower()

match seat_type:
    case 'sleeper':
        print(f'Sleeper - No AC, beds available')
    case 'ac':
        print(f'AC - Air Conditioned, comfy ride')
    case 'general':
        print(f'General - Cheapest option, no reservation')
    case 'luxury':
        print(f'Luxury - Premium seats with meals')
    case _:
        print(f'Invaild seat type')



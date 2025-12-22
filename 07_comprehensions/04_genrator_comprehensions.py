# Genrator comprehensions

daily_sales = [5,10,12,7,3,9,15,8]

total_cups = sum(sale for sale in daily_sales if sale > 5)
# total_cups = [sale for sale in daily_sales if sale > 5]

print(total_cups)

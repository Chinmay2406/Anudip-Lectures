# Program 4: Calculate net amount after discounts for toys
product_code = int(input("Enter the product code (1 for Battery, 2 for Key-based, 3 for Electrical): "))
order_value = float(input("Enter the order amount: "))

if product_code == 1:  # Battery-based toys
    if order_value > 1000:
        discount = 10 / 100 * order_value
    else:
        discount = 0
elif product_code == 2:  # Key-based toys
    if order_value > 100:
        discount = 5 / 100 * order_value
    else:
        discount = 0
elif product_code == 3:  # Electrical charging-based toys
    if order_value > 500:
        discount = 10 / 100 * order_value
    else:
        discount = 0
else:
    print("Invalid product code!")
    discount = 0

net_amount = order_value - discount
print(f"The net amount after discount is Rs. {net_amount:.2f}.")

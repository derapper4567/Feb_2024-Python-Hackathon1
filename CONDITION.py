def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        discount_amount = (discount_percent / 100) * price
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt the user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate and print the final price after applying the discount
final_price = calculate_discount(original_price, discount_percentage)
if final_price == original_price:
    print(f"No discount applied. Original price: ${final_price}")
else:
    print(f"Final price after applying a {discount_percentage}% discount: ${final_price}")
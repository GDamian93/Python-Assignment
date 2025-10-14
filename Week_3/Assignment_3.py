# _________________________ WEEK 3 - ASSIGNMENT   _________________________

# Calculate the discounted price
def calculate_discounted_price(price, discount_percent):
    discount = (discount_percent / 100) * price
    return price - discount

print("================================================================")
print("=                   DISCOUNT CALCULATOR                        =")
print("================================================================")


# Get user input
original_price = float(input("= Enter the original price: "))
discount_percent = float(input("= Enter the discount percentage: "))
print("================================================================")

# Apply discount if eligible
if discount_percent >= 20:
    final_price = calculate_discounted_price(original_price, discount_percent)
    print(f"= Discount applied: {discount_percent}%")
    print(f"= Original price: ${original_price: .2f}")
    print(f"= Final price after discount: ${final_price: .2f}")
else:
    print(f"= No discount applied (only {discount_percent}%).")
    print(f"= Final price: ${original_price: .2f}")
print("================================================================")
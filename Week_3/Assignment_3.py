# _________________________ WEEK 3 ASSIGNMENT   _________________________

# Calculate the discounted price
def calculate_discount(price, discount_percent):
    discount = (discount_percent / 100) * price
    return price - discount

# Get user input for price and discount percentage.
price = float(input("Enter with the price: "))
discount_percent = float(input("Enter with the discount percentage: "))

# Check if the discount percentage is 20% or more
# If so, apply the discount and print the discounted price, otherwise print the original price.

if discount_percent >= 20:
    discounted_price = calculate_discount(price, discount_percent)
    print("Price with discount: ", discounted_price)
else:
    print("Price with discount: ", price)
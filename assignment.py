# Creating a function
def calculate_discount(price, discount_percentage):
    # Calculate the discount amount
    discount_amount = price * (discount_percentage / 100)
    
    # Calculate the final price after discount
    final_price = price - discount_amount
    return final_price

#prompting the user 
price = int(input("Enter the original price: "))
discount_percentage = int(input("Enter the discount percentage: "))

#adding the conditions
if discount_percentage < 20:
    final_price = price
    print(f"The final price is: {price:.2f}")

else:
    final_price = calculate_discount(price, discount_percentage)
    print(f"The final price after a {discount_percentage}% discount is: {final_price:.2f}")



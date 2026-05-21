# Product Price Calculator with Discount and GST

# Get product price
price = float(input("Enter product price: "))

# Get discount percentage
discount = float(input("Enter discount percentage: "))
# Calculate discount amount
discount_amount = (price * discount) / 100

# Price after discount
discounted_price = price - discount_amount

# Get GST percentage
gst = float(input("Enter GST percentage: "))

# Calculate GST amount
gst_amount = (discounted_price * gst) / 100

# Final price after adding GST
final_price = discounted_price + gst_amount

# Display results
print("\n----- BILL DETAILS -----")
print("Original Price:", price)
print("Discount Amount:", discount_amount)
print("Price After Discount:", discounted_price)
print("GST Amount:", gst_amount)
print("Final Price to Pay:", final_price)
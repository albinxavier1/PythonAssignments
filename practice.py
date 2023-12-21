quantity = int(input("Enter the quantity of the products : "))

total_price = quantity*100
if quantity > 1000:
    discount_price = total_price * 0.1
    final_price = total_price - discount_price
    print("Thank you for your purchase")
    print("Your final price after 10% discount is : " , final_price)
else :
    print("Thank you for your purchase")
    print("Your final price is : " , total_price)
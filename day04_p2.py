product=input("Enter item to add to cart: ")
quantity=input("Enter quantity: ")
price=input("Enter price: ")

cart= [{ "item": product, "quantity": int(quantity) , "price": float(price) , "total": float(quantity) * float(price) }]
for item in cart:
    cart_items = input("Do you want to add another item? (yes/no): ")
    while cart_items.lower()=="yes":
        product=input("Enter item to add to cart: ")
        quantity=input("Enter quantity: ")
        price=input("Enter price: ")
        cart.append({ "item": product, "quantity": int(quantity) , "price": float(price) , "total": float(quantity) * float(price) })
        cart_items = input("Do you want to add another item? (yes/no): ")
        print("Thank you for shopping with us.")
    
    break
 
remove_item = input("Do you want to remove an item from the cart? (yes/no): ")
while remove_item.lower() == "yes":
    item_to_remove = input("Enter the name of the item to remove: ")
    cart = [item for item in cart if item["item"] != item_to_remove]
    print(f"Item {item_to_remove} has been removed from the cart.")
    remove_item = input("Do you want to remove another item? (yes/no): ")
    if remove_item.lower() == "no": print("Thank you for shopping with us.")

last_items = cart[-3:]  # Get the last three items added to the cart
print("Last three items added to the cart:")
for item in last_items:
    print(f" - {item['item']}: {item['quantity']} x ${item['price']:.2f} = ${item['total']:.2f}")   
total_price = sum(item["total"] for item in cart)
print(cart)
print("Total price:", total_price)
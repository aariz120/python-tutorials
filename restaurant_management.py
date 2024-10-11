menu={
    "Coffee":2,
    "Pasta":3,
    "Pizza":5,
    "Burger":7,
    "chicken":11,
}


print(
    """
    Welcome to Aariz's Restaurant.Please Order Food!
    
    Coffee:$2
    Pasta:$3
    Pizza:$5
    Burger:$7
    Chicken:$10
    
    """
)

total_price=0

item1=input("Enter the name of the item you want to order:")
if item1 in menu:
    total_price+=menu[item1]
    print(f"You ordered {item1}.Your total order amount is ${total_price}")
    
else:
    print("Invalid item.Please order something from the Menu.")
    

another_order=input("Do you wants to add another item?(Yes/No): ").lower()
if another_order == "yes":
    item2=input("Enter the name of the  2nd item you want to order:")
    if item2 in menu:
        total_price+=menu[item2]
        print(f"You ordered {item2}.Your total order amount is ${total_price}")
        
    else:
        print("Invalid item.Please order something from the Menu.")


print(f"Your Total amount is ${total_price}.Thank you !")
        
    
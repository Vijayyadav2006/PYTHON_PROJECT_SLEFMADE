#Defining Dictonary

Menu = {"Pizza" :3,
        "Pizza" :3,
        "pastry":7,
        "Coffie":9,
        "Chilli Soup":15
        
}

print(" V I J Y E H H O T E L")
print("Pizza :$3\n Pizza :$3\n pastry:$7\n Coffie:$9\n Chilli Soup$:15")

Order = 0 #insilation of Order Amount

Item_1=input("Order Something From Menu")
if Item_1 in Menu:
    Order +=Menu[Item_1]
    print(f"Ordered  {Item_1} You're Items")
else:
    print("Can't Available this goods or Items in Menu {Item_1} Select ")
    
Second_Order=input(" else Want [Yes/No]:")
if Second_Order == "Yes":
    Item_2=input("Enter Something Wants To aaded=")
    if Item_2 in Menu:
        Order +=Menu[Item_2]
        print("New Items {Second_Order} added")
    else:
        print(f"This Items {Second_Order} Not Available")
else:
    print(f"Ordered Menu Items {Item_1}")
    
print(Order)
    


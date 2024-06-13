menu ={
    "Burger":400,
    "Pizza":600,
    "Pasta":500,
    "Roll":250,
    "Sandwich":300,
    "Handi":1200,
    "Biryani":800,
    "Rice":200,
    "Noodles":300,
    "Soup":100,
    "Salad":150,
    "Bread":50,
    "Drink":100,
    "Dessert":200,
}
print("Welcome to Our Hotel ")
for item, price in menu.items():
      print(item, price)

order_tot=0
item1=input("Please input order =")
if item1 in menu:
    order_tot+=menu[item1]
else :
    print("invalid order")
order_2=input("Any thing else ? (Yes/No)")
if order_2=="Yes":
    item_2=input("Select another one!! ")
    if item_2 in menu:
        order_tot+=menu[item_2]
        print("order is added ")
    else:
         print("invalid order")
print(f"the total amount is {order_tot}")

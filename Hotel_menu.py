# DEFINE THE OF RESTAURANT

menu = {
    'PIZZA':99,
    'PASTA':49,
    'BURGER':149,
    'SALAD':69,
    'COFFEE':39,
    'TEA':25,
    }

# GREET
print("WELCOME TO ODIA_RESTAURANT")
print("Menu :")
print(" PIZZA: Rs99\n PASTA: Rs49\n BURGER: Rs149\n SALAD: Rs69\n COFFEE: Rs\n TEA: Rs25\n")

order_total=0

item_1 = input("Enter the name of item you want to order :-")
if item_1 in menu:
    order_total = order_total + menu[item_1]
    print(f"Your item {item_1} has been added to your order.")
else:
    print(f"Order item {item_1} is not avaialable yet. ")

another_order = input("Do you want to add another item? (Yes/No).")
if another_order == 'Yes':
    item_2 = input("Enter the second item :-")
    if item_2 in menu:
        order_total = order_total + menu[item_2]
        print(f"Your item {item_2} has been added to your order.")
    else:
        print(f"Order item {item_2} is not avaialable yet. ")

print(f"The total amount of item to pay is {order_total}.")


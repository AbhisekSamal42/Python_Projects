rent = int(input("Enter your hostel/flat rent = "))
food = int(input("Enter the amount of food order = "))
electricity_spend = int(input("Enter the amount of electicity spend = "))
charge_per_unit = int(input("Enter the charge per unit = "))

persons = int(input("Enter the number of Persons living in room/flat = "))

total_bill= electricity_spend * charge_per_unit

output = (food+rent+total_bill)//persons
print(f"Each person will pay Rs{output}")
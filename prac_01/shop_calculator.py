total = 0
flag = "true"
while flag != "false":
    number_of_items = int(input("Number of items : "))
    if number_of_items > 0:
        for i in range(0,number_of_items):
            price_of_item = float(input("Price of item: "))
            total += price_of_item
        if total > 100:
            total = total - (total * 0.1)
            flag = "false"
        else:
            flag = "false"
        print(f"Total price for {number_of_items} items is {total}")
    else:
        print("Invalid number of items!")
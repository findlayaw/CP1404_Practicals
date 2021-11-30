totalCost = 0
items = int(input("Number of items: "))
while items < 0:
    print("Invalid number")
    items = int(input("Number of items: "))
for i in range(items):
    itemPrice = float(input("Price of item: "))
    totalCost = totalCost + itemPrice
if totalCost > 100:
    totalCost = totalCost * 0.9
print(f"Total price for {items} items is ${totalCost:.2f}")

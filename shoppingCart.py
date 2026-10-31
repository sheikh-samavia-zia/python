products = ["Laptop", "Mouse", "Keyboard", "Headphones", "Monitor"]
prices = [85000, 1500, 4500, 7000, 35000]
stock = [3, 10, 5, 0, 2]

total = 0
bought = []

name1 = input("Enter 1st product name: ")
qt1 = int(input("Enter quantity: "))

if name1 in products:
    i = products.index(name1)
    if stock[i] == 0:
        print(name1, "is OUT OF STOCK")
    elif qt1 > stock[i]:
        print("Only", stock[i], "available")
    else:
        total = total + (prices[i] * qt1)
        stock[i] = stock[i] - qt1
        bought.append(name1)
        print(name1, "added")
else:
    print(name1, "not found")

name2 = input("Enter 2nd product name: ")
qt2 = int(input("Enter quantity: "))

if name2 in products:
    i = products.index(name2)
    if stock[i] == 0:
        print(name2, "is OUT OF STOCK")
    elif qt2 > stock[i]:
        print("Only", stock[i], "available")
    else:
        total = total + (prices[i] * qt2)
        stock[i] = stock[i] - qt2
        bought.append(name2)
        print(name2, "added")
else:
    print(name2, "not found")

name3 = input("Enter product 3 name: ")
qt3 = int(input("Enter quantity: "))

if name3 in products:
    i = products.index(name3)
    if stock[i] == 0:
        print(name3, "is OUT OF STOCK")
    elif qty3 > stock[i]:
        print("Only", stock[i], "available")
    else:
        total = total + (prices[i] * qt3)
        stock[i] = stock[i] - qt3
        bought.append(name3)
        print(name3, "added")
else:
    print(name3, "not found")

if total > 100000:
    total = total - (total * 0.20)
elif total > 50000:
    total = total - (total * 0.10)
elif total > 20000:
    total = total - (total * 0.05)

if "Laptop" in bought:
    if "Mouse" in bought:
        total = total - (total * 0.05)
        print("Laptop + Mouse combo discount applied")

if total > 70000:
    print("Free delivery!")
else:
    total = total + 500

print("\n----- RECEIPT -----")
print("Items bought:", bought)
print("Final Bill: Rs.", total)
print("Stock left:", stock)

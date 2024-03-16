

amazon_cart = [["Watch",5000],["Phone",10000],["Laptop",50000]]
total_cost = amazon_cart[0][1]+amazon_cart[1][1]+amazon_cart[2][1]

#Using For loop

total_cost = 0

for i in amazon_cart:
    total_cost += i[1]

print(total_cost)

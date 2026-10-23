no_of_items = int (input("Enter number of items:"))
if no_of_items <= 10:
    cost_per_item = 120
elif no_of_items > 10 and no_of_items <=99:
    cost_per_item = 85
else:
    cost_per_item = 75
total_cost = no_of_items * cost_per_item
print("Total cost is:", total_cost)
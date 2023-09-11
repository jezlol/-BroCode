fruits = ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrot", "onion", "boccoli"]
meats = ["cow", "chicken", "turkey"]

groceries = [fruits, vegetables, meats]

# print(groceries[0][3])
for collections in groceries:
    for food in collections:
        print(food, end=" ")
    print()
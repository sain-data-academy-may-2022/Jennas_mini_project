import csv

with open('new_orders.csv', 'r') as file:
        read = csv.DictReader(file)
        list_name = list(read)

print(list_name)


import csv
# from Food_dict import Food_dict

# titles = ['ID','Name', 'Description', 'Price']
# with open('food.csv', 'w') as csvfile:
#         writer = csv.DictWriter(csvfile, fieldnames = titles)
#         writer.writeheader()
#         writer.writerows(Food_dict)


# with open("Food.csv", "r") as f:
#         csv_reader = csv.DictReader(f)
#         food_list = list(csv_reader)


# new_food = {5, 'Pie', 'Steak', '£100 (only fair as you are being hard work)'}
# with open('food.csv', 'a', newline='') as f:
#         writer = csv.writer(f)
#         writer.writerow(new_food)

# def csv_open(csv_name, list_name):
#     with open(f"{csv_name}.csv", "r") as f:
#         csv_reader = csv.DictReader(f)
#         list_name = list(csv_reader)
#         print(list_name)

# # with open("courier.csv", "r") as f:
# #     reader = csv.DictReader(f)
# #     dict_list = []
# #     for line in reader:
# #         dict_list.append(line)
# #     print(dict_list)


# def update_csv(csv_name, new_list):
#     with open(F'{csv_name}.csv', 'w') as f:
#         writer = csv.writer(f)
#         writer.writerow(new_list)

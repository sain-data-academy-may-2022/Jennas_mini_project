from typing import List, Dict
class Food:
    def __init__(self, Index : str, Name: int, Description: str, Price: int):
        self.Index = Index
        self.Food_Name =  Name
        self.Description = Description
        self.Price = Price
        print("Item created")

ChocolateCake = Food(1,"Chocolate McChoclate Cake", 'Cake that is chocolate, what more do you need to know', '£20')
Salad = Food(1,'Salad','A boring choice for a boring person','£666')
Hot_Chocolate = Food(2,'Hot Chocolate','With Coconut milk to bring that warm chocolately cozyness','£10')
Costalot_Special = Food(3,"Costa'lot Special","Two slices of toast with jam, but we'll charge the cost of a whole loaf",'£12')
Vegan_Pizza = Food(4, 'Vegan Pepperoni Pizza' ,"With lots of meat and chesee from animals, just what you Vegan's want right?",'£23')



class Courier:
    def __init__(self, Name: str, Number: int):
        self.Name = Name
        self.Number=  Number
        print("Courier created")

    def add_1(self):
        self.Number += 1


class Order:
    def __init__(self, customer_name: str,customer_address,customer_phone: int,status: str,food: str,courier: str):
        self.customer_name = customer_name
        self.customer_address =  customer_address
        self.customer_phone = customer_phone
        self.status = status
        self.food = food
        self.courier = courier
        print("Order created")
    
    def print_nicely():
        for name


def print_cars (cars: List[Dict[str, str]]):
    for car in cars:
        print(f"Brand: {car['brand']}, Colour: {car['color']}" )


cars = [{"brand": "BMW", "colour": "Blue"},
{"brand": "Volvom ", "colour": "Red"}]

print(cars)

Courier()
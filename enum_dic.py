product = {
    '0' : '0. Imma head out ',
    '1' : '1. See the menu!!!!',
    '2' : "2. I'm a princess make something special?",
    '3' : '3. Close, but you want to mix it up a litte?',
    '4' : '4. Get rid of that',
    '5' : '5. Access the order system, only if you have placed one though!'
}

food_order = {
   "Chocolate McChocolate Cake" :"Cake that is chocolate, what more do you need to know",
   "2" : "Salad: A boring choice for a boring person",
   "3" : "Hot Chocolate: With Coconut milk to bring that warm chocolately cozyness",
   "4" : "Costa'lot Special: Basically just two slices of toast with jam and no butter, but we've called it special so will charge the cost of a whole loaf"
}

order1 = {
    "customer_name" : "Jenna",
    "customer_address" :"Thorpe" ,
    "customer_phone" : "07999999999",
    "status" : "PREPARING",
}

order2 = {
    "customer_name" : "",
    "customer_address" :"" ,
    "customer_phone" : "",
    "status" : "PREPARING",
}

orders = [order1,order2]


def show_food_options(): 
       for key, value in enumerate(food_order):
                print(value)



show_food_options()
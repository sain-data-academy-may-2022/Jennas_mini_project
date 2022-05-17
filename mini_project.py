Product = {
'0' : 'Main Menu',
'1' : 'Food and Drinks', 
'2' : 'Create your own order',
'3' : 'Change an existing product',
'4' : 'Ask for a product to be removed',}

Food_Drinks = {
'0' : 'chocolate cake',
'1' : 'salad',
'2' : 'hot chocolate', 
'3' : 'orange juice',
} 

# Connor Code - always back to main menu - thank you Connor!!! ^_^
while(True): 


    # def return_to_product_menu():
    #     user_return = input('Press enter to return to the main menu and continue.')
    #     if user_return == "":
    #               print('Please choose between options 0 - 4')
    #     for key, value in Product.items():
    #         print(key, value) 
    #         pass
    #     else:
    #         print("Invalid input. Press enter to continue.")
    #         return_to_product_menu()
    


#step 1 in the task is print main menu and task 2 is exit app
    Main_Menu = input("J's popup app - welcome! To exit app choose 0, to see our options choose 1:" )
    if Main_Menu == "0":
        print('Exiting app, see you next time!')
        break

#main menu enter first dictionary 
    elif Main_Menu == "1":
        print('Please choose between options 0 - 4')
        for key, value in Product.items():
            print(key, value)  
      
     #first dictionay - back to main menu    
        Product_menu = input()
        if Product_menu == "0":
            print('Heading back to the main menu')

      #enter second dictionary shows food and drink       
        elif Product_menu == "1": 
            for key, value in Food_Drinks.items():
                print(key, value)
            my_order = input("What would you like?")
            print(f'Thank you, your order for {Food_Drinks [my_order]} has been placed successfully. Goodbye!')
            break
                    
    #create new product 
        elif Product_menu == "2":
            Custom = input("Sorry you don't like our selection, please add what you would like instead... ")
            Food_Drinks[4] = Custom
            for key, value in Food_Drinks.items():
                print(key, value)
            my_order = int (input("What would you like?"))
            print(f"Thank you, we've update our menu for future and your order for {Food_Drinks[my_order]} has been placed successfully. Goodbye!")
            break  
            
    #update 
        elif Product_menu == '3':
                print('Please choose between options 0 - 3')
                for key, value in Food_Drinks.items():
                    print(key, value)
                Change = input()
                Change2 = input("What would like to see instead?")
                Food_Drinks[Change] = Change2
 
                my_order = input("What would you like?")
                print(f'Thank you for updating an item, your order for {Food_Drinks [my_order]} has been placed successfully. Goodbye!')
                break
        
    #remove a product 
        elif Product_menu == '4':
                print('Please choose between options 0 - 3')
                for key, value in Food_Drinks.items():
                    print(key, value)
                Remove = input()
                del Food_Drinks[Remove] 
                for key, value in Food_Drinks.items():
                    print(key, value)
                print("Thank you for your for your feedback, that product has been removed!")
                break


        







       


    








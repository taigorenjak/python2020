shopping_basket = ()  #this is an empty dictionary                                                                                                                                                                                                                              (key:volume)e.g ("apples" : 5, "bananas"             
                      #(key:value) e.g ("apples" : 5, "bananas" : 3)
print("""
 shopping bask________________________

1: add item
2: remove ite3: view basket
0: exit program

""")

option = int(input("enter an option: "))       
while option !=0:
    if option == 1:
        item =input("enter an item: ")
        qnty = int(input("enter the quantity: "))
        shopping_basket[item] = qnty
        
    elif option == 2:
        item = input("enter an item: ")
        del(shopping_basket[item])
            
    elif option == 3:
        for item in shopping_basket:
            print(item,":",shopping_basket[item])
            
    elif option != 0:
        print("you didn't enter a valid number.")

        option = int(input("/n/nenter an option: "))
                         
    else:
        print("shopping basket program closed. ")

# Python Project: Cursed Antiques
# Focus: control flow, branching logic, and user interaction

print("Welcome to The Cursed Antique Shop!")

cursed_antiques = ["Talisman",
                   "Monkeys Paw",
                   "Cursed Mirror",
                   "Haunted Painting",
                   "Voodoo Doll",
                   "Crystal Ball",
                   "Cursed Locket",
                   "Ancient Amulet",
                   "Phantom Clock",
                   "Dorian Gray's Portrait",
                   "Cursed Ring"]

shopping_cart = []

# DO NOT CHANGE THE CODE ABOVE HERE
# YOUR CODE BELOW HERE
while True: # loop for the message below
    user_input = input("""\nWhat would you like to do?
    - Buy an item (enter 'buy')
    - Remove antique from shopping cart (enter 'remove')
    - Sort antiques (enter 'sort')
    - List items (enter 'list')
    - Quit (enter 'quit'
    Option: """)

    if user_input == "quit": # user wants to exit
        print("\n\nThank you for visiting the Cursed Antiques Shop!") # goodbye message with 2 \n to maych desried output expectation
        break # breaks the loop and exits
    
    elif user_input == "buy": # user wants to buy from the shop!
        buy_option = input("Would you like to buy the antique by name or by index? (Enter 'name' or 'index') ") # options on how the user would like to purchase

        if buy_option == "name": # first option, by name
            item_name = input("Which item would you like to buy? ") # get item name

            if item_name in cursed_antiques: # check if provided name is in the list
                cursed_antiques.remove(item_name) # remove item from inventory list
                shopping_cart.append(item_name) # add item to cart
                print(f"{item_name} was removed from the inventory and added to the shopping cart.") # item is in the list!

            else: # item is not in the list
                print("That item is not available.")
        
        elif buy_option == "index": # second option, by index

            try:
                item_index = int(input("Which item would you like to buy? ")) # user enter 1, 2, 3, ...
                item_name = cursed_antiques.pop(item_index - 1) # remove item from inventory list if passed a valid index, used - 1 convert from 0-based to 1-based
                shopping_cart.append(item_name) # add item to cart
                print(f"{item_name} was removed from the inventory and added to the shopping cart.") # sucess! 

            except (ValueError, IndexError): # invalid input -not a number- or index # is out of range
                print("That item is not available.")
        
        else: # invalid selection
            print("Sorry I didn't understand that.")

    elif user_input == "sort": # user want to sort the list
        sort_in = input("Would you like to sort the antiques in reverse alphabetical order (y/n)? ")

        if sort_in == "y": # user wants to reverse sort the list!
            cursed_antiques.sort() # sort existing list a - z
            cursed_antiques.reverse # re-sort a - z to z - a
            print("Antiques sorted in reverse alphabetical order.")

        elif sort_in == "n": # user wants to sort the list a - z!
            cursed_antiques.sort() # sort existing list a - z
            print("Antiques sorted in alphabetical order.")

        else: # invalid selection
            print("Sorry I didn't understand that.")

    elif user_input == "list": # user wants to view the list
        list_choice = input("Would you like to view your shopping cart or available antiques (s/a)? ") # choose between 2 lists, cart list or available items list

        if list_choice == "s":
            shopping_cart.sort() # sort the list to match expectations in desired outpout 2.5.1
                
            for index, cart_item in enumerate(shopping_cart): # number the list
                print(f"{index + 1}. {cart_item}") # + 1 to make numbering match expectations and . to match expected style and format

        elif list_choice == "a": # user wants to view available antiques
            cursed_antiques.sort() # sort the list to match expectations in desired outpout 2.5.1

            for index, antique in enumerate(cursed_antiques): # number the list
                print(f"{index + 1}. {antique}") # + 1 to make numbering match expectations and . to match expected style and format

        else: # input is not 's' or 'a'
            print("Sorry I didn't understand that.")

    elif user_input == "remove": # user wants to remove an item from cart
        item_remove = input("Which item would you like to remove from your shopping cart? ")

        try:
            shopping_cart.remove(item_remove) # remove item from cart list if exists

            if item_remove not in cursed_antiques: # check for duplicates
                cursed_antiques.append(item_remove) # put back in available items

            print(f"{item_remove} was removed from the shopping cart.")

        except ValueError: # item not in cart
            print(f"{item_remove} is not in the shopping cart.")

    else: # invalid choice
        print("Sorry I didn't understand that try again.")
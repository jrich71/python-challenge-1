# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# -------------------------Welcome to the Food Truck------------------------------

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered

order = []

# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous loop
place_order = True
while place_order:

# ------------------------Present the Menu Options------------------------------

    # Ask the customer from which menu category they want to order, the actual request (input) comes later
    print("From which menu would you like to order? ")

    # Create a variable "i" for the menu item number, which will be created in the 'global frame'
    i = 1

    # Create a dictionary to store the menu item keys in the 'global frame' for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level dictionary items in menu).
    # This assigns the menu item key (starting with the first) to "key" in the 'global frame'
    for key in menu.keys():

        # Print the value in "i" with the corresponding "key"
        print(f"{i}: {key}")

        # Store the menu category key and its associated menu item number ("i") in the "menu_items" dict
        menu_items[i] = key

        # Add 1 to the menu item number, this increments "i" to go through another loop (if applicable)
        i += 1

    print(menu_items) # This prints all items in the dictionary, "menu_items"

# ---Get the User to Select Option(s) to Present the Related Menu Category's Sub-menu Items, and Prices---
    
    # Get the customer's input by asking for a number, we want an int
    menu_category = input("Enter the menu number: ")

    # Check if the customer's input is a number
    if menu_category.isdigit():

        # Check if the customer's input is a valid option
        if int(menu_category) in menu_items.keys():

            # Save the menu category name to a variable
            menu_category_name = menu_items[int(menu_category)]

            # Print out the menu category name they selected
            print(f"You selected {menu_category_name}")

            # Print out the sub-menu options from the menu_category_name
            print(f"What {menu_category_name} item would you like to order?")
            
            # Create a new number to track sub-menu options within the 'global frame'
            i = 1

            # Create a new dict in the 'global frame', this overwrites the previous "menu_items" dict
            menu_items = {}

            # Print the list header
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")

            # Get the sub-menu key and its value associated with menu and menu category name
            for key, value in menu[menu_category_name].items():

                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:

                    # If the value is a dict, then print out using the following format per line item
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                # If the value is NOT a dict, then print out using the following format per line item
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1

            # 2. Ask customer to select the menu item number located in the sub-menu
            menu_selection = input("Type the number of your selection: ")

            # 3. Check if the customer selected a number
            if menu_selection.isdigit():

                # 4. Check that the menu_selection is an integer and check if the menu selection is in the menu items
                if int(menu_selection) in menu_items.keys():

                    # Store the item name as an int variable
                    selection_name = menu_items[int(menu_selection)]['Item name']

                    # Ask the customer for the quantity of the menu item
                    quantity = input(f"How many {selection_name}s do you want? ")

                    # Check if the quantity variable is a number, default to 1 if not
                    # How do we defult to 1?
                    if quantity.isdigit():

                    # Add the item name, price, and quantity to the order list
                        order.append({
                            "Item name": selection_name,
                            "Price": menu_items[int(menu_selection)]['Price'],
                            "Quantity": quantity
                        })

                    # Tell the customer that their input for quantity isn't valid
                    else:
                        print("For the quantity, you must input a whole number.")


                # Tell the customer they didn't select a menu option
                else:
                    print("For the item number, you must input a whole number.")

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_category} was not a valid menu number.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a valid menu number.")

# ----------Ask Customer if They'd Like to Continue Ordering or Not-------------

    while True:
        # Ask the customer if they would like to order anything else, I also added a 'capitalize' to convert the y/n answer
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o: ").capitalize()

        # 5. Check the customer's input
        if keep_ordering == 'Y'or keep_ordering == 'N':
            
            # Keep ordering
            if keep_ordering == 'Y':
                place_order = True
                break
                
                # Exit the keep ordering question loop and complete the order
            else:
                # Since the customer decided to stop ordering, thank them for their order
                print("Thank you for your order!")

                # Exit the keep ordering question loop
                place_order = False
                break

        # Tell the customer to try again
        else:
            print("Not a valid selection: please choose 'Y' or 'N'.")

# -------------------Display Back the Complete Order----------------------------

print("Item name                 | Price  | Quantity")
print("--------------------------|--------|----------")

# 6. Loop through the items in the customer's order
for i in range(len(order)):

    # 7. Store the dictionary items as variables
    item_name = order[i]["Item name"]
    price = order[i]["Price"]
    quantity = order[i]["Quantity"]

    # 8. Calculate the number of spaces for formatted printing
    num_item_spaces = 26 - len(item_name)
    num_price_spaces = 6 - len(str(price))

    # 9. Create space strings
    item_spaces = " " * num_item_spaces
    price_spaces = " " * num_price_spaces

    # 10. Print the item name, price, and quantity
    print(f"{item_name}{item_spaces}| ${price}{price_spaces}| {quantity}")

# 11. Calculate the cost of the order using list comprehension
# Multiply the price by quantity for each item in the order list, then sum()
# and print the prices.

total_price = sum([item["Price"] * item["Quantity"] for item in order])

print(f"\nTotal price: ${total_price:.2f}")
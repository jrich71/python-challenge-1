# python-challenge-1

## Order System

* Create an empty list. This list will later store a customer's order in dictionary format, as follows:

[
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
  {
    "Item name": "string",
    "Price": float,
    "Quantity": int
  },
]

> Issue: I'm not fully understanding what's being asked, but might the solution be: 'order_list = []'?

* After the sub-menu is printed, prompt the customer to enter their selection from the menu, saving it as a variable menu_selection.

> Issue: What is a/the sub-menu?
> Issue: I'm confused. Is this in place of or separate from "menu_category" variable already in the file?

* Use input validation to check if the customer input menu_selection is a number. If it isn't, print an error message. If it is a number, convert the input to an integer and use it to check if it is in the keys of menu_items.

> Possible solution: Use isdigit and int/type converter.

* If the user input is not in the menu_items keys, print an error. Otherwise, perform the following actions:

> What on earth is being asked of us? How is menu_items keys relating to whatever preceding code?

  * Get the item name from the menu_items dictionary and store it as a variable.

  * Ask the customer for the quantity of the menu item, using the item name variable in the question, and let them know that the quantity will default to 1 if their input is invalid. Save their answer as a variable called quantity.

  * Check that the customer input is a number. If it isn't, set the quantity to the value 1. If it is a number, convert the variable to an integer.

  * Append the customer's order to the order list in dictionary format with the following keys: "Item name", "Price", and "Quantity. You will need this information to print the receipt at the end of the order. The price should be found in the menu_items dictionary.

* Inside the continuous while loop that prompts the customer if they would like to keep ordering, write a match:case statement that checks for y or n (upper or lowercase), and includes a default option if neither letter is entered by the customer. The following actions should be performed for each case:

  * y: Set the place_order variable to True and break from the continuous while loop.

  * n: Set the place_order variable to False, print "Thank you for your order", and break from the continuous while loop.

  * Default: Tell the customer to try again because they didn't type a valid input.
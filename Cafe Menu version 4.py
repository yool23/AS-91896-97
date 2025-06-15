#Version 4 Cafe BDSC App

import easygui

# Store users and passwords
users = {}

# Login or Sign up
while True:
    choice = easygui.buttonbox("Welcome to BDSC Cafe App!\nDo you want to log in or sign up?", choices=["Log In", "Sign Up", "Exit"])

    if choice is None or choice == "Exit":
        easygui.msgbox("Thank you for your time!")
        break

    if choice == "Sign Up":
        username = easygui.enterbox("Enter a new username:")
        if username is None:
            continue
        if username in users:
            easygui.msgbox("Username already taken.")
        else:
            password = easygui.passwordbox("Create a password:")
            if password is None:
                continue
            users[username] = password
            easygui.msgbox("Account created!")

    elif choice == "Log In":
        username = easygui.enterbox("Enter your username:")
        if username is None:
            continue
        password = easygui.passwordbox("Enter your password:")
        if password is None:
            continue
        if username in users and users[username] == password:
            easygui.msgbox("Login successful!")
            break
        else:
            easygui.msgbox("Wrong username or password.")

# If user exited at login/signup, end program here
else:
    # This else corresponds to while-loop, only runs if while-loop ended normally
    # We want to stop here if user chose Exit or canceled before logging in
    exit()

# Menus
food_menu = {
    "pizza": 1.75,
    "nachos": 1.50,
    "popcorn": 2.00,
    "fries": 2.50,
    "chips": 1.00
}
drink_menu = {
    "soda": 2.00,
    "lemonade": 1.00
}

cart = []
total = 0

response = easygui.buttonbox("Welcome to BDSC Cafe App!\nWould you like to join?", choices=["Yes", "No"])
if response is None or response == "No":
    easygui.msgbox("Thank you for your time!")
    easygui.msgbox("Thank you for using the BDSC Cafe App. Come again!")
    exit()

def show_menu():
    menu_text = "-------- MENU -------------\n"
    menu_text += "--- FOOD ---\n"
    for item, price in food_menu.items():
        menu_text += f"{item.title():10} : ${price:.2f}\n"
    menu_text += "\n--- DRINKS ---\n"
    for item, price in drink_menu.items():
        menu_text += f"{item.title():10} : ${price:.2f}\n"
    menu_text += "---------------------------"
    easygui.msgbox(menu_text)

show_menu()

while True:
    food = easygui.enterbox("Type an item to order.\nType 'menu' to view menu again\nType 'remove' to take something out\nType 'done' to finish:")
    if food is None:
        easygui.msgbox("Thank you for your time!")
        easygui.msgbox("Thank you for using the BDSC Cafe App. Come again!")
        exit()
    food = food.strip().lower()

    if food == "done":
        break
    elif food == "menu":
        show_menu()
    elif food == "remove":
        if not cart:
            easygui.msgbox("Your cart is empty. Nothing to remove.")
        else:
            item_to_remove = easygui.enterbox("Type the item name to remove:")
            if item_to_remove is None:
                easygui.msgbox("Thank you for your time!")
                easygui.msgbox("Thank you for using the BDSC Cafe App. Come again!")
                exit()
            item_to_remove = item_to_remove.strip().lower()
            if item_to_remove in cart:
                cart.remove(item_to_remove)
                price = food_menu.get(item_to_remove, drink_menu.get(item_to_remove, 0))
                total -= price
                easygui.msgbox(f"{item_to_remove.title()} removed from your cart.")
            else:
                easygui.msgbox("Item not found in your cart.")
    elif food in food_menu or food in drink_menu:
        cart.append(food)
        price = food_menu.get(food, drink_menu.get(food, 0))
        total += price
        easygui.msgbox(f"{food.title()} added to cart. Price: ${price:.2f}")
    else:
        easygui.msgbox("Item not found. Please try again.")

if cart:
    receipt = "------ YOUR ORDER ------\n"
    for item in cart:
        price = food_menu.get(item, drink_menu.get(item, 0))
        receipt += f"{item.title():10} : ${price:.2f}\n"
    receipt += f"\nTotal: ${total:.2f}\n"
    receipt += "------------------------"
    easygui.msgbox(receipt)
else:
    easygui.msgbox("You didn't order anything.")

# Final thank you message always shown here before program ends
easygui.msgbox("Thank you for using the BDSC Cafe App. Come again!")




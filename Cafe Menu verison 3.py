#Version 3 BDSC Cafe App

import easygui

# Store users and passwords
users = {}

# Login or Sign up
while True:
    choice = easygui.buttonbox("Welcome to BDSC Cafe App!\nDo you want to log in or sign up?", choices=["Log In", "Sign Up", "Exit"])

    if choice == "Sign Up":
        username = easygui.enterbox("Enter a new username:")
        if username in users:
            easygui.msgbox("Username already taken.")
        else:
            password = easygui.passwordbox("Create a password:")
            users[username] = password
            easygui.msgbox("Account created!")

    elif choice == "Log In":
        username = easygui.enterbox("Enter your username:")
        password = easygui.passwordbox("Enter your password:")
        if username in users and users[username] == password:
            easygui.msgbox("Login successful!")
            break
        else:
            easygui.msgbox("Wrong username or password.")

    else:
        easygui.msgbox("Goodbye!")
        exit()

# Separate food and drink menus
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

if response == "Yes":
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
        food = easygui.enterbox("Type an item to order.\nType 'menu' to view menu again or 'done' to finish:").strip().lower()

        if food == "done":
            break
        elif food == "menu":
            show_menu()
        elif food in food_menu or food in drink_menu:
            cart.append(food)
        else:
            easygui.msgbox("Sorry, that item is not on the menu.")

    if cart:
        order_summary = "------- YOUR ORDER -------\n"
        for item in cart:
            if item in food_menu:
                price = food_menu[item]
            else:
                price = drink_menu[item]
            order_summary += f"- {item.capitalize()} : ${price:.2f}\n"
            total += price
        order_summary += f"\nTotal: ${total:.2f}"
        easygui.msgbox(order_summary + "\nThank you! Please wait for your order.")
    else:
        easygui.msgbox("You didn't order anything.")
else:
    easygui.msgbox("Thank you so much for your time, have a good day!")







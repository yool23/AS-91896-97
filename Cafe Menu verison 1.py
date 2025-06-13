#Cafe Menu in bdsc school version 1

menu = {
    "pizza": 1.75,
    "nachos": 1.50,
    "popcorn": 2.00,
    "fries": 2.50,
    "chips": 1.00,
    "soda": 2.00,
    "lemonade": 1.00
}

cart = []
total = 0

print("Welcome to BDSC Cafe App!")
response = input("Would you like to join? (Yes/No): ").strip().lower()

if response == "yes":
    print("-------- MENU -------------")
    for item, price in menu.items():
        print(f"{item.title():10} : ${price:.2f}")
    print("---------------------------")

    while True:
        food = input("Select an item (type 'done' to finish): ").strip().lower()
        if food == "done":
            break
        elif food in menu:
            cart.append(food)
        else:
            print("Sorry, that item is not on the menu.")

    print("------- YOUR ORDER -------")
    for food in cart:
        print(f"- {food.capitalize()} : ${menu[food]:.2f}")
        total += menu[food]

    print(f"\nTotal: ${total:.2f}")
    print("Thank you! Please wait for your order.")

else:
    print(" Thank you so much for your time, have a good day!")


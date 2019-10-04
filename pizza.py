def make_pizza(size, *toppings):
    """Summarize the pizza that we are about to make."""
    
    print("\nMaking a " + str(size) + "-inch pizza with the follwing toppings:")
    
    for topping in toppings:
        print("- " + topping)
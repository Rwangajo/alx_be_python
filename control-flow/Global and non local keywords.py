def outer_function():
    x = 10 # Variable in the enclosing function

    def inner_function():
        nonlocal x  # Using nonlocal to modify x from the enclosing function
        x += 5 # Modifying the value x

    inner_function()  # Calling the nested function
    print("Modified value of c from inner function:", x)

outer_function()
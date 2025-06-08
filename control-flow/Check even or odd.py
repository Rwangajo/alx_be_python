def even_odd(x):

    if x % 2 == 0:
        print(f"{x} is even.")
    else:
        print(f"{x} is odd.")

x = int(input("Enter number to check if its odd or even: "))
even_odd(x)
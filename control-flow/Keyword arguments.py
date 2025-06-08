def user_info(name, age=None):
    #prints user information.
    print(f"Name: {name}")
    if age:
        print(f"Age: {age}")
user_info(name="Bob", age=30)
def has_id():
    response = input("Do you have a valid ID? (yes/no): ").strip().lower()
    return response == "yes"

age = int(input("Enter your age: "))

match age:
    case age if age >= 18:  # Match any age 18 or above
        if has_id():        # Guard: only allow if they have ID
            print("You are eligible to vote.")
        else:
            print("You need a valid ID to vote.")
    case _:  # Default case
        print("You are not yet eligible to vote.")

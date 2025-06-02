# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process using match-case and time-bound logic
match priority:
    case "high":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"\nNote: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a medium priority task that requires attention today.")
        else:
            print(f"\nNote: '{task}' is a medium priority task. Plan to do it soon.")
    case "low":
        if time_bound == "yes":
            print(f"\nReminder: '{task}' is a low priority task but still requires attention today.")
        else:
            print(f"\nNote: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print(f"\nOops! '{priority}' is not a recognized priority. Please use high, medium, or low.")

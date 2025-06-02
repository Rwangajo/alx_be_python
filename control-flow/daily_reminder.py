# Prompt for a single task
task = input("Enter the task description: ")
priority = input("Enter the task's priority (high, medium, low): ").lower()
time_bound = input("Is the task time-bound? (yes or no): ").lower()

# Process the task based on priority
match priority:
    case "high":
        reminder = f"Task: {task} [Priority: HIGH]"
    case "medium":
        reminder = f"Task: {task} [Priority: MEDIUM]"
    case "low":
        reminder = f"Task: {task} [Priority: LOW]"
    case _:
        reminder = f"Task: {task} [Priority: UNKNOWN]"

# Modify the reminder if the task is time-bound
if time_bound == "yes":
    reminder += " — This task requires immediate attention today!"

# Print the customized reminder
print("\nReminder:")
print(reminder)

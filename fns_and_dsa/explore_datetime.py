import datetime

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Save the current date and time
    current_date = datetime.datetime.now()

    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print("Current Date and Time:", formatted)

# Part 2: Calculate a Future Date
def calculate_future_date(days):
    # Get today's date (date only, no time)
    current_date = datetime.date.today()

    # Calculate the future date
    future_date = current_date + datetime.timedelta(days=days)

    # Print the future date in "YYYY-MM-DD" format
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Run the program
if __name__ == "__main__":
    # Part 1
    display_current_datetime()

    # Part 2
    try:
        days_input = int(input("Enter number of days to add: "))
        calculate_future_date(days_input)
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

from datetime import datetime, timedelta, date

# Part 1: Display the Current Date and Time
def display_current_datetime():
    # Save the current date and time
    current_date = datetime.now()

    # Format as "YYYY-MM-DD HH:MM:SS"
    formatted = current_date.strftime("%Y-%m-%d %H:%M:%S")

    # Print the formatted current date and time
    print("Current Date and Time:", formatted)

# Part 2: Calculate a Future Date
def calculate_future_date(days_to_add):
    # Get today's date
    today = date.today()

    # Calculate the future date
    future_date = today + timedelta(days=days_to_add)

    # Print the future date in "YYYY-MM-DD" format
    print("Future Date:", future_date.strftime("%Y-%m-%d"))

# Main program
if __name__ == "__main__":
    display_current_datetime()

    try:
        # ✅ Use the exact expected prompt
        num_days = int(input("Enter the number of days to add to the current date:"))
        calculate_future_date(num_days)
    except ValueError:
        print("Invalid input. Please enter an integer.")

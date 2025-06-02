# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer loop (while) controls the number of rows
while row < size:
    # Inner loop (for) prints asterisks in a row
    for column in range(size):
        print("*", end="")
    print()  # Move to next line after each row
    row += 1

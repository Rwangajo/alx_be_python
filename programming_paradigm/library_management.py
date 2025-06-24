# main.py

import sys
from robust_division_calculator import safe_divide

def main():
    """
    Main function to handle command line arguments for division.
    It takes two arguments: numerator and denominator, and uses
    the safe_divide function to perform the division.
    """
    # Check if the correct number of command line arguments is provided
    # sys.argv[0] is the script name itself, so we expect 3 arguments in total
    if len(sys.argv) != 3:
        print("Usage: python main.py <numerator> <denominator>")
        # Exit the script with an error code
        sys.exit(1)

    # Get numerator and denominator from command line arguments
    numerator = sys.argv[1]
    denominator = sys.argv[2]

    # Call the safe_divide function from robust_division_calculator.py
    result = safe_divide(numerator, denominator)

    # Print the result returned by safe_divide
    print(result)

# Ensure main() is called only when the script is executed directly
if __name__ == "__main__":
    main()


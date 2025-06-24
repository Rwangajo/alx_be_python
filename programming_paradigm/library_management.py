# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Performs division, handling potential errors like division by zero
    and non-numeric inputs.

    Args:
        numerator: The dividend (can be a string or numeric type).
        denominator: The divisor (can be a string or numeric type).

    Returns:
        A string message indicating the result of the division or an error.
    """
    try:
        # Attempt to convert numerator and denominator to floats
        num = float(numerator)
        den = float(denominator)

        # Check for division by zero
        if den == 0:
            return "Error: Cannot divide by zero."
        
        # Perform division if no errors so far
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Catch ValueError if conversion to float fails (non-numeric input)
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Although the 'if den == 0' handles this, a direct ZeroDivisionError
        # catch is included for robustness in case the float conversion
        # or some edge case bypasses the explicit check (though unlikely here).
        # This catch block is technically redundant given the `if den == 0` check,
        # but it demonstrates handling the specific exception type.
        return "Error: Cannot divide by zero."
    except Exception as e:
        # Catch any other unexpected errors
        return f"An unexpected error occurred: {e}"


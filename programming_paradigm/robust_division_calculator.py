def safe_divide(numerator, denominator):

    try:
        num= float (numerator)
        dem = float (denominator)

        result = num/dem
        return print (f"The result of the division is {result:.2f}")
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Both inputs must be numeric."

     



def safe_divide(numerator, denominator): 
    try:
        num = float(numerator)
        dem = float(denominator)

        result = num / dem
        print(f"The result of the division is {result:.1f}")
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    except ValueError:
        print("Error: Please enter numeric values only.")

     



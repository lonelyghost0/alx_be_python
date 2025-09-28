from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    format_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return format_current_date

def calculate_future_date(current_date):
    days_to_add = int(input("Enter the number of days to add to the current date:"))
    future_date = current_date + timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date


# Example usage:
current_date = datetime.now()
print("Current date and time:", display_current_datetime())
print("Future date:", calculate_future_date(current_date))



import datetime

def display_current_datetime ():
    current_date = datetime.datetime.now()
    format_current_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return current_date

def calculate_future_date (current_date):
    days_to_add = int(input("Enter the number of days to add: "))
    future_date = current_date + datetime.timedelta(days=days_to_add)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date


now = display_current_datetime()
<<<<<<< HEAD
calculate_future_date(now)
=======
future = calculate_future_date(now)
>>>>>>> b045fcaf7ecd0d5e68d09b253f4d2ffe15d4ceb8

print (future)

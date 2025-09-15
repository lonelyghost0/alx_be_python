task = input("Enter your task:")
Priority = input("Priority (high/medium/low):")
time_bound = input("Is it time-bound? (yes/no):")

match Priority : 
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low  priority task that requires immediate attention within the next 30 days !")
        else:
            print(f"Note: {task} is a low priority task. Consider completing it when you have free time.")

    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires immediate attention within the next 7 days !")
        else:
            print (f"note : {task} is of medium priority. Consider competing  completing within 2 week.")

    case "high":
        if time_bound == "yes":
            print("Reminder: {task} is a high priority task that requires immediate attention today!")
        else :
         print (f"{task} is of high prioity. Consider competing within the nex 3 days")



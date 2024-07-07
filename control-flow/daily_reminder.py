while True:
    task = input("Enter your task: ")
    priority = input("Priority (high/medium/low): ").lower()
    time_bound = input("Is it time-bound? (yes/no): ").lower()
    match priority:
        case "high":
            reminder = f"'{task}' is a high priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". Consider completing it as soon as possible."
            print("Reminder:", reminder)
        case "medium":
            reminder = f"'{task}' is a medium priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". It should be completed in a timely manner."
            print("Reminder:", reminder)
        
        case "low":
            reminder = f"'{task}' is a low priority task"
            if time_bound == "yes":
                reminder += " that requires immediate attention today!"
            else:
                reminder += ". Consider completing it when you have free time."
            print("Reminder:", reminder)
        
        case _:
            print("Invalid priority level entered.")
    repeat = input("Do you want to enter another task? (yes/no): ").lower()
    if repeat != "yes":
        break
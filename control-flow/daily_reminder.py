# daily_reminder.py

# Prompt for user input
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").strip().lower()
time_bound = input("Is it time-bound? (yes/no): ").strip().lower()

# Process the task using match case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task"
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task"
    case "low":
        message = f"Note: '{task}' is a low priority task"
    case _:
        message = f"Note: '{task}' has an unspecified priority"

# Add time sensitivity message
if time_bound == "yes":
    message += " that requires immediate attention today!"
else:
    if "Note:" in message:
        message += " Consider completing it when you have free time."
    else:
        message += " but it's not time-sensitive. Plan accordingly."

# Display the final reminder
print(message)

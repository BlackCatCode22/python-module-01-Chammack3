# welcome.py
from datetime import datetime

# Get the current time
current_hour = datetime.now().hour

# Determine the appropriate greeting based on the time of day
if current_hour < 12:
    greeting = "Good morning"
elif 12 <= current_hour < 18:
    greeting = "Good afternoon"
else:
    greeting = "Good evening"

# Prompt the user for their name
name = input("Please enter your name: ")

# Display the greeting
print(f"{greeting}, {name}!")

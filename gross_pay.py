hours_worked = float(input("Enter the number of hours worked this week: "))
hourly_rate = float(input("Enter your hourly rate: "))

# Calculate the gross pay
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (hourly_rate * 1.5)
    gross_pay = (40 * hourly_rate) + overtime_pay
else:
    gross_pay = hours_worked * hourly_rate

# Output the gross pay
print(f"Your gross pay is: ${gross_pay:.2f}")

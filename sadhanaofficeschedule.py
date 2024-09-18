from datetime import datetime, timedelta

def is_wfh(date):
    # Calculate the number of weekdays since the reference date
    reference_date = datetime(2024, 8, 8)  # Reference date when she is WFH
    delta_days = (date - reference_date).days
    
    # Calculate the number of weekdays (excluding weekends)
    weekdays_passed = 0
    current_date = reference_date

    while current_date <= date:
        if current_date.weekday() < 5:  # Monday to Friday are considered
            weekdays_passed += 1
        current_date += timedelta(days=1)

    # Determine the week cycle (0-9, where 0-4 is WFH and 5-9 is office)
    cycle_day = weekdays_passed % 10

    # Determine if the given date is WFH or office
    if cycle_day in [0, 1, 2, 3, 4]:  # 5 days WFH
        return "WFH"
    else:
        return "Office"

# Example usage:
input_date_str = input("Enter a date (YYYY-MM-DD): ")
input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
work_status = is_wfh(input_date)
print(f"On {input_date_str}, she is working: {work_status}")


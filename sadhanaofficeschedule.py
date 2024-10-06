from datetime import datetime, timedelta

def is_wfh(date):
    # Define the reference date for the schedule
    reference_date = datetime(2024, 10, 3)  # Start of WFH cycle (first day she WFH)
    
    # Calculate the number of weekdays passed since the reference date
    delta_days = (date - reference_date).days
    weekdays_passed = 0
    current_date = reference_date

    while current_date <= date:
        if current_date.weekday() < 5:  # Only count weekdays (Monday to Friday)
            weekdays_passed += 1
        current_date += timedelta(days=1)

    # Determine the 10-day cycle (5 WFH followed by 5 office days)
    cycle_day = weekdays_passed % 10

    # Determine if the given date is WFH or office
    if cycle_day in [0, 1, 2, 3, 4]:  # First 5 days are WFH
        return "WFH"
    else:  # Next 5 days are Office
        return "Office"

# Example usage:
input_date_str = input("Enter a date (YYYY-MM-DD): ")
input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
work_status = is_wfh(input_date)
print(f"On {input_date_str}, she is working: {work_status}")

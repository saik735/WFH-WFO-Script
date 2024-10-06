from datetime import datetime, timedelta

def is_wfh(date):
    # Define the reference date
    reference_date = datetime(2024, 10, 3)  # First WFH day
    
    # Calculate the number of days between the reference date and the input date
    delta_days = (date - reference_date).days
    
    # Calculate how many weekdays (ignoring weekends) have passed
    weekdays_passed = 0
    current_date = reference_date
    
    while current_date <= date:
        if current_date.weekday() < 5:  # Monday to Friday are considered as weekdays
            weekdays_passed += 1
        current_date += timedelta(days=1)

    # Determine if it's WFH or Office using a 10-day cycle
    cycle_day = weekdays_passed % 10

    if cycle_day in [1, 2, 3, 4, 5]:  # First 5 days are WFH
        return "WFH"
    else:  # Next 5 days are Office
        return "Office"

# Example usage:
input_date_str = input("Enter a date (YYYY-MM-DD): ")
input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
work_status = is_wfh(input_date)
print(f"On {input_date_str}, she is working: {work_status}")

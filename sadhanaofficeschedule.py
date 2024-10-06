from datetime import datetime, timedelta

def is_wfh(date):
    # Define the reference date and schedule start
    reference_date = datetime(2024, 10, 3)  # First WFH day
    delta_days = (date - reference_date).days

    # Count the weekdays only (ignore weekends)
    weekdays_passed = 0
    current_date = reference_date
    while current_date <= date:
        if current_date.weekday() < 5:  # Monday to Friday are considered (0 = Monday, 4 = Friday)
            weekdays_passed += 1
        current_date += timedelta(days=1)

    # Determine the cycle (5 WFH followed by 5 office days)
    cycle_day = (weekdays_passed - 1) % 10  # We subtract 1 to make the pattern start correctly from 0

    # If it's a WFH day (first 5 days), otherwise it's an office day
    if cycle_day in [0, 1, 2, 3, 4]:  # First 5 days are WFH
        return "WFH"
    else:  # Next 5 days are office
        return "Office"

# Example usage:
input_date_str = input("Enter a date (YYYY-MM-DD): ")
input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
work_status = is_wfh(input_date)
print(f"On {input_date_str}, she is working: {work_status}")

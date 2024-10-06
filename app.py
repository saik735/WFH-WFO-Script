from flask import Flask, render_template, request
from datetime import datetime, timedelta

# Define Flask app
app = Flask(__name__)

# The updated `is_wfh` function (assuming it’s in this file; otherwise, import it)
def is_wfh(date):
    # Define the reference date and schedule start
    reference_date = datetime(2024, 10, 3)  # First WFH day
    delta_days = (date - reference_date).days

    # Count the weekdays only (ignore weekends)
    weekdays_passed = 0
    current_date = reference_date
    while current_date <= date:
        if current_date.weekday() < 5:  # Monday to Friday are considered as weekdays
            weekdays_passed += 1
        current_date += timedelta(days=1)

    # Determine the cycle (5 WFH followed by 5 office days)
    cycle_day = (weekdays_passed - 1) % 10  # Adjust cycle by subtracting 1 to start correctly

    # Return WFH for first 5 days and Office for next 5 days
    if cycle_day in [0, 1, 2, 3, 4]:
        return "WFH"
    else:
        return "Office"

# Define a single route that handles both `/check-status` and `/check-status-ui`
@app.route('/check-status', methods=['GET'])
@app.route('/check-status-ui', methods=['GET'])
def check_status():
    # Get the date from URL parameters
    input_date_str = request.args.get('date')
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')

    # Call the `is_wfh` function to get the work status
    work_status = is_wfh(input_date)

    # Debug logging to check the logic output
    print(f"DEBUG: For {input_date_str}, work_status is {work_status}")

    # Render the result using a template
    return render_template('check_status.html', work_status=work_status, date=input_date_str)

# Run the Flask app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)


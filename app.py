from flask import Flask, request, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

# Function to determine WFH or Office
def is_wfh(date):
    reference_date = datetime(2024, 8, 8)  # Reference date when she is WFH
    delta_days = (date - reference_date).days
    
    weekdays_passed = 0
    current_date = reference_date

    while current_date <= date:
        if current_date.weekday() < 5:  # Monday to Friday are considered
            weekdays_passed += 1
        current_date += timedelta(days=1)

    cycle_day = weekdays_passed % 10

    if cycle_day in [0, 1, 2, 3, 4]:  # 5 days WFH
        return "WFH"
    else:
        return "Office"

# Serve the new HTML page
@app.route('/check-status-ui', methods=['GET'])
def check_status_ui():
    return render_template('check_status.html')

# Existing endpoint that takes the date as a query parameter
@app.route('/check-status', methods=['GET'])
def check_status():
    date_str = request.args.get('date')
    input_date = datetime.strptime(date_str, '%Y-%m-%d')
    work_status = is_wfh(input_date)
    return f"On {date_str}, she is working: {work_status}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

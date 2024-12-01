from flask import Flask, render_template, request
import pickle  # For loading model (if required)
from datetime import datetime

app = Flask(__name__)

# Load your pre-trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Extract data from form
        date = request.form['date']
        month_name = request.form['month_name']
        day_name = request.form['day_name']
        weekend = request.form['weekend']
        time_phase = request.form['time_phase']

        # Dictionary for month names
        month_dict = {
            "january": 1,
            "february": 2,
            "march": 3,
            "april": 4,
            "may": 5,
            "june": 6,
            "july": 7,
            "august": 8,
            "september": 9,
            "october": 10,
            "november": 11,
            "december": 12
        }

        # Convert month name to int
        if month_name.isalpha():
            month_name = month_name.lower()
            month_name = month_dict[month_name]
        else:
            month_name = int(month_name)  # Keep as int if numeric

        date = int(date)

        # Specify the day
        mn = month_name
        year = 2015
        date_obj = datetime(year, mn, date)
        
        # Get the day name
        day_name = date_obj.strftime('%A').lower()

        # Dictionary for day names
        day_dict = {
            "monday": 0,
            "tuesday": 1,
            "wednesday": 2,
            "thursday": 3,
            "friday": 4,
            "saturday": 5,
            "sunday": 6
        }
        
        

        # Convert day name to int
        day_name = day_dict[day_name]

        # Determine if it's a weekend
        weekend = 1 if date_obj.weekday() in (5, 6) else 0
        
        # Convert time_phase to int or set to 0 if empty
        time_phase = int(time_phase) if time_phase else 0
        
        # Make a prediction using your model
        prediction = model.predict([[date, month_name, day_name, weekend, time_phase]])

        # Extract prediction values for display
        sales_forecast = prediction[0][0]  # First prediction value
        another_metric = prediction[0][1]   # Second prediction value

        sales_forecast = round(sales_forecast, 2)  # Round to 2 decimal places
        another_metric = round(another_metric, 2)  # Round to 2 decimal places

        return render_template('index.html', sales_forecast=sales_forecast, another_metric=another_metric)

if __name__ == '__main__':
    app.run(debug=True)

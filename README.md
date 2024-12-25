# 🍕 Pizza Sales Forecasting Project <br>
**Author** : Ansh Kapoor <br>

## 📄 Project Overview
This project leverages machine learning to forecast pizza sales using a dataset sourced from Kaggle. The aim is to provide an accurate prediction model and an interactive web interface for user-friendly sales forecasting.<br> The model uses a Random Forest Regressor (RFR) with hyperparameter tuning to achieve high accuracy. The project includes data preprocessing, model training, evaluation, and deployment via a Flask web application.<br>

## 📂 Project Structure
- `DATA MODEL - pizza sales.csv` : Raw dataset sourced from Kaggle.
- `making_my_dataset.ipynb` : Jupyter notebook for initial data preprocessing and feature engineering.
- `main_pizza_dataset_ansh.xlsx` : Processed dataset ready for model training.
- `main.ipynb` : Jupyter notebook for model training, evaluation, and testing.
  - Includes:
    - Model: RandomForestRegressor
    - Hyperparameters: Tuned using GridSearchCV.
    - Performance Metrics:
      - MAE: 61.18
      - MSE: 12320.47
      - R² Score: 0.9153
      - Adjusted R²: 0.9111
- `app.py` : Flask application script for deploying the model and providing a user-friendly web interface.
- `templates/` : Contains HTML and CSS files for the web application.

## 🚀 Features
- Data Preprocessing:<br>
Cleaned raw data and created additional features like Day_name, Weekend, and Time_phase.

- Model Training:<br>
Used Random Forest Regressor with the following configuration:

      main_rfg = RandomForestRegressor(max_depth=None,  
                                 min_samples_leaf=4,  
                                 min_samples_split=10,  
                                 n_estimators=50)  
      main_rfg.fit(X_train, y_train)  
- Performance:
  - Mean Absolute Error (MAE): 61.18
  - Mean Squared Error (MSE): 12320.47
  - R² Score: 91.53%
- Web Application:<br>
Interactive interface where users can input data and get real-time sales predictions.


## 🛠️ Installation
1. Clone the Repository

        git clone https://github.com/ratals/Sales-Forecasting-Using-Machine-Learning.git
        cd pizza-sales-forecasting
2. Install Dependencies

       pip install -r requirements.txt
   
4. Run the Flask App

       python app.py
5. Access the Application<br>
Open your browser and navigate to `http://127.0.0.1:5000`.<br>
Below is a screenshot of the interactive web interface developed for the pizza sales forecasting model:
![image](https://github.com/user-attachments/assets/a2981ab2-1581-4270-8fd4-8cd633d2188d)


## 📊 Key Insights
- Pizza sales are influenced by temporal features such as the day of the week, time of day, and weekends.
- Hyperparameter tuning significantly improved the model’s accuracy.

## 📧 Contact
**LinkedIn** : [Ansh Kapoor](https://www.linkedin.com/in/ansh-kapoor-a153a8222/)


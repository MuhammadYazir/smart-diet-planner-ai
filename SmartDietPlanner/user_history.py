# user_history.py

import pandas as pd
from datetime import datetime
import os

def save_user_result(user_name, user_email, bmi, calories, goal, recipe):
    #Save a user's generated plan to a local CSV file with timestamp and unique ID.
    record = {
        "EntryID": datetime.now().strftime("%Y%m%d%H%M%S"),    # Unique ID (date+time)
        "Name": user_name,
        "Email": user_email,
        "BMI": bmi,
        "Calories": calories,
        "Goal": goal,
        "Recipe": recipe,
        "Timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.DataFrame([record])
    if os.path.exists("user_results.csv"):
        df.to_csv("user_results.csv", mode="a", header=False, index=False)
    else:
        df.to_csv("user_results.csv", index=False)

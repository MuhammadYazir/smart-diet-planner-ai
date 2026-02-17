# diet_utils.py

def calculate_bmi(weight, height):
# Calculate BMI using the formula: weight (kg) / height^2 (m^2)
# Returns the BMI value and the status
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        status = "Underweight"
    elif bmi < 24.9:
        status = "Normal"
    elif bmi < 29.9:
        status = "Overweight"
    else:
        status = "Obese"
    return bmi, status

def calculate_calories(weight, height, age, gender, activity, goal):
    # Estimate daily calorie needs using Mifflin-St Jeor formula.
    if gender.lower() == "male":
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age + 5
    else:
        bmr = 10 * weight + 6.25 * height * 100 - 5 * age - 161

    activity_multiplier = {"low": 1.2, "medium": 1.55, "high": 1.9}
    calories = bmr * activity_multiplier.get(activity, 1.2)

    if goal == "weight loss":
        calories -= 500
    elif goal == "muscle gain":
        calories += 400

    return calories

def get_macros(calories, goal):
    # Break down total calories into grams of protein, carbs, and fats based on goals
    if goal == "weight loss":
        protein_perc, carbs_perc, fats_perc = 0.4, 0.3, 0.3
    elif goal == "muscle gain":
        protein_perc, carbs_perc, fats_perc = 0.3, 0.35, 0.35
    else:
        protein_perc, carbs_perc, fats_perc = 0.3, 0.4, 0.3

    protein = (calories * protein_perc) / 4
    carbs = (calories * carbs_perc) / 4
    fats = (calories * fats_perc) / 9

    return protein, carbs, fats

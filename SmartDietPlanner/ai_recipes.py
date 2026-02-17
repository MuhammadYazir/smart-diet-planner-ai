# ai_recipes.py

import openai

def generate_ai_recipe(goal, dish, condition):
    # Generate a recipe using AI based on the selected dish
    prompt = f"Generate a healthy recipe for {dish}. User's goal: {goal}, medical condition: {condition}. Please provide list of ingredients and step-by-step instructions."
    try:
        response = openai.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "You are a nutritionist and chef creating personalized healthy recipes."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=700,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Unable to generate: {e}"

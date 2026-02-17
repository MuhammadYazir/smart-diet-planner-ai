# nutrition_api.py

import requests
# Move credentials to environment variables in future
CLIENT_ID = "9d5b01ec343344fc9fca9b226e95d777"
CLIENT_SECRET = "1a1f8799509f4c16b99ece8bce306782"

def get_access_token():
    # Request an OAuth access token from FatSecret API using client credentials
    url = "https://oauth.fatsecret.com/connect/token"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}
    data = {
        "grant_type": "client_credentials",
        "scope": "basic",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

def get_nutrition_info(food_name):
    # Fetching nutrition information for the given food item using FatSecret API
    token = get_access_token()
    if not token:
        return "❌ Failed to authentication failed with FatSecret."
    url = "https://platform.fatsecret.com/rest/server.api"
    params = {
        "method": "foods.search",
        "search_expression": food_name,
        "format": "json"
    }
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers, params=params)
    try:
        item = response.json()["foods"]["food"][0]
        return f"{item['food_name']} — {item['food_description']}"
    except Exception as e:
        return "No nutrition information found for the given input"

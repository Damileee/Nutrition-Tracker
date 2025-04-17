import csv
from datetime import datetime

def load_food_data(filename):
    """Load food data from a CSV file into a dictionary."""
    food_data = {}
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row["Food"].strip().lower()
            food_data[name] = {
                "calories": float(row["Calories"]),
                "protein": float(row["Protein"]),
                "carbs": float(row["Carbs"]),
                "fat": float(row["Fat"]),
            }
    return food_data

def calculate_nutrition(food_data, selected_foods):
    """Calculate total nutrition based on selected foods."""
    totals = {"calories": 0, "protein": 0, "carbs": 0, "fat": 0}
    for food in selected_foods:
        food = food.lower()
        if food in food_data:
            for key in totals:
                totals[key] += food_data[food][key]
        else:
            print(f"Warning: '{food}' not found in food data.")
    return totals

def get_user_meal():
    """Get a list of food items from the user."""
    print("Enter foods you ate (comma-separated):")
    user_input = input("> ")
    return [item.strip() for item in user_input.split(",")]

def display_nutrition_summary(totals):
    """Display the total nutrition summary."""
    print("\nNutrition Summary:")
    print(f"Calories: {totals['calories']} kcal")
    print(f"Protein: {totals['protein']} g")
    print(f"Carbs:   {totals['carbs']} g")
    print(f"Fat:     {totals['fat']} g")

def save_log(selected_foods, totals, filename="nutrition_log.csv"):
    """Append the meal to a log file with timestamp and nutrition info."""
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([now, ", ".join(selected_foods), totals["calories"], totals["protein"], totals["carbs"], totals["fat"]])

def main():
    food_data = load_food_data("food_data.csv")
    selected_foods = get_user_meal()
    totals = calculate_nutrition(food_data, selected_foods)
    display_nutrition_summary(totals)
    save_log(selected_foods, totals)

if __name__ == "__main__":
    main()
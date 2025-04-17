🍎 Nutrition Tracker

Overview

The Nutrition Tracker is a Python program that helps users track the nutritional value of their meals. Users input foods they’ve eaten, and the program calculates the total calories, protein, fats, carbohydrates, and other nutritional information based on a food database. The project emphasizes file handling, data parsing, modular programming with functions, and testing with pytest.

Features
	•	📂 Reads nutritional data from a CSV file.
	•	🍽️ Allows users to input multiple meals and foods.
	•	➕ Calculates total calories, macronutrients, and other nutrition facts.
	•	📊 Displays daily nutrition summary clearly.
	•	🧪 Includes unit tests for key functions using pytest.
	•	💾 Easily extendable to add more foods or nutrients.

Installation
	1.	Clone the repository:
git clone https://github.com/your-username/nutrition-tracker.git
cd nutrition-tracker

Project Structure
  nutrition-tracker/
  │
  ├── nutrition_tracker.py   # Main program
  ├── food_data.csv           # Nutritional database (example CSV file)
  ├── test_nutrition.py       # Test file for functions
  ├── README.md               # This file

Key Functions
	•	load_food_data(filename): Loads food nutritional info from a CSV.
	•	get_user_input(): Collects the user’s meal input.
	•	calculate_totals(meal_list, food_database): Calculates total nutrition.
	•	display_summary(totals): Prints the nutrition summary.
	•	Test functions:
	•	test_load_food_data()
	•	test_calculate_totals()

Skills Demonstrated
	•	📚 Reading and writing CSV files
	•	🧠 Organizing code into reusable functions
	•	🔎 Writing unit tests with pytest
	•	🛠️ Debugging and problem-solving
	•	📈 Basic data aggregation and processing

Future Improvements
	•	Add GUI with tkinter for easier input.
	•	Track multiple days of meals.
	•	Generate graphs using matplotlib.
	•	Save meal history to a file for long-term tracking.

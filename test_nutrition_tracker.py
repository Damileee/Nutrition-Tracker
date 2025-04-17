from nutrition_tracker import calculate_nutrition, load_food_data

def test_calculate_nutrition():
    sample_data = {
        "apple": {"calories": 95, "protein": 0.5, "carbs": 25, "fat": 0.3},
        "banana": {"calories": 105, "protein": 1.3, "carbs": 27, "fat": 0.4},
    }
    selected = ["apple", "banana"]
    result = calculate_nutrition(sample_data, selected)
    assert result["calories"] == 200
    assert abs(result["protein"] - 1.8) < 0.01
    assert result["carbs"] == 52
    assert abs(result["fat"] - 0.7) < 0.01

def test_load_food_data(tmp_path):
    file = tmp_path / "food_data.csv"
    file.write_text("Food,Calories,Protein,Carbs,Fat\napple,95,0.5,25,0.3")
    data = load_food_data(file)
    assert "apple" in data
    assert data["apple"]["calories"] == 95
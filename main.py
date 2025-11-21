class NutritionTracker:
    def __init__(self):
        self.Nutrition = []

    def add_nutrition(foodname, time, protein, calories):
        nutrition = {
            'foodname': food_name,
            'time': time,
            'protein': protein,
            'calories': calories
        }
        self.nutrition.append(nutrition)
        print(f"Added nutrition: {foodname} on {time} with {protein} grams of protein, including {calories} calories.")

    def view_nutrition(self):
        if not self.nutrition:
            print("No nutrition to display.")
            return

        for i, nutrition in enumerate(self.nutrition, 1):
            print(f"{i}. {nutrition['name']} on {nutrition['time']} with {nutrition['protein']} grams of protein, and {nutrition['calories']} calories.")

    def delete_nutrition(self, index):
        try:
            removed_nutrition = self.nutrition.pop(index - 1)
            print(f"Removed nutrients: {removed_nutrition['name']} on {removed_nutrition['time']}.")
        except IndexError:
            print("Invalid nutrition number.")

def main():
    manager = NutritionManager()

    while True:
        print("\nNutrition Manager")
        print("1. Add Nutrition")
        print("2. View Nutrition")
        print("3. Delete Nutrition")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter Nutrition name: ")
            time = input("Enter intake time (xx:xx): ")
            Protein = input("Enter the amount of protein: ")
            calories = input("Enter the amount calories: ")
            manager.add_workout(name, date, protein, calories)
        elif choice == '2':
            manager.view_nutrition()
        elif choice == '3':
            manager.view_nutrition()
            index = int(input("Enter the nutrition number to delete: "))
            manager.delete_workout(index)
        elif choice == '4':
            print("Exiting the Nutrion Tracker.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

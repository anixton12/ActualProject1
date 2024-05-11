# recipe_manager.py
import settings

class RecipeManager:
    def __init__(self):
        self.recipes = {}
        self.load_recipes()

    def add_recipe(self, title: str, ingredients: str, instructions: str):
        recipe_id = max(self.recipes.keys(), default=0) + 1
        self.recipes[recipe_id] = {
            'title': title,
            'ingredients': ingredients,
            'instructions': instructions
        }
        self.save_recipes()

    def update_recipe(self, recipe_id: int, title: str, ingredients: str, instructions: str):
        if recipe_id in self.recipes:
            self.recipes[recipe_id] = {
                'title': title,
                'ingredients': ingredients,
                'instructions': instructions
            }
            self.save_recipes()

    def delete_recipe(self, recipe_id: int):
        if recipe_id in self.recipes:
            del self.recipes[recipe_id]
            self.save_recipes()

    def load_recipes(self):
        try:
            with open(settings.RECIPE_FILE, 'r') as file:
                for line in file:
                    parts = line.strip().split('|')
                    if len(parts) == 4:
                        recipe_id = int(parts[0])
                        self.recipes[recipe_id] = {
                            'title': parts[1],
                            'ingredients': parts[2],
                            'instructions': parts[3]
                        }
        except FileNotFoundError:
            open(settings.RECIPE_FILE, 'w').close()  # Corrected this line by removing the period

    def save_recipes(self):
        with open(settings.RECIPE_FILE, 'w') as file:
            for recipe_id, recipe in self.recipes.items():
                file.write(f"{recipe_id}|{recipe['title']}|{recipe['ingredients']}|{recipe['instructions']}\n")








# Aleksi Kesälä
# RecipeBooks Recipe part
# This searches from recipes.json and writes recipes in recipes.json.
# DO NOT DO ANY CHANGES HERE ANY MORE EVER NEVER

class Recipe:
    def __init__(self, name, category, ingredients, instructions):
        self.name = name
        self.category = category
        self.ingredients = ingredients
        self.instructions = instructions

    def __str__(self):
        return (f"{self.name}\nCategory: {self.category}\nIngredients: {self.ingredients}\nInstructions:"
                f" {self.instructions}")
    
    def to_dictionary(self):
        return {
            'name': self.name,
            'category': self.category,
            'ingredients': self.ingredients,
            'instructions': self.instructions
        }
    
    @staticmethod
    def from_dictionary(data):
        return Recipe(data['name'], data['category'], data['ingredients'], data['instructions'])
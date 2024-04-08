# Aleksi Kesälä
# "Backend of recipebook."
# Icludes methods for loading/reading json, saving, adding, searching, deleting recipes.

import json
from recipe import Recipe

class Recipebook:
    def __init__(self, filename="recipes.json"):
        self.filename = filename
        self.recipes = self.load_recipe()


    def load_recipe(self): # Method for reading recipe in recipes.json
        try:
            with open(self.filename, "r") as file:
                recipes_data = json.load(file)
            recipes =  [Recipe.from_dictionary(recipes_data) for recipes_data in recipes_data]
            return recipes
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading recipes: {e}")
            return []


    def save_recipe(self):  # Method for saving recipe in JSON file recipes.json
        with open(self.filename, 'w') as file:
            json.dump([recipe.to_dictionary() for recipe in self.recipes], file, indent=4)

    
    def list_recipes(self):  # Basic printout method for all recipes
        for recipe in self.recipes:
            print(f"Name: {recipe.name}, category: {recipe.category}")


    def add_recipe(self, recipe):  # THIS HANDLES USERS RECIPE IN BACKEND
        # Checks if recipe exists already. 
        if any(existing_recipe.name == recipe.name for existing_recipe in self.recipes):
            raise ValueError(f"Recipe with name already exists.")
        self.recipes.append(recipe)
        self.save_recipe()

    
    def search_recipe(self, search_keyword):  # Basic search method
        matching_recipes = [recipe for recipe in self.recipes if search_keyword.lower() in recipe.name.lower()]
        return matching_recipes
    
    
    def remove_recipe(self, name):
        for i, recipe in enumerate(self.recipes):
            if recipe.name == name:
                del self.recipes[i]
                self.save_recipe()  # Save changes
                return True
        return False  # False if not found
    
    def get_categories(self):
        categories = set(recipe.category for recipe in self.recipes)
        return list(categories)


    def get_recipes_by_category(self, category):
        return [recipe for recipe in self.recipes if recipe.category.lower() == category.lower()]
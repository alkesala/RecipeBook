# Aleksi Kesälä
# "Backend of recipebook."

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
            return [Recipe.from_dictionary(recipes_data) for recipes_data in recipes_data]
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def save_recipe(self):  # method for saving recipe in JSON file recipes.json
        with open(self.filename, 'w') as file:
            json.dump([recipe.to_dictionary() for recipe in self.recipes], file, indent=4)

    
    def list_recipes(self):  # basic printout method for all recipes
        for recipe in self.recipes:
            print(f"Name: {recipe.name}, category: {recipe.category}")


    def add_recipe(self, recipe):  # THIS HANDLES USERS RECIPE IN BACKEND
        # Checks if recipe exists already. 
        if any(existing_recipe.name == recipe.name for existing_recipe in self.recipes):
            raise ValueError(f"Recipe with name already exists.")
        self.recipes.append(recipe)
        self.save_recipe()

    
    def search_recipe(self, search_keyword):  # basic search method
        matching_recipes = [recipe for recipe in self.recipes if search_keyword.lower() in recipe.name.lower()]
        return matching_recipes
    
    
    def remove_recipe(self, name):
        for i, recipe in enumerate(self.recipes):
            if recipe.name == name:
                del self.recipes[i]
                self.save_recipe()  # save changes
                return True
        return False  # False if not found

    
    def categories(self, category):
        category_recipes = [recipe for recipe in self.recipes if recipe.category.lower() == category.lower()]
        return category_recipes


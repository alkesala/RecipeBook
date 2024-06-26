# Aleksi Kesälä
# Object oriented programming practice work RECIPEBOOK
# "Frontend" of recipebook

from recipe import Recipe
from recipebook import Recipebook


def list_recipes(recipe_book):  # Method for listing all recipe names.
    recipe_book.list_recipes()


def add_recipe(recipe_book):  # Method for adding a new recipe.
    name = input("Enter the name for the recipe: ")
    category = input("Enter a category for the recipe: ")
    ingredients = input("Enter ingredients for the recipe: ")
    instructions = input("Enter instructions for the recipe: ")
    recipe = Recipe(name, category, ingredients, instructions)
    recipe_book.add_recipe(recipe)
    print("Recipe added! Enjoy.")


def search_recipe(recipe_book):  # Searches for a keyword in the recipe book.
    search_keyword = input("Enter recipe name or keyword to search for a recipe: ")
    matching_recipes = recipe_book.search_recipe(search_keyword)
    if len(matching_recipes) == 0:
        print("No recipes found.")
    elif len(matching_recipes) == 1:
        print(matching_recipes[0])
    else:
        print("Found more than one matching recipe, please choose one:")
        for recipe in matching_recipes:
            print(f"{recipe.name}")
        user_choice = input("Please enter the recipe name you choose: ")
        user_recipe = next((recipe for recipe in matching_recipes if recipe.name.lower() == user_choice.lower()), None)
        if user_recipe:
            print(user_recipe)
        else:
            print("No recipes found.")


def remove_recipe(recipe_book):  # Basic remove method.
    name = input("Enter the recipe you want to delete: ")
    if recipe_book.remove_recipe(name):
        print("Recipe removed successfully.")
    else:
        print("Recipe not found.")


def pick_category(recipe_book):
    categories = recipe_book.get_categories()
    if not categories:
        print("No categories available.")
        return

    # prints categories for user
    for i, category in enumerate(categories, start=1):
        print(f"{i}. {category.capitalize()}")

    # users choice
    category_choice = input("Select category: ")
    try:
        category_num = int(category_choice) - 1
        category = categories[category_num]
    except (ValueError, IndexError):
        print("Invalid selection.")
        return

    # get recipes in the chosen category
    recipe_categories = recipe_book.get_recipes_by_category(category)
    if not recipe_categories:
        print("No recipes found in this category.")
        return

    # Display recipes in the chosen category
    for i, recipe in enumerate(recipe_categories, start=1):
        print(f"{i}. {recipe.name}")

    # Get user's recipe choice
    recipe_choice = input("Select a recipe to view details: ")
    try:
        selected_num = int(recipe_choice) - 1
        if 0 <= selected_num < len(recipe_categories):
            selected_recipe = recipe_categories[selected_num]
            print(selected_recipe)  # This will call the __str__ method of Recipe class
        else:
            print("Invalid selection.")
    except ValueError:
        print("Please enter a number.")
 
        
def main():
    recipe_book = Recipebook()

    while True:
        print("\nAleksi's Recipe Book v0.1:")
        print("1. List all recipes")
        print("2. Add a new recipe")
        print("3. Search for a recipe")
        print("4. Remove a recipe")
        print("5. Pick a category")
        print("0. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            list_recipes(recipe_book)
        elif choice == "2":
            add_recipe(recipe_book)
        elif choice == "3":
            search_recipe(recipe_book)
        elif choice == "4":
            remove_recipe(recipe_book)
        elif choice == "5":
            pick_category(recipe_book)
        elif choice == "0":
            print("Thanks for using this application!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
        


    

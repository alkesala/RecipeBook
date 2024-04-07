    # Recipebook can be initialized with a default filename or a custom one
    
class Recipebook:
    def __init__(self, filename="recipes.json"):
        self.filename = filename
        self.recipes = self.load_recipe()
    
    
    def test_initialize_with_default_filename(self):
        recipebook = Recipebook()
        assert recipebook.filename == "recipes.json"
    
    
        # Recipebook can be initialized with a default filename or a custom one
    def test_initialize_with_custom_filename(self):
        recipebook = Recipebook("custom_recipes.json")
        assert recipebook.filename == "custom_recipes.json"
        
    
        # Recipebook can handle loading an empty JSON file
    def test_load_empty_json_file(self):
        with open("empty_recipes.json", "w") as file:
            file.write("[]")
        recipebook = Recipebook("empty_recipes.json")
        assert len(recipebook.recipes) == 0
        
        
class Recipe:
        # Recipe object can be created with valid name, category, ingredients, and instructions
    def test_valid_recipe_creation(self):
        name = "Chocolate Cake"
        category = "Dessert"
        ingredients = ["flour", "sugar", "cocoa powder", "baking powder", "eggs", "milk", "vegetable oil"]
        instructions = "1. Preheat the oven. 2. Mix the dry ingredients. 3. Add the wet ingredients. 4. Bake the cake."
    
        recipe = Recipe(name, category, ingredients, instructions)
    
        assert recipe.name == name
        assert recipe.category == category
        assert recipe.ingredients == ingredients
        assert recipe.instructions == instructions
        
    def test_empty_recipe_creation(self):
        recipe_data = {
            'name': '',
            'category': 'Dessert',
            'ingredients': ['flour', 'sugar', 'cocoa powder', 'baking powder', 'eggs', 'milk', 'vegetable oil'],
            'instructions': '1. Preheat the oven. 2. Mix the dry ingredients. 3. Add the wet ingredients. 4. Bake the cake.'
        }

        recipe = Recipe.from_dictionary(recipe_data)

        assert recipe.to_dictionary() == recipe_data
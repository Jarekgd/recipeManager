class Recipe:
    def __init__(self):
        self._name = None
        self._ingredients = None
        self._description = None

    def set_name(self, name):
        self._name = name.strip()

    def set_ingredients(self, ingredients):
        self._ingredients = [ingredient.strip() for ingredient in ingredients]

    def set_description(self, description):
        self._description = description.strip()

    def get_name(self):
        return self._name

    def get_ingredients(self):
        return self._ingredients

    def get_description(self):
        return self._description

    def __str__(self):
        return f"Name: {self._name}\nIngredients: {', '.join(self._ingredients)}\nDescription: {self._description}"


class ManageRecipe:
    def __init__(self):
        self.recipes = []

    def add_recipe(self, recipe):
        self.recipes.append(recipe)

        with open("recipes.txt", "a") as file:
            file.write(str(recipe) + "\n")

    def delete_recipe(self, recipe_name):
        deleted = False
        with open("recipes.txt", "r") as file:
            lines = file.readlines()
        with open("recipes.txt", "w") as file:
            for line in lines:
                if f"Name: {recipe_name}" not in line:
                    file.write(line)
                else:
                    deleted = True

        self.recipes = [recipe for recipe in self.recipes if recipe.get_name() != recipe_name]
        return deleted

    def edit_recipe(self, recipe_name, new_name, new_ingredients, new_description):
        for recipe in self.recipes:
            if recipe.get_name() == recipe_name:
                recipe.set_name(new_name)
                recipe.set_ingredients(new_ingredients)
                recipe.set_description(new_description)

        with open("recipes.txt", "w") as file:
            for recipe in self.recipes:
                file.write(str(recipe) + "\n")

    def show_recipes(self):
        if not self.recipes:
            print("No recipes found.")
        else:
            for recipe in self.recipes:
                print(recipe)

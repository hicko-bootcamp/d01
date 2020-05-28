

class Recipe():
    def __init__(self, name, cooking_lvl, cooking_time,
                 ingredients, description, recipe_type):
        if not isinstance(name, str):
            raise TypeError("name must be type of str")
        if name == "":
            raise ValueError("name must not be empty")
        if not isinstance(cooking_lvl, int):
            raise TypeError("cooking_lvl must be type of int")
        if not 1 <= cooking_lvl <= 5:
            raise ValueError("cooking_lvl must be in range 1 to 5")
        if not isinstance(cooking_time, int):
            raise TypeError("cooking_time must be type of int")
        if cooking_time < 0:
            raise ValueError("cooking_time cannot be negative")
        if not isinstance(ingredients, list):
            raise TypeError("ingredients must be a list of str")
        ingredients = list(filter(len, ingredients))
        if len(ingredients) == 0:
            raise ValueError("ingredients must contain"
                             " at least 1 not empty element")
        for elem in ingredients:
            if not isinstance(elem, str):
                raise TypeError("ingredients must contains only strings")
        if not isinstance(description, str):
            raise TypeError("description must be type of str")
        if not isinstance(recipe_type, str):
            raise TypeError("recipe_type must be type of str")
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("recipe_type must not be empty and must be "
                             "one of the following: starter, lunch or dessert")
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "name = " + self.name + "\n"
        txt += "cooking_lvl = " + str(self.cooking_lvl) + "\n"
        txt += "cooking_time = " + str(self.cooking_time) + "\n"
        txt += "ingredients = " + str(self.ingredients) + "\n"
        txt += "description = " + self.description + "\n"
        txt += "recipe_type = " + self.recipe_type + "\n"
        return txt

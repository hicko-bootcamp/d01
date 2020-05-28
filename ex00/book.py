from recipe import Recipe
from datetime import datetime


class Book():
    def __init__(self, name, recipes_list=list()):
        if not isinstance(name, str):
            raise TypeError("name must be type of str")
        if name == "":
            raise ValueError("name must not be empty")
        if not isinstance(recipes_list, list):
            raise TypeError("recipes_list must be type of list")
        for elem in recipes_list:
            if not isinstance(elem, Recipe):
                raise TypeError("elements of recipes_list"
                                " must be type of Recipe")
        self.name = name
        self.recipes_list = self.__sort_by_type(recipes_list)
        self.creation_date = datetime.now()
        self.last_update = datetime.now()

    def __sort_by_type(self, recipes_list):
        starter = list(filter(lambda item: item.recipe_type == "starter",
                              recipes_list))
        lunch = list(filter(lambda item: item.recipe_type == "lunch",
                            recipes_list))
        dessert = list(filter(lambda item: item.recipe_type == "dessert",
                              recipes_list))
        recipes_dict = {"starter": starter,
                        "lunch": lunch,
                        "dessert": dessert
                        }
        return recipes_dict

    def get_recipe_by_name(self, name):
        """Print a recipe with the name `name` and return the instance"""
        for key in self.recipes_list:
            for recipe in self.recipes_list[key]:
                if recipe.name == name:
                    print(str(recipe))
                    return recipe
        print("there is no recipe with that name")

    def get_recipes_by_types(self, recipe_type):
        """Get all recipe names for a given recipe_type """
        if recipe_type not in ['starter', 'lunch', 'dessert']:
            raise ValueError("recipe_type must not be empty and must be "
                             "one of the following: starter, lunch or dessert")
        print(str(len(self.recipes_list[recipe_type])) + " recipe(s) found ")
        for recipe in self.recipes_list[recipe_type]:
            print(str(recipe))

    def add_recipe(self, recipe: Recipe):
        """Add a recipe to the book and update last_update"""
        if not isinstance(recipe, Recipe):
            raise TypeError("recipe must be type of Recipe")
        self.recipes_list[recipe.recipe_type].append(recipe)
        self.last_update = datetime.now()

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt += "name = " + self.name + "\n"
        txt += "creation_date = " + str(self.creation_date) + "\n"
        txt += "last_update = " + str(self.last_update) + "\n"
        txt += "recipes_lists :\n\n"
        for key in self.recipes_list:
            for elem in self.recipes_list[key]:
                txt += str(elem) + "\n"
        return txt

from book import Book
from recipe import Recipe

recette1 = Recipe("corona soup", 3, 15, ["eau", "chauve-souris", "pangolin"],
                  "WTF", "lunch")
recette2 = Recipe("horse lasagna", 1, 70, ["viande de cheval", "bechamel",
                  "tomate", "merde de votre choix"],
                  "Naturellement il y Findus", "lunch")
recette3 = Recipe("vent", 1, 0, ["R"], "", "starter")
recette4 = Recipe("mousse au quelque chose", 5, 20, ["des", "trucs"],
                  "j'ai plus d'inspi. RIP", "dessert")

liste = [recette1, recette2, recette3]

book_vide = Book("non")
print("le book vide :\n")
print(str(book_vide))


book = Book("ouai", liste)
print("book préremplie:\n")
print(str(book))

print("appel de get_recipe_by_name(corona soup):\n")
recette_recuperer = book.get_recipe_by_name("corona soup")

print("return du get_recipe_by_name(corona soup):\n")
print(str(recette_recuperer))

print("get_recipes_by_types(lunch):\n")
book.get_recipes_by_types("lunch")


book.add_recipe(recette4)
print("resultat après ajout d'une recette :\n")
print(book.__str__())

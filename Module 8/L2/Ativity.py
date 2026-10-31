# Create Tuples for recipe details (fixed - cannot be changed)
pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1: ", pasta)
print("Name: ", pasta[0])
print("Cuisine: ", pasta[1])
print("Difficulty: ", pasta[-1])
# Nested tuples and slicing
all_recipes = (pasta, biryani)
print("\nFirst recipe name: ", all_recipes[0][0])
print("Second recipe name: ", all_recipes[1][2])
print("Pasta details (sliced): ", pasta[1:3])
# Iterate through a tuple
print("\nPasta Recipe details: ")
for details in pasta:
    print(" _", details)

pasta_ingredients = {"tomato", "garlic", "olive oil", "chilli", "pasta", "garlic"}
biryani_ingredients = {"rice", "chicken", "garlic", "onion", "tomato", "spices"}
print("\nPasta Ingredients:", pasta_ingredients)
print("Biryani Ingredients:", biryani_ingredients)
print("Total pasta Ingredients:", len(pasta_ingredients))

pasta_ingredients.add("parmesan")
pasta_ingredients.discard("chilli")
print("\nUpdated pats ingredients:", pasta_ingredients)

all_ingredients = pasta_ingredients.union(biryani_ingredients)
common = pasta_ingredients.intersection(biryani_ingredients)
only_pasta = pasta_ingredients.difference(biryani_ingredients)
unique_to_each = pasta_ingredients.symmetric_difference(biryani_ingredients)

print("\nAll ingredients (union):", all_ingredients)
print("Common ingredients (intersection):", common)
print("Only in pasta (difference):", only_pasta)
print("Not shared (sym.difference):", unique_to_each)
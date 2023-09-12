import tkinter as tk
from tkinter import messagebox
from recipe import Recipe, ManageRecipe


def main():
    use_gui = input("Do you want to use GUI? (y/n): ")
    if use_gui.lower() == 'y':
        gui_main()
    else:
        console_main()


def console_main():
    manage_recipe = ManageRecipe()
    while True:
        print("\n1. Add Recipe and Save\n2. Show Recipes\n3. Edit Recipe\n4. Delete Recipe\n5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            recipe = Recipe()
            name = input("Enter the recipe name: ")
            recipe.set_name(name)

            ingredients = input("Enter the ingredients (separated by commas): ").split(',')
            recipe.set_ingredients(ingredients)

            description = input("Enter the recipe description: ")
            recipe.set_description(description)

            manage_recipe.add_recipe(recipe)
            print("Recipe added and saved successfully!\n")
        elif choice == "2":
            manage_recipe.show_recipes()
        elif choice == "3":
            recipe_name = input("Enter the name of the recipe to edit: ")
            new_name = input("Enter the new recipe name: ")
            new_ingredients = input("Enter the new ingredients (separated by commas): ").split(',')
            new_description = input("Enter the new recipe description: ")

            manage_recipe.edit_recipe(recipe_name, new_name, new_ingredients, new_description)
            print(f"Recipe '{recipe_name}' edited successfully!\n")
        elif choice == "4":
            recipe_name = input("Enter the name of the recipe to delete: ")
            if manage_recipe.delete_recipe(recipe_name):
                print(f"Recipe '{recipe_name}' deleted successfully!\n")
            else:
                print(f"Recipe '{recipe_name}' not found!\n")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


def gui_add_recipe():
    recipe = Recipe()

    name = name_entry.get()
    recipe.set_name(name)

    ingredients = ingredients_entry.get().split(',')
    recipe.set_ingredients(ingredients)

    description = description_text.get("1.0", tk.END)
    recipe.set_description(description)

    manage_recipe.add_recipe(recipe)

    messagebox.showinfo("Success", "Recipe added and saved successfully!")


def gui_edit_recipe():
    recipe_name = edit_entry.get()
    new_name = new_name_entry.get()
    new_ingredients = new_ingredients_entry.get().split(',')
    new_description = new_description_text.get("1.0", tk.END)

    manage_recipe.edit_recipe(recipe_name, new_name, new_ingredients, new_description)

    messagebox.showinfo("Success", f"Recipe '{recipe_name}' edited successfully!")


def gui_delete_recipe():
    recipe_name = delete_entry.get()
    if manage_recipe.delete_recipe(recipe_name):
        messagebox.showinfo("Success", f"Recipe '{recipe_name}' deleted successfully!")
    else:
        messagebox.showinfo("Error", f"Recipe '{recipe_name}' not found!")


def gui_main():
    root = tk.Tk()
    root.title("Recipe Management System")

    recipe_frame = tk.Frame(root)
    recipe_frame.pack(padx=20, pady=10)

    name_label = tk.Label(recipe_frame, text="Recipe Name:")
    name_label.grid(row=0, column=0, sticky=tk.W)
    name_entry = tk.Entry(recipe_frame)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    ingredients_label = tk.Label(recipe_frame, text="Ingredients:")
    ingredients_label.grid(row=1, column=0, sticky=tk.W)
    ingredients_entry = tk.Entry(recipe_frame)
    ingredients_entry.grid(row=1, column=1, padx=5, pady=5)

    description_label = tk.Label(recipe_frame, text="Description:")
    description_label.grid(row=2, column=0, sticky=tk.W)
    description_text = tk.Text(recipe_frame, width=30, height=5)
    description_text.grid(row=2, column=1, padx=5, pady=5)

    add_button = tk.Button(root, text="Add Recipe and Save", command=gui_add_recipe)
    add_button.pack(pady=10)

    edit_frame = tk.Frame(root)
    edit_frame.pack(padx=20, pady=10)

    edit_label = tk.Label(edit_frame, text="Recipe Name to Edit:")
    edit_label.grid(row=0, column=0, sticky=tk.W)
    edit_entry = tk.Entry(edit_frame)
    edit_entry.grid(row=0, column=1, padx=5, pady=5)

    new_name_label = tk.Label(edit_frame, text="New Recipe Name:")
    new_name_label.grid(row=1, column=0, sticky=tk.W)
    new_name_entry = tk.Entry(edit_frame)
    new_name

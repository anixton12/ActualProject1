# application_gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
from recipe_manager import RecipeManager

class ApplicationGUI:
    def __init__(self, master):
        self.manager = RecipeManager()
        self.master = master
        self.master.title('Recipe Management')
        self.setup_ui()

    def setup_ui(self):
        tk.Label(self.master, text="Recipe Management System", font=("Arial", 16, "bold")).pack(pady=(10, 20))
        tk.Button(self.master, text='Add Recipe', command=self.add_recipe, font=("Arial", 12), relief=tk.RAISED, borderwidth=2).pack(fill=tk.X, padx=50, pady=5)
        tk.Button(self.master, text='View Recipes', command=self.view_recipes, font=("Arial", 12), relief=tk.RAISED, borderwidth=2).pack(fill=tk.X, padx=50, pady=5)

    def add_recipe(self):
        title = simpledialog.askstring("Recipe Title", "Enter the recipe title:")
        ingredients = simpledialog.askstring("Ingredients", "List ingredients separated by commas:")
        instructions = simpledialog.askstring("Instructions", "Describe the preparation steps:")
        if title and ingredients and instructions:
            self.manager.add_recipe(title, ingredients, instructions)
            messagebox.showinfo('Success', 'Recipe added successfully')
        else:
            messagebox.showerror('Error', 'All fields are required')

    def view_recipes(self):
        window = tk.Toplevel(self.master)
        window.title("View Recipes")
        text_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
        text_area.pack(padx=10, pady=10)
        text_area.insert(tk.INSERT, self.format_recipes())
        text_area.config(state=tk.DISABLED)

    def format_recipes(self):
        formatted_text = ""
        for id, recipe in self.manager.recipes.items():
            formatted_text += f"Recipe ID: {id}\nTitle: {recipe['title']}\nIngredients: {recipe['ingredients']}\nInstructions: {recipe['instructions']}\n\n"
        return formatted_text if formatted_text else "No recipes available."

def main():
    root = tk.Tk()
    app = ApplicationGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()



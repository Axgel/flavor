from flask import Flask, render_template, request, session, url_for, redirect
from model import stringSplit, getRecipeData2
# import config
import requests
from datetime import datetime, timezone
import os


app = Flask(__name__)
app.jinja_env.globals['current_time'] = datetime.now()

API_KEY_SPOON = os.getenv("API_KEY_SPOON")
# API_KEY_SPOON = config.API_KEY_SPOON
app.secret_key = API_KEY_SPOON

@app.route('/')
def homePage():
    return render_template('index.html')


# directs to different homepage options based on what is clicked
recipe_data = dict()

@app.route('/recipe', methods=["GET", "POST"])
def recipe():
    ingredients = request.form["recipes"]
    numOfRecipes = 10
    ingredList = stringSplit(ingredients)
    recipe_link = f"https://api.spoonacular.com/recipes/findByIngredients?apiKey={API_KEY_SPOON}&ingredients={ingredList}&number={numOfRecipes}"
    global recipe_data
    recipe_data = getRecipeData2(recipe_link, numOfRecipes)
    session["recipe_data"] = recipe_data
    if request.method == 'GET':
        return render_template("food_recipe.html", recipe_data=recipe_data)
    else:
        return render_template("recipe2.html", recipe_data=recipe_data)



@app.route('/recipe/<string:recipeID>', methods=["GET", "POST"])
def recipeInfo(recipeID):
    if request.method == "GET":
        print(recipe_data)
        session["recipe_data"] = recipe_data
        return render_template("food_recipe.html", recipe_data=recipe_data, recID=recipeID)
    return 1

if __name__ == '__main__':
    app.run()

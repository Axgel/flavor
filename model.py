import re

import requests
import config

API_KEY_SPOON = config.API_KEY_SPOON


def stringSplit(ingredients):
    # Input ingredients, formats them properly
    splitIngred = ingredients.split(',')
    queryFormat = ""
    for ingred in splitIngred:
        queryFormat += ingred.strip() + ",+"
    queryFormat = queryFormat[:-2]
    return queryFormat


"""
def getRecipeData(recipe_link, numOfRecipes):
    # Returns recipe data with name, id, image, and ingredients
    recipe_request_data = list()
    recipe_data = dict()
    recipe_requests = requests.get(recipe_link).json()
    recipe_request_data.append(recipe_requests)
    for num in range(int(numOfRecipes)):
        recipe_data[recipe_request_data[0][num]["title"]] = {"id":recipe_request_data[0][num]["id"],  "image":recipe_request_data[0][num]["image"], "ingredients":""}
        counter = recipe_request_data[0][num]["usedIngredientCount"]
        ingredients_list = []
        addOne = 0
        while counter > 0:
            ingredients_list.append(recipe_request_data[0][num]["usedIngredients"][addOne]["originalString"])
            counter -= 1
            addOne += 1
        counter = recipe_request_data[0][num]["missedIngredientCount"]
        addOne = 0
        while counter > 0:
            ingredients_list.append(recipe_request_data[0][num]["missedIngredients"][addOne]["originalString"])
            counter -= 1
            addOne += 1
        recipe_data[recipe_request_data[0][num]["title"]].update({"ingredients":ingredients_list})

        instruction_request_data = []
        instruction_link = "https://api.spoonacular.com/recipes/"+str(recipe_request_data[0][num]["id"])+f"/information?includeNutrition=false&apiKey={API_KEY_SPOON}"
        instruction_request = requests.get(instruction_link).json()
        instruction_request_data.append(instruction_request)
        instruction_list = []
        print(instruction_request["analyzedInstructions"])
        if not (instruction_request_data[0]["analyzedInstructions"]):
            continue
        counter = len(instruction_request_data[0]["analyzedInstructions"][0]["steps"])
        addOne = 0
        while counter > 0:
            instruction_list.append(instruction_request_data[0]["analyzedInstructions"][0]["steps"][addOne]["step"])
            addOne += 1
            counter -= 1
        recipe_data[recipe_request_data[0][num]["title"]].update({"instructions":instruction_list})

    return recipe_data
"""


def getRecipeData2(recipe_link, numOfRecipes):
    # Loads the link and calls the api
    recipe_requests = requests.get(recipe_link).json()
    recipe_data = dict()

    for num in range(int(numOfRecipes)):
        # Adds the title, id, and image to a dictionary
        ingredient_list = list()
        recipe_data[recipe_requests[num]["title"]] = {"id": recipe_requests[num]["id"],
                                                      "image": recipe_requests[num]["image"], "ingredients": "",
                                                      "instructions": "n/a",
                                                      "summary":"Summary not available. Click to learn more"}
        for i in range(recipe_requests[num]["usedIngredientCount"]):
            ingredient_list.append(recipe_requests[num]["usedIngredients"][i]["originalString"])
        for i in range(recipe_requests[num]["missedIngredientCount"]):
            ingredient_list.append(recipe_requests[num]["missedIngredients"][i]["originalString"])
        recipe_data[recipe_requests[num]["title"]].update({"ingredients": ingredient_list})

        # Instructions link and calls api
        instruction_list = list()
        instruction_link = "https://api.spoonacular.com/recipes/" + str(recipe_requests[num]["id"]) + f"/information?includeNutrition=false&apiKey={API_KEY_SPOON}"
        instruction_request = requests.get(instruction_link).json()

        # adds the instructions to the recipe data
        if not instruction_request["analyzedInstructions"]:
            continue
        for i in range(len(instruction_request["analyzedInstructions"][0]["steps"])):
            instruction_list.append(instruction_request["analyzedInstructions"][0]["steps"][i]["step"])
        recipe_data[recipe_requests[num]["title"]].update({"instructions": instruction_list})
        if not instruction_request["summary"]:
            continue
        summary = parseString(instruction_request["summary"])
        recipe_data[recipe_requests[num]["title"]].update({"summary": summary})
    return recipe_data


def getCoords(geocode_link):
    geocode_requests = requests.get(geocode_link).json()
    coords = dict()
    coords["address"] = geocode_requests["results"][0]["formatted_address"]
    coords["lat"] = geocode_requests["results"][0]["location"]["lat"]
    coords["long"] = geocode_requests["results"][0]["location"]["lng"]
    return coords

def parseString(summary):
    modified_string = re.sub('<[^>]+>', '', summary)
    return modified_string

"""
- Get long and lat using the geocode api
- Using zomato, generate a list of diff nearby resturants
    - Display address of resturant, 
- Using google api create a map and pin point the locations on the map, centered around the long and lat of the geocode api

"""

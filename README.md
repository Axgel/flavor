# flavor

About: This will allow you to enter any ingredients, and it will show all possible recipes/food items you can make with it that includes the ingredients, instructions, estimate preparation time, and many more!

Check out the website <a href="https://flavordemo.herokuapp.com/">here!</a>
Note: Website may not work depending on how many API calls it has done for the day. I am using a free API key from spoonacular and it only limits me to 150 calls per day. As a result, the website may not work if it has been called 150 times already for the day.

# API Resource
The API that I am using is https://spoonacular.com/food-api. You can create a free account and get an authentication key. You will need this for the program to work. Since API Keys are meant to be a secret, I have added mine to a .env file so when I push to github, it keeps my key secret and safe. I have added a comment "API key initizalized here" in the app.py to where the API Key is defined and located to be referenced later on in my code.

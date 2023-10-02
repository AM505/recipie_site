import os
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    data=[]
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
    return render_template("index.html", recipes=data)

@app.route("/<recipe_name>")
def recipe(recipe_name):
    recipe = {}
    with open("data/recipes.json", "r") as json_data:
        data = json.load(json_data)
        for obj in data:
            if obj["recipe_url"] == recipe_name:
                recipe = obj
    return "<h1></h1>"
    

if __name__ == "__main__":
    app.run(
        host=os.environ.get("IP", "0.0.0.0"),
        port=int(os.environ.get("PORT", "5000")),
        debug=True
    )
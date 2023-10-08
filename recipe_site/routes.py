from flask import ( render_template, 
    redirect, request, session, url_for)
from recipe_site import app,  db
from recipe_site.models import User, Recipe

@app.route("/")
@app.route("/index")
def index():
    categories = list(Recipe.query.order_by(Recipe.recipe_name).all())
    return render_template("base.html")

@app.route("/admin_recipe", methods=["GET", "POST"])
def admin_recipie():
    return render_template("admin_recipie.html")

@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        ## get all post vars and stuff
        print("nothin to see here")
    return render_template("admin_recipe.html")

## lets do user login 
@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/register")
def register():
    return render_template('register.html')


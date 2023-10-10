from flask import ( render_template, 
    redirect, request, session, url_for, flash)
from recipe_site import app,  db
from recipe_site.models import User, Recipe

@app.route("/")
@app.route("/index")#, defaults={'username': None}
def index():
    recipes = list(Recipe.query.order_by(Recipe.recipe_name).all())
    return render_template("index.html", recipes=recipes)

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
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        existing_user = User.query.filter_by(username=request.form.get("username")).first()   
    
        if existing_user:
            if existing_user.check_password(request.form.get("password")):
                session["user"] = request.form.get("username")
                session["is_admin"] = request.form.get("is_admin")
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for("index", username=session["user"]))

            else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
        else:
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))
    return render_template('login.html')

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        #check if user exists in db

        existing_user = User.query.filter_by(username=request.form.get("username")).first()        
        if existing_user:
            flash ("Username already exists")
            return redirect(url_for("login"))
        
        user = User(username=request.form.get("username"), is_admin=False)
        user.set_password(request.form.get("password"))
        db.session.add(user)
        db.session.commit()
        session["user"] = request.form.get("username")
        flash("Registration successful")
        return redirect(url_for("index", username=session["user"]))
    return render_template("register.html")


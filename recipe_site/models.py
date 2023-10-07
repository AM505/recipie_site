from recipe_site import db

class Recipe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    recipe_name = db.Column(db.String(50), unique=True, nullable=False)
    recipe_stars = db.Column(db.Integer, nullable=False)
    recipe_description = db.Column(db.Text, nullable=False)
    recipe_ingredients = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
          return super().__repr__()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)
    def __repr__(self) -> str:
          return super().__repr__()
        
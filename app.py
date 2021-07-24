import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Create instance of Flask
app = Flask(__name__)

# Set up configurations for MongoDB
app.config["MONGO_DBASE"] = os.environ.get("MONGO_DBASE")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Set up secret key
app.secret_key = os.environ.get("SECRET_KEY")

# Create an instance of PyMongo
mongo = PyMongo(app)


# All Recipes
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("recipes.html", recipes=recipes)


# Search Recipes
@app.route("/regex", methods=["GET", "POST"])
def regex():
    query = request.form.get("query")
    print("query is ", query)
    # recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    recipes = list(mongo.db.recipes.find({"ingredients": {
        "$regex": query, "$options": "i"}}))
    print("recipes is ", recipes)
    return render_template("recipes.html", recipes=recipes)


# Register a New User
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please choose another")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        # Add new user to the db
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# Log In Existing User
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
             existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(
                    request.form.get("username")))
                return redirect(url_for(
                    "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


# Profile Username
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's name from database
    username = mongo.db.users.find_one({
        "username": session["user"]})["username"]

    # Once session['user] cookie is truthy return their profile page
    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


# Log Out
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Add Recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    if request.method == "POST":
        recipe = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "method": request.form.getlist("method"),
            "ingredients": request.form.getlist("ingredients"),
            "added_by": session["user"],
            "image_url": request.form.get("image_url"),
            "calories": request.form.get("calories"),
            "serves": request.form.get("serves")
        }
        mongo.db.recipes.insert_one(recipe)
        flash("Recipe Added Succesfully")
        return redirect(url_for("get_recipes"))

    categories = mongo.db.categories.find().sort("name", 1)
    return render_template("add_recipe.html", categories=categories)


# Edit Recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):
    if request.method == "POST":
        print("CATEGORY NAME: ", request.form.get("category_name"))
        submit = {
            "category_name": request.form.get("category_name"),
            "name": request.form.get("name"),
            "description": request.form.get("description"),
            "method": request.form.getlist("method"),
            "ingredients": request.form.getlist("ingredients"),
            "added_by": session["user"],
            "image_url": request.form.get("image_url"),
            "calories": request.form.get("calories"),
            "serves": request.form.get("serves")
        }
        mongo.db.recipes.update_one(
            {"_id": ObjectId(recipe_id)}, {"$set": submit})
        flash("Recipe Updated Succesfully")

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("name", 1)
    return render_template(
        "edit_recipe.html", recipe=recipe, categories=categories)


# Delete Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Deleted Successfully")
    return redirect(url_for("get_recipes"))


# Manage Categories
@app.route("/get_categories")
def get_categories():
    categories = list(mongo.db.categories.find().sort("name", 1))
    return render_template("categories.html", categories=categories)


# Add Category
@app.route("/add_category", methods=["GET", "POST"])
def add_category():
    if request.method == "POST":
        category = {
            "name": request.form.get("name")
        }
        mongo.db.categories.insert_one(category)
        flash("New Category Added")
        return redirect(url_for("get_categories"))

    return render_template("add_category.html")


# Edit Category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):
    if request.method == "POST":
        submit = {
            "name": request.form.get("name")
        }
        mongo.db.categories.update(
            {"_id": ObjectId(category_id)}, submit)
        flash("Category Updated Successfully")
        return redirect(url_for("get_categories"))

    category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
    return render_template("edit_category.html", category=category)


# Delete Category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):
    mongo.db.categories.remove({"_id": ObjectId(category_id)})
    flash("Category Deleted Successfully")
    return redirect(url_for("get_categories"))


# Set how & where to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

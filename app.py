import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_mail import Mail, Message
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from flask_paginate import Pagination, get_page_args
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

# Create instance of Flask
app = Flask(__name__)

# Create an instance of the Mail class
mail = Mail(app)

# Configure server parameters
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'webdeveloperevakukla@gmail.com'
app.config['MAIL_PASSWORD'] = os.environ.get("MY_EMAIL_PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)


# Set up configurations for MongoDB
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBASE")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
# Set up secret key
app.secret_key = os.environ.get("SECRET_KEY")

# Create an instance of PyMongo
mongo = PyMongo(app)

# CREDIT: Edb83 https://github.com/Edb83/self-isolution/blob/master/app.py
PER_PAGE = 8


def paginated(recipes):
    page, per_page, offset = get_page_args(
        page_parameter='page',
        per_page_parameter='per_page')
    offset = page * PER_PAGE - PER_PAGE
    return recipes[offset: offset + PER_PAGE]


def pagination_args(recipes):
    page, per_page, offset = get_page_args(
        page_parameter='page',
        per_page_parameter='per_page')
    total = len(recipes)

    return Pagination(page=page, per_page=PER_PAGE, total=total)
# End of credit


# All Recipes
@app.route("/")
@app.route("/get_recipes")
def get_recipes():
    recipes = list(mongo.db.recipes.find())
    categories = list(mongo.db.categories.find())
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "recipes.html", categories=categories, recipes=recipes_paginated,
        pagination=pagination, search=True)


# Search Recipes
@app.route("/regex", methods=["GET", "POST"])
def regex():
    query = request.form.get("query")
    # recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    recipes = list(mongo.db.recipes.find({"ingredients": {
        "$regex": query, "$options": "i"}}))
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "recipes.html", recipes=recipes_paginated,
        pagination=pagination, title="Search Results", search=True)


# Display Recipes By Category
@app.route("/categories/<name>")
def categories(name):
    recipes = list(mongo.db.recipes.find(
        {"category_name": name}).sort("_id", -1))
    categories = list(mongo.db.categories.find())
    recipes_paginated = paginated(recipes)
    pagination = pagination_args(recipes)
    return render_template(
        "recipes.html",
        name=name,
        categories=categories, title=name,
        recipes=recipes_paginated,
        pagination=pagination, search=True)


# Utensils page to dysplay kitchen tools for smoothies
@app.route("/utensils")
def utensils():
    categories = list(mongo.db.categories.find())
    return render_template(
        "utensils.html", categories=categories, title="Utensils")


# Register a New User
@app.route("/register", methods=["GET", "POST"])
def register():
    categories = list(mongo.db.categories.find())
    if request.method == "POST":
        # check if username already exists in database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists, please choose another")
            return redirect(url_for("register"))

        # confirm password
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        if password == confirm_password:
            register = {
                "username": request.form.get("username").lower(),
                "password": generate_password_hash(
                    request.form.get("password")),
            }

            # Add new user to the db
            mongo.db.users.insert_one(register)

            # put the new user into 'session' cookie
            session["user"] = request.form.get("username").lower()
            flash("Welcome, {}".format(
                request.form.get("username")), "success")
            return redirect(url_for("profile", username=session["user"]))
        else:
            flash(("Password doesn't match, try again"))
            return redirect(url_for("register"))

    return render_template("register.html", categories=categories)


# Log In Existing User
@app.route("/login", methods=["GET", "POST"])
def login():
    categories = list(mongo.db.categories.find())
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
                flash("Username or password is incorrect")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Username or password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html", categories=categories)


# Profile Username
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Get the session user's name from database
    username = mongo.db.users.find_one({
        "username": session["user"]})["username"]
    categories = list(mongo.db.categories.find())

    # Once session['user] cookie is truthy return their profile page
    # Display recipes added by the current user to his profile
    if session["user"]:
        recipes = list(mongo.db.recipes.find(
            {"added_by": session["user"]}).sort("_id", -1))
        recipes_paginated = paginated(recipes)
        pagination = pagination_args(recipes)
        return render_template(
            "profile.html", username=username,
            categories=categories, title="Profile",
            recipes=recipes_paginated,
            pagination=pagination, search=True)

    return redirect(url_for("login"))


# Log Out
@app.route("/logout")
def logout():
    # remove user from session cookies
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


# Contact
@app.route("/contact", methods=["GET", "POST"])
def contact():
    categories = list(mongo.db.categories.find())
    if request.method == "POST":
        email = request.form.get("email")
        message = request.form.get("message")

        msg = Message('Hello',
                      sender=("Smoothie Lovers", email),
                      recipients=['webdeveloperevakukla@gmail.com'])

        msg.body = message
        mail.send(msg)
        flash("Email Sent Successfully")
        return redirect(url_for("contact"))

    return render_template("contact.html", categories=categories)


# Display Single recipe
@app.route("/recipe/<recipe_id>")
def recipe(recipe_id):
    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = list(mongo.db.categories.find())
    return render_template(
        "recipe.html", recipe=recipe, categories=categories, name=recipe)


# Add Recipe
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():

    # Only logged in user is allowed to add a recipe
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

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
        return redirect(url_for("profile", username=session["user"]))

    categories = list(mongo.db.categories.find().sort("name", 1))
    return render_template("add_recipe.html", categories=categories)


# Edit Recipe
@app.route("/edit_recipe/<recipe_id>", methods=["GET", "POST"])
def edit_recipe(recipe_id):

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})
    categories = list(mongo.db.categories.find().sort("name", 1))

    # Only a logged in user or admin can edit the recipe added by themself
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == recipe["added_by"] or session["user"] == "admin":

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
            return redirect(url_for("profile", username=session["user"]))

        return render_template(
            "edit_recipe.html", recipe=recipe, categories=categories)
    else:
        flash("Access denied. You don't have permission")
        return render_template("403.html")


# Delete Recipe
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):

    recipe = mongo.db.recipes.find_one({"_id": ObjectId(recipe_id)})

    # Only a logged in user or admin can delete added by themself recipe
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == recipe["added_by"] or session["user"] == "admin":
        mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
        flash("Recipe Deleted Successfully")
        return redirect(url_for("profile", username=session["user"]))

    else:
        flash("Access denied. You don't have permission")
        return render_template("403.html")


# Manage Categories: only admin has access to this page
@app.route("/get_categories")
def get_categories():

    categories = list(mongo.db.categories.find().sort("name", 1))

    # Only a logged in admin can have access  to the category
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session['user'] == 'admin':
        return render_template("categories.html", categories=categories)
    else:
        flash("You have to be an Admin to access this page")
        return render_template("403.html")


# Add Category allow admin to add new category to db
@app.route("/add_category", methods=["GET", "POST"])
def add_category():

    # Only  logged in admin can add the category
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session['user'] == 'admin':

        if request.method == "POST":
            category = {
                "name": request.form.get("name"),
                "description": request.form.get("description")
            }
            mongo.db.categories.insert_one(category)
            flash("New Category Added")
            return redirect(url_for("get_categories"))

        return render_template("add_category.html")

    else:
        flash("You have to be an Admin to access this page")
        return render_template("403.html")


# Edit Category allows admin to edit category
@app.route("/edit_category/<category_id>", methods=["GET", "POST"])
def edit_category(category_id):

    # Only a logged in admin can edit the category
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session['user'] == 'admin':

        if request.method == "POST":
            submit = {
                "name": request.form.get("name"),
                "description": request.form.get("description")
            }
            mongo.db.categories.update(
                {"_id": ObjectId(category_id)}, submit)
            flash("Category Updated Successfully")
            return redirect(url_for("get_categories"))

        category = mongo.db.categories.find_one({"_id": ObjectId(category_id)})
        return render_template("edit_category.html", category=category)

    else:
        flash("You have to be an Admin to access this page")
        return render_template("403.html")


# Delete Category allows admin to delete category
@app.route("/delete_category/<category_id>")
def delete_category(category_id):

    # Only a logged in admin can delete the category
    if "user" not in session:
        flash("Please Log In")
        return redirect(url_for("login"))

    if session["user"] == "admin":
        mongo.db.categories.remove({"_id": ObjectId(category_id)})
        flash("Category Deleted Successfully")
        return redirect(url_for("get_categories"))

    else:
        flash("You have to be an Admin to access this page")
        return render_template("403.html")


# Errors Handlers
# https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
@app.errorhandler(403)
# To handle Forbidden access control
def forbidden(e):
    return render_template('403.html'), 403


@app.errorhandler(404)
# To handle not found page
def page_not_found(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
# To handle Internal Server Error
def internal_server_error(e):
    return render_template('500.html'), 500


# Set how & where to run the app
if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

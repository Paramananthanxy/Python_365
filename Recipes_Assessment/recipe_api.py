from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from recipe_service import get_recipes, search_recipes

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/recipes")
def recipes():

    page = int(request.args.get("page", 1))
    limit = int(request.args.get("limit", 10))

    result = get_recipes(page, limit)

    return jsonify(result)


@app.route("/api/recipes/search")
def search():

    title = request.args.get("title")
    cuisine = request.args.get("cuisine")
    rating = request.args.get("rating")
    total_time = request.args.get("total_time")

    result = search_recipes(title, cuisine, rating, total_time)

    return jsonify({"data": result})


if __name__ == "__main__":
    app.run(debug=True)
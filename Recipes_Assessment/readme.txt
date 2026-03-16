Recipe Data Collection and API Development
Project Overview

This project parses recipe data from a JSON file, stores it in a SQLite database, and exposes the data through RESTful APIs using Flask.

The API supports:

Pagination

Sorting by rating

Searching recipes based on different filters

A simple frontend UI is also included to display the recipe data in a table.

Tech Stack

Python

Flask

SQLite

HTML / JavaScript

Flask-CORS

Project Structure
Recipes_Assessment
│
├── recipes_db.py        # Database connection and table creation
├── load_recipes.py      # JSON parsing and loading data into DB
├── recipe_service.py    # Service layer (DB queries)
├── recipe_api.py        # Flask API endpoints
│
├── recipes.db           # SQLite database
├── US_recipes_null.Pdf.json
│
└── templates
      └── index.html     # Simple frontend UI
Database Schema

Table: recipes

Column	Type
id	INTEGER (Primary Key)
cuisine	TEXT
title	TEXT
rating	REAL
prep_time	INTEGER
cook_time	INTEGER
total_time	INTEGER
description	TEXT
nutrients	TEXT (JSON)
serves	TEXT
Setup Instructions
1. Install dependencies
pip install flask flask-cors
2. Create the database

Run:

python recipes_db.py

This will create the recipes table.

3. Load JSON data into database

Run:

python load_recipes.py

This parses the JSON file and inserts the recipe records into the database.

4. Start the API server
python recipe_api.py

Server will run on:

http://127.0.0.1:5000
API Endpoints
1. Get All Recipes (Paginated)

Endpoint

GET /api/recipes

Example Request

http://127.0.0.1:5000/api/recipes?page=1&limit=10

Example Response

{
 "page": 1,
 "limit": 10,
 "total": 50,
 "data": [
   {
     "id": 1,
     "title": "Sweet Potato Pie",
     "cuisine": "Southern Recipes",
     "rating": 4.8,
     "prep_time": 15,
     "cook_time": 100,
     "total_time": 115,
     "description": "...",
     "serves": "8 servings"
   }
 ]
}
2. Search Recipes

Endpoint

GET /api/recipes/search

Query Parameters

title

cuisine

rating

total_time

Example Request

http://127.0.0.1:5000/api/recipes/search?title=pie

Example Request

http://127.0.0.1:5000/api/recipes/search?cuisine=Southern&rating=4
Frontend UI

The frontend displays recipes in a table with:

Title

Cuisine

Rating (Star format)

Total Time

Serves

Clicking a row shows recipe details.

To view the UI, open:

index.html
Handling NaN Values

During JSON parsing:

"NaN" values are converted to NULL

This ensures numeric fields remain valid in the database.
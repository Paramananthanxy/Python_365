import json
from recipes_db import get_connection

conn = get_connection()
cursor = conn.cursor()

with open("C:/Python_Beg_to_Adv/Recipes_Assessment/US_recipes_null.Pdf.json") as f:
    data = json.load(f)

recipes = data.values() if isinstance(data, dict) else data

for r in recipes:

    rating = None if r.get("rating") in ["NaN", None] else r.get("rating")
    prep_time = None if r.get("prep_time") in ["NaN", None] else r.get("prep_time")
    cook_time = None if r.get("cook_time") in ["NaN", None] else r.get("cook_time")
    total_time = None if r.get("total_time") in ["NaN", None] else r.get("total_time")

    cursor.execute("""
    INSERT INTO recipes(
        cuisine,title,rating,prep_time,
        cook_time,total_time,description,
        nutrients,serves
    )
    VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        r.get("cuisine"),
        r.get("title"),
        rating,
        prep_time,
        cook_time,
        total_time,
        r.get("description"),
        json.dumps(r.get("nutrients")),
        r.get("serves")
    ))

conn.commit()
conn.close()

print("Recipes loaded successfully")
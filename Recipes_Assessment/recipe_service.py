from recipes_db import get_connection


# Get recipes with pagination
def get_recipes(page=1, limit=10):

    conn = get_connection()
    cursor = conn.cursor()

    offset = (page - 1) * limit

    # total number of records
    cursor.execute("SELECT COUNT(*) FROM recipes")
    total = cursor.fetchone()[0]

    # get paginated recipes sorted by rating
    cursor.execute("""
        SELECT *
        FROM recipes
        ORDER BY rating DESC
        LIMIT ? OFFSET ?
    """, (limit, offset))

    rows = cursor.fetchall()
    conn.close()

    data = []
    for r in rows:
        data.append(dict(r))

    return {
        "page": page,
        "limit": limit,
        "total": total,
        "data": data
    }


# Search recipes
def search_recipes(title=None, cuisine=None, rating=None, total_time=None):

    conn = get_connection()
    cursor = conn.cursor()

    query = "SELECT * FROM recipes WHERE 1=1"
    params = []

    if title:
        query += " AND title LIKE ?"
        params.append("%" + title + "%")

    if cuisine:
        query += " AND cuisine = ?"
        params.append(cuisine)

    if rating:
        query += " AND rating >= ?"
        params.append(rating)

    if total_time:
        query += " AND total_time <= ?"
        params.append(total_time)

    cursor.execute(query, params)

    rows = cursor.fetchall()
    conn.close()

    results = []
    for r in rows:
        results.append(dict(r))

    return results
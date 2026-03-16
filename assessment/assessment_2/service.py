from database import get_connect

def get_weather(date):
    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""SELECT temp,humidity,pressure 
                   FROM weath
                    WHERE  date LIKE ?""",(date+'%',))
    rows = cursor.fetchall()
    conn.close()

    result = []
    for r in rows:
        result.append({
            'temp':r[0],
            'humidity':r[1],
            'pressure':r[2]
        })
    return result
def get_year(year):
    conn = get_connect()
    cursor = conn.cursor()

    cursor.execute("""SELECT substr(date,5,2) AS month,
                   MAX(temp),
                   MIN(temp),
                   AVG(temp)
                   FROM weath
                   WHERE substr(date,1,4) = ?
                   GROUP BY month

                   """,(year,))
    rows = cursor.fetchall()
    conn.close()
    result = []
    for r in rows:
        result.append({
            "month":r[0],
            "max_temp":r[1],
            "min_temp":r[2],
            "avg_temp":r[3]
        })
    return result
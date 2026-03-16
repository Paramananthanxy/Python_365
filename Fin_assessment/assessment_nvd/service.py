from nvd_database import sql_connect
def cvlist():
    conn = sql_connect()
    cursor = conn.cursor()

    cursor.execute("SELECT cve_id,published,lastmodified FROM cve LIMIT 10")
    data = cursor.fetchall()
    # print(data)

    result = []
    for x in data:
        result.append({
            "id": x[0],
            "published": x[1],
            "lastmodified": x[2]
        })
        # print(result)
    return result


def cve_id(id):
    conn = sql_connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT cve_id,descriptions,basescore FROM cve WHERE cve_id = ?""",(id,))
    data = cursor.fetchall()
    conn.close()
    result = []
    for x in data:
        result.append({
            'id':x[0],
            'descripitons':x[1],
            'basescore':x[2]
        })
    return result
def spe_year(year):
    conn = sql_connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT cve_id,descriptions,published,lastmodified FROM cve 
                   WHERE published like ?""",(year + '%',))
    data = cursor.fetchall()
    conn.close()
    result = []
    for x in data:
        result.append({
            'id':x[0],
            'descripitons':x[1],
            'published':x[2],
            'lastmodified':x[3]

        })
    return result
def cve_score(id):
    conn = sql_connect()
    cursor = conn.cursor()
    cursor.execute("""SELECT cve_id,descriptions,basescore FROM cve WHERE cve_id = ?""",(id,))
    data = cursor.fetchall()
    conn.close()
    result = []
    for x in data:
            result.append({
                'id':x[0],
                'descripitons':x[1],
                'basescore':x[2]
            })
    return result




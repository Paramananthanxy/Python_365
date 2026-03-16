import sqlite3 
import flask
from nvd_db import connect
from datetime import datetime,timedelta

def cve_id(id):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute("""SELECT id,descriptions FROM cve WHERE id = ? """,(id,))
    data = cursor.fetchall()
    rows = []
    conn.close()
    for r in data:
        rows.append({
            'id':r[0],
            'descriptions':r[1]
        })
    return rows

def nvd_lastmodifi(days):
    conn = connect()
    cursor = conn.cursor()
    datelimit = datetime.utcnow() - timedelta(days=int(days))

    cursor.execute("""SELECT id,descriptions,published,lastmodified FROM cve 
                   WHERE lastmodified >= ?""",(datelimit.isoformat(),))
    data = cursor.fetchall()
    rows = []
    conn.close()
    for r in data:
        rows.append({
            "id":r[0],
            "descriptions":r[1],
            "published":r[2],
            "lastmodified":r[3]
        })
    return rows


import csv
from database import get_connect,create_table

def load_data(filepath):
    create_table()
    conn = get_connect()
    cursor = conn.cursor()

    with open(filepath,'r') as file:
        csv_file = csv.DictReader(file)
        for data in csv_file:
            if data['_pressurem'] in ['-9999',''] or data['_tempm'] =='':
                continue
            cursor.execute("INSERT INTO weath VALUES (?,?,?,?)",(
                data['datetime_utc'],
                data['_tempm'],
                data['_hum'],
                data['_pressurem']
            ) )
    conn.commit()
    cursor.close()

if __name__ == "__main__":
    load_data("C:/Python_Beg_to_Adv/assessment/assessment_2/testset.csv")

import matplotlib.pyplot as plt
import csv



# Parsing the csv file Headers...
with open("C:\Python_Beg_to_Adv\Assessments\customers-100.csv") as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)
    
    date,temp  =[],[]
    for index,column in enumerate(header_row):
        print(index, column)
    # for row in reader:
    #     first_name.append(row[2])
    #     print(first_name)
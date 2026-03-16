import xmltodict
import json

data = input("Enter the path of the file: ")
with open(data ,encoding='utf-8') as xml_file:
    xml_dict = xmltodict.parse(xml_file.read())
    json_file = json.dumps(xml_dict, indent = 4)
with open("compnay.json",'w') as json_data:
    json_data.write(json_file)
import xmltodict
import json

with open("C:/Python_Beg_to_Adv/assessment/bookstore.xml") as xml_file:
    xml = xmltodict.parse(xml_file.read())
    # print(xml)
    print(json.dumps(xml,indent=4))

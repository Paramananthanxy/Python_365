import xmltodict
import json

with open("C:/Python_Beg_to_Adv/Fin_assessment/assessment_nvd/compnay.json",'r') as file:
    print(file)
    re = json.load(file)
    # print(re)
    # data = {"com":{"dec":re}}
    # xml = xmltodict.unparse(data,pretty=True)
    # print(xml)
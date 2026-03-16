import xmltodict

with open("C:/Python_Beg_to_Adv/assessment/exercise/event.xml",encoding='utf-8') as xml_file:
    xml_dict = xmltodict.parse(xml_file.read())
    events = xml_dict['events']['event']
for event in events:
        # print(event)
        if event['severity']=='High':
            print(event['id'])
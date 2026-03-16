import xmltodict 

with open("C:/Python_Beg_to_Adv/assessment/exercise/logs.xml",encoding='utf-8') as xml_file:
    xml_dict = xmltodict.parse(xml_file.read())
    # print(xml_dict)
    log1 = xml_dict['logs']['log']
    for logg in log1:
        if logg['status'] == 'failed':
            print(f"Failed action by user: {logg['user'].title()}")
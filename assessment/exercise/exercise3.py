import xmltodict

with open("C:/Python_Beg_to_Adv/assessment/exercise/event.xml",encoding='utf-8') as xml_file:
    xml_dict = xmltodict.parse(xml_file.read())
    events = xml_dict['events']['event']
    st1,st2,st3,st4 = [],[],[],[]
    for event in events:
        events1 = event
        st1.append(events1)
  
    for sev in events:
        if sev['severity'] == 'High':
            st2.append(sev)
# print(len(st2))
        elif sev['severity'] == 'Medium':
            st3.append(sev)
        elif sev['severity'] == 'Low':
            st4.append(sev)

print(f"The Total events:{len(st1)}")
print(f"The High Severity:{len(st2)}")
print(f"The Medium Severity:{len(st3)}")
print(f"The Low Severity:{len(st4)}")
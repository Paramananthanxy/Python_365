import xml.etree.ElementTree as et
tree = et.parse('bookstore.xml')
root = tree.getroot()
print(root[0][0].tag)
print(root[0][0].text)

for item in root[0]:
    print(item)
    
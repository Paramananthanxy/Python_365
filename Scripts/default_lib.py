from collections import OrderedDict

fav = OrderedDict()
fav['jen'] = 'python'
fav['sarah'] = 'c'

for name,lang in fav.items():
    print(f"{name.title()} favorite language is {lang.title()}")
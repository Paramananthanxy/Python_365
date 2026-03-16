import json
import pygal
from pygal_maps_world.maps import COUNTRIES
from pygal_maps_world.maps import World
from pygal.style import RotateStyle

filename = "C:/Users/nates/Downloads/population_data.json"
populations = {}
def country_codes(country_name):
    for code,name in COUNTRIES.items():
        if name == country_name:
            return code
    return None

with open(filename) as f:
    data = json.load(f)



    for pop_dic in data:
        if pop_dic['Year']=='2010':
            country_name = pop_dic['Country Name']
            country_code = pop_dic['Country Code']
            population = int(float(pop_dic['Value']))
            cd = country_codes(country_name)
            if cd:
                populations[cd]=population
cc_1,cc_2,cc_3 = {},{},{}
for cc,values in populations.items():
        if values < 100000000:
             cc_1[cc] = values
        elif values <10000000000:
             cc_2[cc] = values
        else:
             cc_3[cc] = values

wm = World()
wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = "Population of the World.."
# wm.add('world',populations)
wm.add("middle population",cc_1)
wm.add("Higher population",cc_2)
wm.add("lower population",cc_3)
wm.render_to_file("world.svg")

import json
import pygal
from get_code import get_country_codes

filename = 'gdp_json.json'

with open(filename) as file_object:
    gdp_data = json.load(file_object)

gdp_world = {}

for gdp_dict in gdp_data:
    if gdp_dict['Year'] == 2015:
        country_name = gdp_dict['Country Name']
        gdp = int(float(gdp_dict['Value']))
        code = get_country_codes(country_name)
        if code:
            gdp_world[code] = gdp

print(gdp_world)

worldmap = pygal.maps.world.World()
worldmap.add('global gdp in 2015', gdp_world)
worldmap.render_to_file('gdp.svg')

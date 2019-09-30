import json
import pygal
from get_code import get_country_codes
from pygal.style import LightenStyle

filename = 'population_data.json'

with open(filename) as file_object:
    pop_data = json.load(file_object)

popgroup_1, popgroup_2, popgroup_3 = {}, {}, {}

for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        population = int(float(pop_dict['Value']))
        code = get_country_codes(country_name)
        if code:
            if population < 10000000:
                popgroup_1[code] = population
            elif 10000000 <= population < 1000000000:
                popgroup_2[code] = population
            else:
                popgroup_3[code] = population
        else:
            print('ERROR - ' + country_name)

worldmap_style = LightenStyle('#336676', step=5)
worldmap = pygal.maps.world.World(style=worldmap_style)
worldmap.add('<10m', popgroup_1)
worldmap.add('10m-1bn', popgroup_2)
worldmap.add('1bn+', popgroup_3)
worldmap.render_to_file('worldmap.svg')

"""
worldmap.add('North America', ['ca', 'mx', 'us'])
worldmap.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
worldmap.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])
worldmap.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
worldmap.render_to_file('testing.svg')
"""

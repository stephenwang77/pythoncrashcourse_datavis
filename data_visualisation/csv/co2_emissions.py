import csv
import pygal
from get_code import get_country_codes

filename = 'co2.csv'
co2_emission = {}

with open(filename) as file_object:
    reader = csv.reader(file_object)
    header_row = next(reader)

    for row in reader:
        try:
            country_name = row[0]
            code = get_country_codes(country_name)
            if code:
                co2_emission[code] = float(row[52])
        except ValueError:
            pass

worldmap = pygal.maps.world.World()
worldmap.add('co2 emissions', co2_emission)
worldmap.render_to_file('co2.svg')


"""
for index, header in enumerate(header_row):
    print(index, header)
"""

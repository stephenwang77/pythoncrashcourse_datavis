from pygal.maps.world import COUNTRIES

def get_country_codes(country_name):
    for code, name in COUNTRIES.items():
        if country_name == COUNTRIES[code]:
            return code
        elif country_name in COUNTRIES[code]:
            return code
    return None

"""
print('Yemen' in 'Yemen, Rep.')

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
"""

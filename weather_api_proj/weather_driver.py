import requests
from pprint import pprint
import json

baseurl = 'http://dataservice.accuweather.com'
parameters = {
    'apikey':'acV0n6pLYWc4QXhcNjl7GV5RbpuG5olk',
    'language':'en-us',
    'details':'false'
}

def get_cities():
    # City list
    r = requests.get(baseurl + '/locations/v1/topcities/50', params=parameters)
    r.raise_for_status()

    print("url {}".format(r.url))
    pprint(r.json()[-1])

    citydict = {}
    # only loop through last object due to API 50call/day limit
    for city in r.json()[-1:]:
        citydict.update({city.get('EnglishName'):[city.get('Key')]})
    print("List of Cities:")
    print('\n'.join(citydict.keys()))
    
    return citydict

def get_temps(citydict):
    for cityname, citykey in citydict.items():
        r2 = requests.get(baseurl + '/currentconditions/v1/' + citykey[0], params=parameters)
        # import pdb; pdb.set_trace()
        pprint(r2.json())
        citykey.append(r2.json()[0].get('Temperature').get('Imperial').get('Value'))
    pprint(citydict)    

if __name__ == "__main__":
    # citydict = get_cities()
    citydict = {u'Reykjavik': [u'190390']}
    get_temps(citydict)

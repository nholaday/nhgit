import requests
import json

url = 'http://dataservice.accuweather.com/locations/v1/'
params = {
    'apikey': 'acV0n6pLYWc4QXhcNjl7GV5RbpuG5olk',
    'q': 'Oakland',
}

def main():
    r = requests.get(url + "cities/search", params=params)
    # import pdb; pdb.set_trace()
    print(json.dumps(r.json(), indent=4))
    
if __name__ == '__main__':
    main()
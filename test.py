import requests
import json

def get_package_monthy_downloads(package_name):
    url = 'https://pypistats.org/api/packages/{}/recent'.format(package_name)
    response = requests.get(url)
    package_dict = response.json()
    
    print(package_dict['data']['last_month'])

get_package_monthy_downloads('pandas')
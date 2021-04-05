import requests
import re
import json
import sys
import argparse


def get_packagenames(package_name, substring = True):
    """
    Search for package with full or partial package name
    """
    url = 'https://pypi.org/simple/'
    matches = []
    response = requests.get(url, stream=True)
    for line in response.iter_lines():
        p_name = (str(line, 'UTF-8'))
        if substring == True:
            if p_name.find(package_name) > 0:
                p_name_arr = p_name.split('>')
                matches.append(p_name_arr[1][:-5])
        else:
            p_match = re.search(r"\b"+package_name+r"\b", p_name)
            if p_match is not None:
                p_name_arr = p_name.split('>')
                matches.append(p_name_arr[1][:-5])
                
    return matches

def package_description(package_name):
    url = 'https://pypi.org/pypi/{}/json'.format(package_name) 
    response = requests.get(url)
    package_dict = json.loads(response.text)
    
    return(package_dict['info']['description'])
    

if __name__ == '__main__':






    
    
    
   

   
#!/usr/bin/env python3

import requests
import re
import json
import sys


def get_package_monthy_downloads(package_name):
    url = 'https://pypistats.org/api/packages/{}/recent'.format(package_name)
    response = requests.get(url)
    package_dict = response.json()
    
    print (package_dict['data']['last_month'])


def get_packagenames(package_name, substring_match = True):
    """
    Search for package with full or partial package name
    """
    url = 'https://pypi.org/simple/'
    matches = []

    response = requests.get(url, stream=True)
    for line in response.iter_lines():
        p_name = (str(line, 'UTF-8'))
        
        if substring_match == True:
            if p_name.find(package_name) > 0:
                p_name_arr = p_name.split(r'/">')
                matches.append(p_name_arr[1][:-4])

        
        if substring_match == False:
            p_match = re.findall('\\b' + package_name + '\\b', p_name)
            if len(p_match) > 0:
                p_name_arr = p_name.split(r'/">')
                matches.append(p_name_arr[1][:-4])                
                
    for match in matches:
       print(match)


def get_package_description(package_name):
    url = 'https://pypi.org/pypi/{}/json'.format(package_name) 
    response = requests.get(url)
    package_dict = response.json()
    print(package_dict['info']['description'])


def pypi_search():
    help_message = ('Please enter ./pip_search -p (-e) package_name for package list, -d for package_description'
                    'or -n for number of monthly package downloads')
    try:
        
        if sys.argv[1] == '-p' and len(sys.argv) == 3:
           get_packagenames(sys.argv[2])
        
        elif sys.argv[1] == '-p' and sys.argv[2] == '-e' and len(sys.argv) == 4: 
           get_packagenames(sys.argv[3], substring_match=False)
    
        elif sys.argv[1] == '-d' and len(sys.argv) == 3:
            get_package_description(sys.argv[2])

        elif sys.argv[1] == '-n' and len(sys.argv) == 3:
            get_package_monthy_downloads(sys.argv[2])
        
        else:
            print(help_message)

    except:
        print(help_message)
        
    
        
if __name__ == '__main__':
    pypi_search()





    
    
    
   

   

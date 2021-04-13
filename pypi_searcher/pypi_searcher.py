#!/usr/bin/env python3

import requests
import re
import json
import sys

# decorator for modifying function behaviors based on weather this file is run
# directly as script (results are printed) or as module (results are returned).
def print_or_return(func):  
    def wrapper(package_name):
        values = func(package_name)
        if __name__ == '__main__':
            if isinstance(values, list):
                for value in values:
                    print(value)
            else:
                print(values)
        else:
            return values
    return wrapper


@print_or_return
def get_package_monthy_downloads(package_name):
    url = 'https://pypistats.org/api/packages/{}/recent'.format(package_name)
    response = requests.get(url)
    package_dict = response.json()

    return package_dict['data']['last_month']


@print_or_return
def get_packagenames(package_name):
    """
    Search for package with full or partial package name
    """
    url = 'https://pypi.org/simple/'
    matches = []

    response = requests.get(url, stream=True)
    for line in response.iter_lines():
        p_name = (str(line, 'UTF-8'))
    
        if p_name.find(package_name) > 0:
            p_name_arr = p_name.split(r'/">')
            matches.append(p_name_arr[1][:-4])

    return matches


@print_or_return
def get_package_description(package_name):
    url = 'https://pypi.org/pypi/{}/json'.format(package_name)
    response = requests.get(url)
    package_dict = response.json()

    return package_dict['info']['description']


def pypi_search(*argv):
    help_message = ('Please enter ./pip_search -p package_name for package list, -d for package_description'
                    'or -n for number of monthly package downloads')

    if __name__ == '__main__':
        argv = sys.argv

    try:

        if argv[1] == '-p' and len(argv) == 3:
           get_packagenames(argv[2])

        elif argv[1] == '-p' and len(argv) == 3:
           get_packagenames(argv[3])

        elif argv[1] == '-d' and len(argv) == 3:
            get_package_description(argv[2])

        elif argv[1] == '-n' and len(argv) == 3:
            get_package_monthy_downloads(argv[2])

        else:
            print(help_message)

    except:
        print(help_message)



if __name__ == '__main__':
    pypi_search()
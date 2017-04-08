import json
import os
from pprint import pprint

def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='windows-1251') as data_file:
        return json.load(data_file)


def pretty_print_json(data):
    return pprint(data)


if __name__ == '__main__':
    data = load_data('data-2897-2016-11-23.json')
    pretty_print_json(data)

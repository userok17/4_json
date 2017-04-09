import json
import os
from pprint import pprint
from optparse import OptionParser


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='windows-1251') as data_file:
        return json.load(data_file)


def pretty_print_json(json_data):
    return pprint(json_data)

def parser_command():
    parser = OptionParser()
    parser.add_option('-f', '--filepath', help='Укажите файл до json файла',dest='filepath')
    opts, args = parser.parse_args()
    if opts.filepath:
        pretty_print_json(load_data(opts.filepath))
        


if __name__ == '__main__':
    parser_command()

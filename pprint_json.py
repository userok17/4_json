import json
import os
from argparse import ArgumentParser


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, encoding='windows-1251') as data_file:
        return json.load(data_file)


def pretty_print_json(json_data):
    dumps =  json.dumps(json_data, sort_keys=True, indent=4)
    print(dumps)

def main():
    parser = ArgumentParser(description='Скрипт выводит  json содержимое в консоль в удобном формате')
    parser.add_argument('-f', '--filepath', help='Укажите путь до json файла', required=True, dest='filepath')
    args = parser.parse_args()
    json_data = load_data(args.filepath)
    if json_data:
        pretty_print_json(json_data)
    else:
        print('Неверно указан путь до json файла')
        


if __name__ == '__main__':
    main()

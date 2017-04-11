# Prettify JSON

Скрипт Prettify JSON на вход принимает путь до файла, в котором хранится json и выводит его содержимое в консоль в удобном формате.

# Quickstart

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:


```#!bash
usage: pprint_json.py [-h] -f FILEPATH

Скрипт выводит json содержимое в консоль в удобном формате

optional arguments:
  -h, --help            show this help message and exit
  -f FILEPATH, --filepath FILEPATH
                        Укажите путь до json файла


$ python pprint_json.py -f <path to file>
# TODO add output example
[
    {
        "Cells": {
            "Address": "улица Академика Павлова, дом 10", 
            "AdmArea": "Западный административный округ", 
            "ClarificationOfWorkingHours": null, 
            "District": "район Кунцево", 
            "IsNetObject": "да", 
            "Name": "Ароматный Мир", 
            "OperatingCompany": "Ароматный Мир", 
            "PublicPhone": [
                {
                    "PublicPhone": "(495) 777-51-95"
                }
            ], 
            "TypeService": "реализация продовольственных товаров", 
            "WorkingHours": [
                {
                    "DayOfWeek": "понедельник", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "вторник", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "среда", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "четверг", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "пятница", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "суббота", 
                    "Hours": "09:30-22:30"
                }, 
                {
                    "DayOfWeek": "воскресенье", 
                    "Hours": "09:30-22:30"
                }
            ], 
            "geoData": {
                "coordinates": [
                    37.39703804817934, 
                    55.740999719549094
                ], 
                "type": "Point"
            }, 
            "global_id": 14371450
        }, 
        "Id": "79742784-9ef3-4543-bc98-a219a8903c18", 
        "Number": 1
    }, 
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)

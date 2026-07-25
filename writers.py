import csv
import json
import yaml


fieldnames = [
    "id",
    "name",
    "category",
    "status",
    "priority",
    "duration",
    "vehicle",
    "environment",
    "temperature",
    "executed_by",
    "timestamp",
]


def write_json(data, output_file):
    with open (output_file, 'w') as file:
        json.dump(data, file, indent=4)



def write_yaml(data, output_file):
    with open (output_file, 'w') as file:
        yaml.dump(data, file)


def write_csv(data, output_file):
    with open (output_file, 'w') as file:
        writer = csv.DictWriter(file, fieldnames)
        writer.writeheader()
        for test in data["tests"]:
            writer.writerow(test)

import pytest
from pathlib import Path
import writers
import json
import yaml
import csv




#sample data
def simple_data():
    return {
        "project": "Autonomous Vehicle Validation",
        "version": "1.0",
        "generated_at": "2026-07-23T14:30:00Z",
        "tests": [
            {
              "id": 1001,
              "name": "Emergency Braking",
              "category": "Safety",
              "status": "Passed",
              "priority": "Critical",
              "duration": 2.8,
              "vehicle": "Car-A",
              "environment": "Simulation",
              "temperature": 24,
              "executed_by": "CI",
              "timestamp": "2026-07-22T09:15:00Z"
            }
        ]
    }




#test (write_json) function
def test_write_json_creates_file():
    file = Path("output") / "test_json.json"
    minimum_data = simple_data()
    writers.write_json(minimum_data, file)
    assert file.exists()


def test_write_json_writes_correct_content():
    file = Path("output") / "test_json.json"
    minimum_data = simple_data()
    writers.write_json(minimum_data, file)
    with open(file, 'r') as f:
        retrieved_data = json.load(f)
    assert retrieved_data == minimum_data


def test_write_json_invalid_output_directory():
    file = Path("outputt") / "test_json.json"
    minimum_data = simple_data()
    with pytest.raises(FileNotFoundError):
        writers.write_json(minimum_data, file)




#test (write_yaml) function
def test_write_yaml_creates_file():
    file = Path("output") / "test_yaml.yaml"
    minimum_data = simple_data()
    writers.write_yaml(minimum_data, file)
    assert file.exists()


def test_write_yaml_writes_correct_content():
    file = Path("output") / "test_yaml.yaml"
    minimum_data = simple_data()
    writers.write_yaml(minimum_data, file)
    with open(file, 'r') as f:
        retrieved_data = yaml.safe_load(f)
    assert retrieved_data == minimum_data


def test_write_yaml_invalid_output_directory():
    file = Path("outputt") / "test_yaml.yaml"
    minimum_data = simple_data()
    with pytest.raises(FileNotFoundError):
        writers.write_yaml(minimum_data, file)


#test (write_csv) function
def test_write_csv_creates_file():
    file = Path("output") / "test_csv.csv"
    minimum_data = simple_data()
    writers.write_csv(minimum_data, file)
    assert file.exists()


def test_write_csv_writes_correct_content():
    file = Path("output") / "test_csv.csv"
    minimum_data = simple_data()
    writers.write_csv(minimum_data, file)
    with open(file, 'r') as f:
        retrieved_data = list(csv.DictReader(f))

    for item in retrieved_data[0]:
        assert retrieved_data[0][item] == str(minimum_data["tests"][0][item])


def test_write_csv_invalid_output_directory():
    file = Path("outputt") / "test_csv.csv"
    minimum_data = simple_data()
    with pytest.raises(FileNotFoundError):
        writers.write_csv(minimum_data, file)

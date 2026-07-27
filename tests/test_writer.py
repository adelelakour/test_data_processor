import pytest
from pathlib import Path
import writers
import json
import yaml
import csv



@pytest.fixture
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


@pytest.fixture
def json_file_path(tmp_path):
    return tmp_path / "test_json.json"

@pytest.fixture
def yaml_file_path(tmp_path):
    return tmp_path / "test_yaml.yaml"

@pytest.fixture
def csv_file_path(tmp_path):
    return tmp_path / "test_csv.csv"

@pytest.fixture
def invalid_path():
    return Path("outputt") / "x.csv"



#test (write_json) function
def test_write_json_creates_file(simple_data, json_file_path):
    writers.write_json(simple_data, json_file_path)
    assert json_file_path.exists()


def test_write_json_writes_correct_content(simple_data, json_file_path):
    writers.write_json(simple_data, json_file_path)
    with open(json_file_path, 'r') as f:
        retrieved_data = json.load(f)
    assert retrieved_data == simple_data


def test_write_json_invalid_output_directory(simple_data, invalid_path):
    with pytest.raises(NotADirectoryError):
        writers.write_json(simple_data, invalid_path)




#test (write_yaml) function
def test_write_yaml_creates_file(simple_data, yaml_file_path):
    writers.write_yaml(simple_data, yaml_file_path)
    assert yaml_file_path.exists()


def test_write_yaml_writes_correct_content(simple_data, yaml_file_path):
    writers.write_yaml(simple_data, yaml_file_path)
    with open(yaml_file_path, 'r') as f:
        retrieved_data = yaml.safe_load(f)
    assert retrieved_data == simple_data


def test_write_yaml_invalid_output_directory(simple_data, invalid_path):
    with pytest.raises(NotADirectoryError):
        writers.write_yaml(simple_data, invalid_path)


#test (write_csv) function
def test_write_csv_creates_file(simple_data, csv_file_path):
    writers.write_csv(simple_data, csv_file_path)
    assert csv_file_path.exists()


def test_write_csv_writes_correct_content(simple_data, csv_file_path):
    writers.write_csv(simple_data, csv_file_path)
    with open(csv_file_path, 'r') as f:
        retrieved_data = list(csv.DictReader(f))

    for item in retrieved_data[0]:
        assert retrieved_data[0][item] == str(simple_data["tests"][0][item])


def test_write_csv_invalid_output_directory(simple_data, invalid_path):
    with pytest.raises(NotADirectoryError):
        writers.write_csv(simple_data, invalid_path)


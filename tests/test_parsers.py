from json import JSONDecodeError
from yaml import YAMLError
import parsers
import pytest
from pathlib import Path


#test read_json function
def test_read_json_valid_file() -> None:

    data = parsers.read_json(Path("tests/data") / "data.json")

    assert  data["project"] == "Autonomous Vehicle Validation"
    assert  data["version"] == "1.0"
    assert  data["generated_at"] == "2026-07-23T14:30:00Z"
    assert  len(data["tests"]) == 20

    first_test = data["tests"][0]

    assert  first_test["name"] == "Emergency Braking"
    assert  first_test["status"] == "Passed"
    assert  first_test["duration"] == 2.8
    assert  first_test["temperature"] == 24


def test_read_json_empty_file() -> None:
    with pytest.raises(JSONDecodeError):
        parsers.read_json(Path("tests/data") / "data_empty.json")


def test_read_json_malformed_file() -> None:
    with pytest.raises(JSONDecodeError):
        parsers.read_json(Path("tests/data") / "data_invalid.json")


def test_read_json_not_existing_file() -> None:
    with pytest.raises(FileNotFoundError):
        parsers.read_json(Path("tests/data") / "x.json")



#test read_yaml function

def test_read_yaml_valid_file() -> None:

    data = parsers.read_yaml(Path("tests/data") / "data.yaml")

    assert  data["project"] == "Autonomous Vehicle Validation"
    assert  data["version"] == "1.0"
    assert  data["generated_at"] == "2026-07-23T14:30:00Z"
    assert  len(data["tests"]) == 20

    first_test = data["tests"][0]

    assert  first_test["name"] == "Emergency Braking"
    assert  first_test["status"] == "Passed"
    assert  first_test["duration"] == 2.8
    assert  first_test["temperature"] == 24


def test_read_yaml_empty_file():
    assert parsers.read_yaml(Path("tests/data") / "data_empty.yaml") is None


def test_read_yaml_malformed_file() -> None:
    with pytest.raises(YAMLError):
        parsers.read_yaml(Path("tests/data") / "data_invalid.yaml")


def test_read_yaml_not_existing_file() -> None:
    with pytest.raises(FileNotFoundError):
        parsers.read_yaml(Path("tests/data") / "x.yaml")



#test read_csv function
def test_read_csv_valid_file() -> None:

    data = parsers.read_csv(Path("tests/data") / "data.csv")

    assert  len(data["tests"]) == 20

    first_test = data["tests"][0]

    assert  first_test["name"] == "Emergency Braking"
    assert  first_test["status"] == "Passed"
    assert  first_test["duration"] == 2.8
    assert  first_test["temperature"] == 24


def test_read_csv_empty_file() -> None:
    data = parsers.read_csv(Path("tests/data") / "data_empty.csv")
    assert len(data["tests"]) == 0

def test_read_csv_not_existing_file() -> None:
    with pytest.raises(FileNotFoundError):
        parsers.read_csv(Path("tests/data") / "x.csv")







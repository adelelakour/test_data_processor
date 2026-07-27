import pytest
import validator

#helper function
def sample_data() ->dict:
    return {
            "tests":
                [
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


#Test (validate_schema) function  -- 4 Tests
def test_validate_schema_valid():
    data = sample_data()
    validator.validate_schema(data)


def test_validate_schema_missing_key() -> None:
    data = sample_data()
    del data["tests"][0]["id"]

    with pytest.raises(KeyError):
        validator.validate_schema(data)


def test_validate_schema_missing_tests() -> None:
    data = sample_data()
    del data["tests"]

    with pytest.raises(KeyError):
        validator.validate_schema(data)


def test_validate_schema_empty_tests() ->None:
    data = sample_data()
    data["tests"] = []
    with pytest.raises((ValueError)):
        validator.validate_schema(data)



#Test (validate_data_types) function
def test_validate_data_types_valid() -> None:
    data = sample_data()
    validator.validate_data_types(data)

def test_validate_data_types_invalid_id_type() -> None:
    data = sample_data()
    data["tests"][0]["id"] = "1001"
    with pytest.raises(TypeError):
        validator.validate_data_types(data)

def test_validate_data_types_invalid_id_range() -> None:
    data = sample_data()
    data["tests"][0]["id"] = -100
    with pytest.raises(ValueError):
        validator.validate_data_types(data)

def test_validate_data_types_invalid_name_type() -> None:
    data = sample_data()
    data["tests"][0]["name"] = 100
    with pytest.raises(TypeError):
        validator.validate_data_types(data)

def test_validate_data_types_invalid_duration_type() -> None:
    data = sample_data()
    data["tests"][0]["duration"] = "2.8"
    with pytest.raises(TypeError):
        validator.validate_data_types(data)

def test_validate_data_types_invalid_duration_range() -> None:
    data = sample_data()
    data["tests"][0]["duration"] = -2.8
    with pytest.raises(ValueError):
        validator.validate_data_types(data)

def test_validate_data_types_invalid_temperature_type() -> None:
    data = sample_data()
    data["tests"][0]["temperature"] = "24"
    with pytest.raises(TypeError):
        validator.validate_data_types(data)


#Test (validate_status_field) function
def test_validate_status_field_valid() -> None:
    data = sample_data()
    validator.validate_status_field(data)

def test_validate_status_field_invalid() -> None:
    data = sample_data()
    data["tests"][0]["status"] = "True"
    with pytest.raises(ValueError):
        validator.validate_status_field(data)





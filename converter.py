#!/usr/bin/env python3
import parsers
import writers
import validator
import utils

import sys




def main() -> None:

    INPUT_FILE, OUTPUT_FILE = utils.get_files_from_user()

    if INPUT_FILE.suffix == ".json":
        retrieved_data = parsers.read_json(INPUT_FILE)
    elif INPUT_FILE.suffix == ".csv":
        retrieved_data = parsers.read_csv(INPUT_FILE)
    elif INPUT_FILE.suffix == ".yaml":
        retrieved_data = parsers.read_yaml(INPUT_FILE)

    try:
        validator.validate_schema(retrieved_data)
        validator.validate_data_types(retrieved_data)
        validator.validate_status_field(retrieved_data)
    except (KeyError, ValueError, TypeError) as e:
        print(f"Error message is {e}")


    if OUTPUT_FILE.suffix == ".json":
        writers.write_json(retrieved_data, OUTPUT_FILE)
    elif OUTPUT_FILE.suffix == ".yaml":
        writers.write_yaml(retrieved_data, OUTPUT_FILE)
    elif OUTPUT_FILE.suffix == ".csv":
        writers.write_csv(retrieved_data, OUTPUT_FILE)


if __name__ == "__main__":
    main()
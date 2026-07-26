# TestDataProcessor

`TestDataProcessor` is a small Python CLI for reading autonomous vehicle test data from `JSON`, `YAML`, or `CSV`, validating the records, and writing the dataset back out in another format.

The project is intentionally simple: file locations are fixed to the local `input/` and `output/` folders, and the conversion flow is implemented directly in [`converter.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/converter.py:1).

## What The Project Does

- Reads source files from `input/`
- Supports `.json`, `.yaml`, and `.csv` input
- Validates schema, types, and allowed `status` values
- Writes converted files to `output/`
- Includes pytest coverage for parsers, validators, and writers

## Project Layout

```text
test_data_processor/
├── converter.py
├── parsers.py
├── validator.py
├── writers.py
├── transformer.py
├── utils.py
├── input/
├── output/
├── tests/
└── requirements.txt
```

## Requirements

- Python 3
- `PyYAML`
- `pytest` for running tests

Install dependencies with:

```bash
pip install -r requirements.txt
```

## Usage

Run the converter from the repository root:

```bash
python3 converter.py <input-file> <output-file>
```

Examples:

```bash
python3 converter.py data.json converted.yaml
python3 converter.py data.yaml converted.csv
python3 converter.py data.csv converted.json
```

How paths work:

- `<input-file>` is resolved as `input/<input-file>`
- `<output-file>` is resolved as `output/<output-file>`

So this command:

```bash
python3 converter.py data.json converted.yaml
```

reads `input/data.json` and writes `output/converted.yaml`.

## Supported Data Shape

For `JSON` and `YAML`, the tool expects a top-level mapping with a `tests` list:

```json
{
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
```

For `CSV`, each row must contain these columns:

```text
id,name,category,status,priority,duration,vehicle,environment,temperature,executed_by,timestamp
```

When reading CSV, the parser injects metadata as:

- `project: "Unknown"`
- `version: "Unknown"`
- `generated_at: None`

## Validation Rules

Each test record must contain:

- `id`
- `name`
- `category`
- `status`
- `priority`
- `duration`
- `vehicle`
- `environment`
- `temperature`
- `executed_by`
- `timestamp`

Current validation checks:

- `tests` must exist and must not be empty
- `id` must be an `int` and non-negative
- `duration` must be an `int` or `float` and non-negative
- `temperature` must be an `int` or `float`
- `name`, `category`, `status`, `priority`, `vehicle`, `environment`, `executed_by`, and `timestamp` must be strings
- `status` must be either `Passed` or `Failed`

## Current Behavior And Limitations

- Only `.json`, `.csv`, and `.yaml` are handled explicitly
- File locations are hardcoded through [`utils.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/utils.py:1)
- The CLI does not provide help text or argument validation
- If validation fails, the program prints the exception message, but it does not exit early before the writer step
- Empty YAML files load as `None`, which will then fail later during validation
- CSV parsing converts `id` to `int`, `duration` to `float`, and `temperature` to `int` while reading
- [`transformer.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/transformer.py:1) contains a filtering helper, but it is not connected to the CLI flow and currently uses incorrect metadata keys
- [`utils.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/utils.py:1) imports `Path` correctly and simply maps CLI arguments into `input/` and `output/`

## Running Tests

Run the test suite from the repository root:

```bash
pytest
```

The current tests cover:

- parser behavior for valid, empty, malformed, and missing files
- validator behavior for schema, type, and status failures
- writer behavior for JSON, YAML, and CSV output

## Main Modules

- [`converter.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/converter.py:1): CLI entry point and format routing
- [`parsers.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/parsers.py:1): JSON, YAML, and CSV readers
- [`validator.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/validator.py:1): schema and field validation
- [`writers.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/writers.py:1): JSON, YAML, and CSV writers
- [`transformer.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/transformer.py:1): unused status filter helper
- [`utils.py`](/home/adelelakour/TestDataProsessor_local/test_data_processor/utils.py:1): CLI path handling

## Suggested Next Improvements

- stop conversion immediately when validation fails
- add argument count checks and `--help`
- support custom input and output paths
- handle unsupported extensions explicitly
- either fix and integrate `transformer.py` or remove it
- add higher-level integration tests for the full CLI flow

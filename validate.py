import json
import jsonschema

def validate_json(json_data, schema):
    try:
        jsonschema.validate(instance=json_data, schema=schema)
        print("JSON data is valid")
    except jsonschema.exceptions.ValidationError as err:
        print("JSON data is invalid. See error message below.")
        print(err)

if __name__ == "__main__":
    with open("data_contract_test.json", "r") as file:
        json_data = json.load(file)
    with open("schema.json", "r") as file:
        schema = json.load(file)
    validate_json(json_data, schema)

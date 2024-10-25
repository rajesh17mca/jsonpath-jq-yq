import yaml
import json

def yaml_to_json(yaml_file_path, json_file_path):
    # Open and load YAML data
    with open(yaml_file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
    
    # Convert to JSON and save
    with open(json_file_path, 'w') as json_file:
        json.dump(data, json_file, indent=4)
    
    print(f"JSON file created at: {json_file_path}")

# Usage
yaml_file_path = 'data.yaml'   # Replace with your YAML file path
json_file_path = 'data.json'   # Replace with your desired JSON file path
yaml_to_json(yaml_file_path, json_file_path)

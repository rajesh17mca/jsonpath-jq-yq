import json
import yaml

def json_to_yaml(json_file_path, yaml_file_path):
    # Open and load JSON data
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Convert JSON data to YAML format and save
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)
    
    print(f"YAML file created at: {yaml_file_path}")

# Usage
json_file_path = 'data.json'   # Replace with your JSON file path
yaml_file_path = 'data.yaml'   # Replace with your desired YAML file path
json_to_yaml(json_file_path, yaml_file_path)

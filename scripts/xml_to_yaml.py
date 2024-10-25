import xml.etree.ElementTree as ET
import yaml

def xml_to_dict(element):
    """Recursively converts an XML element and its children to a dictionary."""
    data = {}
    # Convert child elements to dictionary keys
    if len(element):
        for child in element:
            if child.tag not in data:
                data[child.tag] = []
            data[child.tag].append(xml_to_dict(child))
        # Flatten lists with a single element
        for key in data:
            if len(data[key]) == 1:
                data[key] = data[key][0]
    else:
        # Add text content if no children
        data = element.text or ''
    return data

def xml_to_yaml(xml_file_path, yaml_file_path):
    # Parse XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Convert XML to dictionary
    data_dict = {root.tag: xml_to_dict(root)}
    
    # Convert dictionary to YAML and save
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.dump(data_dict, yaml_file, default_flow_style=False)
    
    print(f"YAML file created at: {yaml_file_path}")

# Usage
xml_file_path = 'data.xml'     # Replace with your XML file path
yaml_file_path = 'data.yaml'   # Replace with your desired YAML file path
xml_to_yaml(xml_file_path, yaml_file_path)

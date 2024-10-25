import xml.etree.ElementTree as ET
import json

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

def xml_to_json(xml_file_path, json_file_path):
    # Parse XML
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    # Convert XML to dictionary
    data_dict = {root.tag: xml_to_dict(root)}
    
    # Convert dictionary to JSON and save
    with open(json_file_path, 'w') as json_file:
        json.dump(data_dict, json_file, indent=4)
    
    print(f"JSON file created at: {json_file_path}")

# Usage
xml_file_path = 'data.xml'     # Replace with your XML file path
json_file_path = 'data.json'   # Replace with your desired JSON file path
xml_to_json(xml_file_path, json_file_path)

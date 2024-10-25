import json
import xml.etree.ElementTree as ET

def dict_to_xml(tag, data):
    """Recursively converts a dictionary to XML."""
    element = ET.Element(tag)
    for key, val in data.items():
        if isinstance(val, dict):
            child = dict_to_xml(key, val)
            element.append(child)
        elif isinstance(val, list):
            for item in val:
                child = dict_to_xml(key, item)
                element.append(child)
        else:
            child = ET.Element(key)
            child.text = str(val)
            element.append(child)
    return element

def json_to_xml(json_file_path, xml_file_path):
    # Load JSON data
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Convert to XML
    root_element_name = 'root'  # Root name for XML
    root = dict_to_xml(root_element_name, data)
    
    # Save XML to file
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
    
    print(f"XML file created at: {xml_file_path}")

# Usage
json_file_path = 'data.json'   # Replace with your JSON file path
xml_file_path = 'data.xml'     # Replace with your desired XML file path
json_to_xml(json_file_path, xml_file_path)

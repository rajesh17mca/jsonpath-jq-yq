import yaml
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

def yaml_to_xml(yaml_file_path, xml_file_path):
    # Load YAML data
    with open(yaml_file_path, 'r') as yaml_file:
        data = yaml.safe_load(yaml_file)
    
    # Convert to XML
    root_element_name = 'root'  # Root name for XML
    root = dict_to_xml(root_element_name, data)
    
    # Save XML to file
    tree = ET.ElementTree(root)
    tree.write(xml_file_path, encoding='utf-8', xml_declaration=True)
    
    print(f"XML file created at: {xml_file_path}")

# Usage
yaml_file_path = 'data.yaml'   # Replace with your YAML file path
xml_file_path = 'data.xml'     # Replace with your desired XML file path
yaml_to_xml(yaml_file_path, xml_file_path)

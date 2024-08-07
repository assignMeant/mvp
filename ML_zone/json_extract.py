import json

import re

def extract_student_data(content):
    data = {}
    try:
        # Split the content into separate JSON objects
        json_objects = content.strip().split('\n\n')
        for json_object in json_objects:
            if json_object.strip():  # Ensure it's not an empty string
                parsed_object = json.loads(json_object.strip())
                student_id = str(parsed_object["student_id"])  # Convert student_id to string
                data[student_id] = parsed_object["questions"]
    except json.JSONDecodeError as e:
        print(f"Failed to parse JSON response: {e}")
    return data

def save_combined_json(data, output_file):
    with open(output_file, 'w') as file:
        json.dump(data, file, indent=4)
    print(f"Combined JSON saved to {output_file}")

def main(response_content):
    # Response content
    #response_content 
  
    combined_data = extract_student_data(response_content)
    
    print(f"Combined student data: {combined_data}")
    return combined_data
   


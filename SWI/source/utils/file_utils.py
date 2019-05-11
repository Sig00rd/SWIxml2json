import json
import pathlib

from typing import List


INPUT_FILE_PATH = pathlib.Path(__file__).parents[2] / 'input.xml'
OUTPUT_FILE_PATH = pathlib.Path(__file__).parents[2] / 'output.json'


def load_xml_object_list_from_input_file() -> List[str]:
    xml_objects, current_object = [], ""

    with open(INPUT_FILE_PATH, 'r') as file:
        for line in file:
            line.replace("\n", "")
            current_object += line

            if "</object>" in line:
                xml_objects.append(current_object)
                current_object = ""

    return xml_objects


def dump_dictionary_to_output_file_as_json(object_dictionary):
    with open(OUTPUT_FILE_PATH, 'w+') as output_file:
        json.dump(object_dictionary, output_file, indent=4)

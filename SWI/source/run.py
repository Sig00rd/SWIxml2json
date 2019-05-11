from utils import file_utils, converter


def run():
    try:
        xml_objects = file_utils.load_xml_object_list_from_input_file()
        object_dictionary = converter.convert_xml_objects_to_dictionary(xml_objects)
        file_utils.dump_dictionary_to_output_file_as_json(object_dictionary)

    except FileNotFoundError:
        print("Input file not found")


if __name__ == "__main__":
    run()

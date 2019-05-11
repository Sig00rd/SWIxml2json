import xml.etree.ElementTree as ElementTree


from utils import config, string_utils


def build_fields_dictionary(fields_root):
    fields_dictionary = dict()

    for field in fields_root.findall("field"):
        try:
            field_name, field_type, field_value = \
                field.find("name").text, field.find("type").text, field.find("value").text

        # ignore field if it doesn't have either of: name, type or value
        except AttributeError:
            continue

        # ignore field if its type is not supported
        if field_type not in config.VALID_FIELD_TYPES:
            continue

        if field_type == 'int':
            try:
                field_value = int(field_value)
            except ValueError:
                continue

        fields_dictionary[field_name] = field_value
    return fields_dictionary


def get_roots_from_object_xmls(object_xmls):
    roots = []
    for object_xml in object_xmls:
        try:
            roots.append(ElementTree.fromstring(object_xml))
        except ElementTree.ParseError:
            continue
    return roots


def convert_xml_objects_to_dictionary(object_xmls):
    objects_dictionary = dict()

    object_xmls = list(filter(string_utils.contains_only_printable_characters, object_xmls))

    roots = get_roots_from_object_xmls(object_xmls)

    for root in roots:
        '''
        if the mentioned flag is checked in config file,
        ignore object if it has an unsupported field (refer to readme)
        '''
        if config.SKIP_OBJECTS_WITH_UNSUPPORTED_KEYWORDS:
            if any(child.tag not in config.SUPPORTED_KEYWORDS for child in root):
                continue

        try:
            name = root.find("obj_name").text

        # ignore object if it has no obj_name field (is invalid)
        except AttributeError or TypeError:
            continue

        # ignore object if it has no text in obj_name field (is invalid)
        if not name:
            continue

        fields = build_fields_dictionary(root)

        # ignore object if it has no valid fields (is invalid)
        if not fields:
            continue

        objects_dictionary[name] = fields

    return objects_dictionary

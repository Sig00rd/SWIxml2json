import string


def filter_non_printable_characters(text: string) -> string:
    return "".join(filter(lambda x: x in string.printable, text))


def contains_only_printable_characters(text: string) -> bool:
    return all(character in string.printable for character in text)


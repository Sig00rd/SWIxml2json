from SWI.source.utils import string_utils


# contains_only_printable_characters
def test_should_return_true_given_input_string_with_only_printable_characters():
    input_string = "sample input"
    assert(string_utils.contains_only_printable_characters(input_string)) is True


def test_should_return_true_given_input_string_with_non_printable_character():
    input_string = "\t"
    assert (string_utils.contains_only_printable_characters(input_string)) is False

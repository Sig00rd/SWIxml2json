from SWI.source.utils import string_utils


# contains_only_printable_characters
def test_should_return_true_given_input_string_with_only_printable_characters():
    input_string = "sample input"
    assert(string_utils.contains_only_printable_characters(input_string)) is True


def test_should_return_false_given_input_string_with_non_printable_character():
    input_string = "\x01"
    assert(string_utils.contains_only_printable_characters(input_string)) is False


def test_should_return_true_given_empty_input_string():
    input_string = ""
    assert(string_utils.contains_only_printable_characters(input_string)) is True


# filter_non_printable_characters
def test_should_return_unchanged_input_given_fully_printable_input():
    # given
    input_string = "sample input"
    # when
    output_string = string_utils.filter_non_printable_characters(input_string)
    # then
    assert input_string == output_string


def test_should_not_return_unchanged_input_given_partially_nonprintable_input():
    # given
    input_string = "sampleinp\x01ut"
    # when
    output_string = string_utils.filter_non_printable_characters(input_string)
    # then
    assert input_string != output_string


def test_should_return_printable_part_changed_given_partially_nonprintable_input():
    # given
    input_string = "sampleinp\x01ut"
    # when
    output_string = string_utils.filter_non_printable_characters(input_string)
    # then
    expected_output_string = "sampleinput"
    assert output_string == expected_output_string


def test_should_return_empty_string_given_fully_nonprintable_input():
    #given
    input_string = "\x01\x01"
    # when
    output_string = string_utils.filter_non_printable_characters(input_string)
    # then
    expected_output_string = ""
    assert output_string == expected_output_string

from src.str_arrays.string_reversal import reverse_string, reverse_string_rec


def test_reverse_string_odd_number_letter():
    input_string = "hello world"
    reversed_string = reverse_string(input_string)
    expected_string = "dlrow olleh"
    assert reversed_string == expected_string


def test_reverse_string_even_number_letter():
    input_string = "helloworld"
    reversed_string = reverse_string(input_string)
    expected_string = "dlrowolleh"
    assert reversed_string == expected_string


def test_reverse_string_rec_odd_number_letter():
    input_string = "hello world"
    reversed_string = reverse_string_rec(input_string)
    expected_string = "dlrow olleh"
    assert reversed_string == expected_string


def test_reverse_string_even_number_letter():
    input_string = "helloworld"
    reversed_string = reverse_string_rec(input_string)
    expected_string = "dlrowolleh"
    assert reversed_string == expected_string

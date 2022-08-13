def reverse_string(string_to_reverse: str) -> str:
    reversed_string = list(string_to_reverse)
    start_index = 0
    end_index = len(string_to_reverse) - 1
    while start_index < end_index:
        temp_swap_value = reversed_string[start_index]
        reversed_string[start_index] = reversed_string[end_index]
        reversed_string[end_index] = temp_swap_value
        start_index += 1
        end_index -= 1
    return "".join(reversed_string)


def reverse_string_rec(string_to_reverse: str) -> str:
    reversed_string = list(string_to_reverse)
    start_index = 0
    end_index = len(string_to_reverse) - 1
    swap_letters(reversed_string, start_index, end_index)
    return "".join(reversed_string)


def swap_letters(string_to_reverse: str, start_index: int, end_index: int):
    if start_index > end_index:
        return
    temp_swap_value = string_to_reverse[start_index]
    string_to_reverse[start_index] = string_to_reverse[end_index]
    string_to_reverse[end_index] = temp_swap_value
    swap_letters(string_to_reverse, start_index + 1, end_index - 1)

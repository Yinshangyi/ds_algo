def sort_string(string_to_sort: str) -> str:
    sorted_list_from_string = sorted(list(string_to_sort))
    return "".join(sorted_list_from_string)


def is_strings_permutations(str1: str, str2: str) -> bool:
    sorted_str1 = sort_string(str1)
    sorted_str2 = sort_string(str2)
    return sorted_str1 == sorted_str2


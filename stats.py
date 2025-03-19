def get_num_words(text: str) -> int:
    return len(text.split())


def get_num_chars(text: str) -> dict:
    count_dict = {}
    for char in text:
        if char.lower() in count_dict:
            count_dict[char.lower()] += 1
        else:
            count_dict[char.lower()] = 1
    return count_dict


def get_sorted_charcount(count_dict: dict) -> list:
    return sorted(count_dict.items(), key=lambda item: item[1], reverse=True)

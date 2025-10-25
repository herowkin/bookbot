def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    chars = {}
    for c in text.lower():
        if c in chars:
            chars[c] += 1
        else:
            chars[c] = 1
    return chars


def sort_on(item):
    return item["num"]


def sort_chars_dict(char_dict):
    sorted_list = []
    for char, num in char_dict.items():
        sorted_list.append({"char": char, "num": num})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

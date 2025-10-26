def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    counts = {}
    for c in text.lower():
        if c.isalpha():                   # count letters only
            counts[c] = counts.get(c, 0) + 1
    return counts

def sort_on(item):
    return item["num"]

def sort_chars_dict(char_dict):
    out = [{"char": ch, "num": n} for ch, n in char_dict.items()]
    out.sort(reverse=True, key=sort_on)   # highest count first
    return out

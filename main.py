from stats import get_num_words, get_num_chars


def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    chars_dict = get_num_chars(text)
    print(chars_dict)


def get_book_text(path):
       with open(path, "r", encoding="utf-8-sig") as f:
        return f.read()


main()
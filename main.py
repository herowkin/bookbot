import sys
from stats import get_num_words, get_num_chars, sort_chars_dict

def get_book_text(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)

    num_words = get_num_words(text)
    print(f"Found {num_words} total words")

    chars_dict = get_num_chars(text)  # letters only, lowercase
    sorted_chars = sort_chars_dict(chars_dict)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

if __name__ == "__main__":
    main()

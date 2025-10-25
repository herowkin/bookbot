from stats import get_num_words, get_num_chars, sort_chars_dict

def get_book_text(path):
    with open(path, "r", encoding="utf-8-sig") as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    num_words = get_num_words(text)
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    chars_dict = get_num_chars(text)
    sorted_chars = sort_chars_dict(chars_dict)

    for item in sorted_chars:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")

    print("============= END ===============")

main()

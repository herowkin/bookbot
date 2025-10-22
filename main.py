from pathlib import Path

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        return f.read()

def count_words(text):
    return len(text.split())

def main():
    # Resolve a path relative to this file so it works no matter where you run it from
    book_path = Path(__file__).parent / "books" / "frankenstein.txt"
    if not book_path.exists():
        print(f"Could not find: {book_path}")
        print("Make sure the file exists at: project_root/books/frankenstein.txt")
        return

    text = get_book_text(book_path)
    num_words = count_words(text)
    print(f"Found {num_words} total words")

if __name__ == "__main__":
    main()

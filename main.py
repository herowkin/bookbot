def get_book_text(filepath: str) -> str:
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

if __name__ == "__main__":
    main()

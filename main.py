import sys
from stats import get_num_words, get_num_chars, get_sorted_charcount

def get_book_text(filepath: str) -> str:
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return ""


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    book_text = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book_text)} total words")
    print("----------- Character Count ----------")
    sorted_list = get_sorted_charcount(get_num_chars(book_text))
    for char, count in sorted_list:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()



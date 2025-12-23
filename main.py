import sys
from stats import count_words, count_chars, sort_chars

def get_book_text(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        file_contents = file.read()
    return file_contents

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words(book)} total words.")
    print("--------- Character Count -------")
    for char in sort_chars(book):
        print(f"{char["char"]}: {char["num"]}")
    print("============= END ===============")


main()
# debug()
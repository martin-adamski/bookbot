import sys
from stats import get_num_words, char_count, sorted_dictionary

def get_book_text(file):
    with open(file) as f:
        file_contents = f.read()
    return file_contents

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_location = sys.argv[1]
    num_words = get_num_words(get_book_text(book_location))
    character_dictionary = sorted_dictionary(char_count(get_book_text(book_location)))

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_location}..")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    for dictionary in character_dictionary:
        if dictionary["char"].isalpha():
            print(f"{dictionary["char"]}: {dictionary["num"]}")


main()

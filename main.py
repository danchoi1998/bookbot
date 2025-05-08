from stats import get_word_count, get_character_count, sort_dict
import sys

def get_book_text(book):
    with open(book) as f:
        book_text = f.read()

    return book_text

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    sorted_char_values = sort_dict(get_character_count(sys.argv[1]))

    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at {sys.argv[1]}...
    ----------- Word Count ----------
    Found {get_word_count(sys.argv[1])} total words
    --------- Character Count -------""")
    for kv_pair in sorted_char_values:
        print(f"{kv_pair["char"]}: {kv_pair["num"]}")
    print("============= END ===============")

main()
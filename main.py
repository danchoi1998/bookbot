from stats import get_word_count, get_character_count, sort_dict

def get_book_text(book):
    with open(book) as f:
        book_text = f.read()

    return book_text

def main():

    sorted_char_values = sort_dict(get_character_count("books/frankenstein.txt"))

    print(f"""
    ============ BOOKBOT ============
    Analyzing book found at books/frankenstein.txt...
    ----------- Word Count ----------
    Found {get_word_count("books/frankenstein.txt")} total words
    --------- Character Count -------""")
    for kv_pair in sorted_char_values:
        print(f"{kv_pair["char"]}: {kv_pair["num"]}")
    print("============= END ===============")

main()
from stats import get_word_count, get_character_count

def get_book_text(book):
    with open(book) as f:
        book_text = f.read()

    return book_text

def main():
    character_count = get_character_count("books/frankenstein.txt")
    print(f"{get_word_count("books/frankenstein.txt")} words found in the document")
    print(character_count)

main()
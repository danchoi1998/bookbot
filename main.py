from stats import get_word_count

def get_book_text(book):
    with open(book) as f:
        book_text = f.read()

    return book_text

def main():
    print(f"{get_word_count("books/frankenstein.txt")} words found in the document")

main()
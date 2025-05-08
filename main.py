def get_book_text(book):
    with open(book) as f:
        book_text = f.read()

    return book_text

def get_word_count(document):
    with open(document) as f:
        text = f.read()

    word_count = len(text.split())

    return word_count


def main():
    print(f"{get_word_count("books/frankenstein.txt")} words found in the document")

main()
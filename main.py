def get_book_text(book):
    with open(book) as f:
        book_text = f.read()

    return book_text

def main():
    print(get_book_text("books/frankenstein.txt"))

main()
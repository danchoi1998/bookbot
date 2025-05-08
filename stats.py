def get_word_count(document):
    with open(document) as f:
        text = f.read()

    word_count = len(text.split())

    return word_count
def get_word_count(document):
    with open(document) as f:
        text = f.read()

    word_count = len(text.split())

    return word_count

def get_character_count(document):
    with open(document) as f:
        text = f.read()

    cc_dict = {}
    
    for character in text.lower():
        if character not in cc_dict:
            cc_dict[character] = 0
        cc_dict[character] += 1
    
    return cc_dict

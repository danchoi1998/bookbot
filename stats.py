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

def sort_on(char_num_pair):
    return char_num_pair["num"]

def sort_dict(dictionary):
    sorted_dict = []
    for char in dictionary:
        if char.isalpha() == True:
            kv_pair = {"char": char, "num": dictionary[char]}
            sorted_dict.append(kv_pair)

    sorted_dict.sort(key=sort_on, reverse=True)

    return sorted_dict
        



    


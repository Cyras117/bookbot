def get_num_words(text):
    words = text.split()
    return len(words)

def sort_on(itens):
    return itens['count']

def get_letters_from_text(text):
    letters={}
    for char in text.lower():
        if char.isalpha():
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
    return letters

def letters_dict_to_list(letters_dict):
    letters_list = []
    for key, value in letters_dict.items():
        letters_list.append({"name": key, "count": value})
    return letters_list

def get_letter_count(text):
    letters = get_letters_from_text(text)
    letters_dict = letters_dict_to_list(letters)
    letters = sorted(letters_dict, key=sort_on, reverse=True)
    return letters

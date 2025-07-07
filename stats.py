def get_num_words(text):
    words = text.split()
    return len(words)

def search_letter(letter, letters):
    for l in letters:
        if l["name"] == letter:
            return letters.index(l)
    return -1


def get_letter_count(text):
    letters = []
    for char in text.lower():
        if char.isalpha():
            src_result = search_letter(char,letters)
            if src_result == -1:
                letters.append({"name": char, "count": 1})
            else:
                letters[src_result]["count"] += 1
    return letters

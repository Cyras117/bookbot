def get_file_text(file_name):
    file_path = f"books/{file_name}"
    with open(file_path) as file:
        return file.read()
    
def get_word_count(string):
    return len(string.split())

def get_letters_count(string):
    letters = {}
    string = string.lower()
    for l in string:
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

def sort_on(dict):
    return dict["count"]

def dict_to_list_letters(dict):
    l = []
    for i in dict:
        l.append({"letter":i,"count":l[i]})
    return l

def show_report(file_name):
    file_text=get_file_text(file_name)
    letter_count = get_letters_count(file_text)
    letter_count_list = dict_to_list_letters(letter_count)
    letter_count_list.sort(reverse=True,key=sort_on)
    
    print(f"--- Begin report of books/{file_name} ---")
    print(f"\n{get_word_count(file_text)} words found in the document")
    for i in letter_count_list:
        if i["letter"].isalpha():
            print(f"The {i["letter"]} character was found {i["count"]} times")
    print("\n--- End report ---")

def main():
    show_report("frankenstein.txt")

main()
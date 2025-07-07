from stats import get_num_words, get_letter_count

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def sort_on(itens):
    return itens['count']

def main():
    filepath = "/home/saryc/bootdev/projects/bookbot/books/frankenstein.txt"
    text = get_book_text(filepath)
    count = get_letter_count(text)
    count.sort(key=sort_on, reverse=True)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for letter in count:
        print(f"{letter['name']}: {letter['count']}")

if __name__ == "__main__":
    main()

def get_book_text(self, filepath):
    with open(filepath) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def main():
    filepath = "/home/saryc/bootdev/projects/bookbot/books/frankenstein.txt"
    text = get_book_text(None, filepath)
    num_words = get_word_count(text)
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()
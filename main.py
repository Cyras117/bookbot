
def get_book_text(self, filepath):
    with open(filepath) as f:
        return f.read()

def main():
    filepath = "/home/saryc/bootdev/projects/bookbot/books/frankenstein.txt"
    text = get_book_text(None, filepath)
    print(text)

if __name__ == "__main__":
    main()
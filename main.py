# Import functions
from stats import get_num_words, get_letter_count  
import sys

# Reads the entire contents of the file at the given filepath
def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

# Main function to analyze a book file
def main():
    # Check if the user provided a file path argument
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    # Read the book text from the provided file path
    text = get_book_text(sys.argv[1])
    count = get_letter_count(text)

    # Print the results
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")
    for letter in count:
        print(f"{letter['name']}: {letter['count']}")

if __name__ == "__main__":
    # Entry point of the script
    main()
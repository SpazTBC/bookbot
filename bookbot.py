import sys
from stats import count_letters, get_num_words

def get_book_text(filepath):
    with open(filepath, encoding="utf8") as f:
        return f.read()

def main():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 bookbot.py <path_to_book>")
        sys.exit(1)
    
    # Get the book path from command line arguments
    book_path = sys.argv[1]
    
    try:
        text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: The file '{book_path}' was not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading the file: {e}")
        sys.exit(1)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    
    # Get and print word count
    word_count = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    
    # Get character counts
    char_counts = count_letters(text)
    
    # Sort characters by count (descending)
    sorted_chars = sorted(char_counts.items(), key=lambda x: x[1], reverse=True)
    
    # Print character counts
    print("--------- Character Count -------")
    for char, count in sorted_chars:
        if char.isalpha():  # Only print alphabetic characters
            print(f"{char}: {count}")
    
    print("============= END ===============")

if __name__ == "__main__":
    main()

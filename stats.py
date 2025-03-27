def count_letters(text):
    # Create an empty dictionary
    letter_counts = {}
    
    # Convert text to lowercase
    text = text.lower()
    
    # Loop through each character in the text
    for char in text:
        # Count all characters (including symbols and spaces)
        if char in letter_counts:
            letter_counts[char] += 1
        else:
            letter_counts[char] = 1
    
    return letter_counts

def get_num_words(text):
    words = text.split()
    return len(words)

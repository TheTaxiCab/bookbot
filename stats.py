def get_num_words(book_text):
    """
    Counts the number of words in the given book text.
    :param book_text: The text of the book.
    :return: The number of words in the book.
    """
    if not book_text:
        return 0
    words = book_text.split()
    return len(words)

def get_unique_characters(book_text):
    """
    Counts the number of unique characters in the given book text.
    :param book_text: The text of the book.
    :return: The number of unique characters (including symbols and spaces) in the book as a dictonary
    """
    if not book_text:
        return {}
    
    unique_chars = {}
    for char in book_text.lower():  # Convert to lowercase to ensure case insensitivity
        if char in unique_chars:
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars

def sort_list(dictionary):
    """
    Sorts the dictionary by keys
    :param dictionary: The dictionary to sort
    :return: A sorted list of tuples from the dictionary
    """
    if not dictionary:
        return []
    
    sorted_list = sorted(dictionary.items())
    return sorted_list
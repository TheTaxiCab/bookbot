from stats import get_num_words, get_unique_characters, sort_list
import sys

def get_book_text(filepath):
    """
    Reads the content of a book file and returns it as a string.
    :param filepath: Path to the book file.
    :return: Content of the book as a string.
    """
    with open(filepath) as f:
        return f.read()
    
def main():
    if sys.argv.__len__() < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path =sys.argv[1] 

    book_txt = get_book_text(book_path)

    num_words = get_num_words(book_txt)
    unique_char = get_unique_characters(book_txt)

    sorted_unique_char = sort_list(unique_char)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for character in sorted_unique_char:
        if character[0].isalpha():
            print(f"{character[0]}: {character[1]}")
    print("============= END ===============")


main()
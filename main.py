from stats import get_book_text
from stats import count_chars
from stats import print_stats
import sys
# The function get_book_text is imported from the stats module
# and is used to count the number of words in a book text file.
def main():
    #path_to_file = 'books/frankenstein.txt'

    if(len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_words = book_text.split()
    res = count_chars(book_text.lower())
    sorted_res = dict(sorted(res.items(), key=lambda x: x[1], reverse=True))

    print_stats(sys.argv[1],len(num_words),sorted_res)
if __name__ == "__main__":
    main()
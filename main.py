from stats import (count_words, count_chars, sort_chars)
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        fileContents = f.read()
    return fileContents

def main():
    if len(sys.argv) < 2: 
        print("Usage: python3 main.py <path_to_book>") 
        sys.exit(1)
    filepath = sys.argv[1]
    bookContents = get_book_text(filepath)
    numWords = count_words(bookContents)
    numChars = count_chars(bookContents)
    sortedChars = sort_chars(numChars)

    print(f"============ BOOKBOT ============\nAnalyzing book found at {filepath}...\n----------- Word Count ----------\nFound {numWords} total words\n--------- Character Count -------")
    for line in sortedChars: print(f"{line['char']}: {line['num']}")
    print("============= END ===============")



if __name__ == '__main__':
    main()

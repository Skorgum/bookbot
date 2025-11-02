import sys
from stats import get_book_text, count_characters, sort_count

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    text = get_book_text(filepath)
    num_words = len(text.split())

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    characters = sort_count(count_characters(text))
    for character in characters:
        ch = character["char"]
        if ch.isalpha():
            print(f"{ch}: {character['num']}")
    print("============= END ===============")
    
main()
from stats import get_book_text

def main():
      filepath = "books/frankenstein.txt"
      num_words = len(get_book_text(filepath).split())
      print(f"Found {num_words} total words")
main()
      
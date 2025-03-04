from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)

    num_words = count_words(book_text)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    char_counts = count_characters(book_text)
    sorted_chars = sort_characters(char_counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['count']}")

    print("============= END ===============")

if __name__ == "__main__":
    main()
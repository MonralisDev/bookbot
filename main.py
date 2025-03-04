import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(filepath):
    with open(filepath, encoding="utf-8") as f:
        return f.read()

def main():
    # Перевіряємо, чи переданий аргумент (шлях до книги)
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]  # Отримуємо шлях до файлу з аргументу

    try:
        book_text = get_book_text(book_path)
    except FileNotFoundError:
        print(f"Error: File '{book_path}' not found.")
        sys.exit(1)

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
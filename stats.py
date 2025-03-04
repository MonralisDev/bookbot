def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    text = text.lower()

    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    return char_count

def sort_characters(char_dict):
    sorted_list = [{"char": char, "count": count} for char, count in char_dict.items() if char.isalpha()]
    sorted_list.sort(key=lambda d: d["count"], reverse=True)  # Сортуємо за кількістю входжень
    return sorted_list
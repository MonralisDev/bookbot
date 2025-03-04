def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    char_count = {}
    text = text.lower()

    for chair in text:
        if chair in char_count:
            char_count[chair] += 1
        else:
            char_count[chair] = 1
    return char_count
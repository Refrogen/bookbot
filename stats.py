def get_num_words(book_text):
    if not book_text:
        return 0
    words = book_text.split()
    return len(words)

def get_unique_characters(book_text):
    if not book_text:
        return {}
    
    unique_chars = {}
    for char in book_text.lower():
        if char in unique_chars:
            unique_chars[char] += 1
        else:
            unique_chars[char] = 1
    return unique_chars

def sort_list(dictionary):
    if not dictionary:
        return []
    
    sorted_list = sorted(dictionary.items())
    return sorted_list
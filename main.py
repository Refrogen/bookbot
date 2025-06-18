def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def main():
    story = get_book_text("frankenstein.txt")
    num_words = get_num_words(story)
    print(f"{num_words} words found in the document")

def get_num_words(story):
    if not story:
        return 0
    words = story.split()
    return len(words)

main()
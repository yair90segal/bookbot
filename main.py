def main():
    path = "books/frankenstein.txt"
    file_contents = get_text_by_path(path)
    print(file_contents)

    print(word_count(file_contents))

def get_text_by_path(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

main()
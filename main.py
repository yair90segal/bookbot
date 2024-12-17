def main():
    path = "books/frankenstein.txt"
    file_contents = get_text_by_path(path)
    # print(file_contents)

    # print(word_count(file_contents))
    word_count_val = word_count(file_contents)
    char_dict = char_count(file_contents)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count_val} words found in the document")
    for key in char_dict:
        print(f"The '{key}' character was found {char_dict[key]} times")
    
    print("--- End report ---")


def get_text_by_path(path):
    with open(path) as f:
        return f.read()

def word_count(text):
    return len(text.split())

def char_count(text):
    char_dict = {}
    for ch in text:
        ch_lower = ch.lower()
        if ch_lower in char_dict:
            char_dict[ch_lower] += 1
        else:
            char_dict[ch_lower] = 1
    return char_dict

main()
def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    n_characters = get_n_characters(text)
    # print(f"{num_words} words found in the document")
    # print(n_characters)
    print_report(text)


def get_num_words(text):
    words = text.split()
    return len(words)

def get_n_characters(text):
    lowered = text.lower()
    unique_chars = set(lowered)
    n_appearances = {char: lowered.count(char) for char in unique_chars}
    return n_appearances

def sort_on(dict):
    return dict["num"]

def print_report(text):
    report_dict = []
    total_words = get_num_words(text)
    n_characters = get_n_characters(text)
    for char, num in n_characters.items():
        if char.isalpha():
            report_dict.append({"char": char, "num": num})
    report_dict.sort(key=sort_on, reverse=True)
    print(f"{total_words} total words found in the document")
    for entry in report_dict:
        print(f"The {entry['char']} appears {entry['num']} times")
    


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
main()

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_book_text(path_to_file)
    report(file_contents)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    all_words = text.split()
    number_of_words = len(all_words)
    return number_of_words

def num_of_times_each_char_appeared(text):
    result_dict = {}
    for char in text:
        lowered_char = char.lower()
        if lowered_char in result_dict:
            result_dict[lowered_char] += 1
        else:
            result_dict[lowered_char] = 1
    return result_dict

def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    total = count_words(text) # Get total number of words in the text
    print(f"{total} words found.")
    char_dict = num_of_times_each_char_appeared(text) # Get a dictionary of each char and thier total number in the text
    char_list = []
    for char in char_dict:
        if char.isalpha():
            char_list.append(char) # We append chars from dictionary to list so we can sort them from A to Z.
    char_list.sort() # Sort new list
    for char in char_list:
        print(f"The {char} character was found {char_dict[char]} times.")

main()
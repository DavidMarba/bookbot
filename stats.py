def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_chars(book_text):
    char_dictionary = {}
    for char in book_text:
        lower_char = char.lower()
        if lower_char in char_dictionary:
            char_dictionary[lower_char] += 1
        else:
            char_dictionary[lower_char] = 1
    return char_dictionary

def sort_chars(book_text):
    char_list = []
    char_dictionary = count_chars(book_text)
    for char in char_dictionary:
        if char.isalpha():
            new_char = {"char": char, "num": char_dictionary[char]}
            char_list.append(new_char)
    char_list.sort(key=sort_list, reverse=True)
    return char_list

def sort_list(char_list):
    return char_list["num"]
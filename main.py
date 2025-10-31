from stats import *


def print_message(filepath):
    num_words = count_words(filepath)
    num_characters = get_num_characters(filepath)
    list_nums = new_list(num_characters)
    sorted_list = sort(list_nums)
    print_alphabet_characters(sorted_list)
    print(f"Found {num_words} total words")
    # print(num_characters)
    

print_message("books/frankenstein.txt")


#--Print Contents of the Book--
# def get_book_text(filepath):
#     with open(filepath) as f:
#         file_contents = f.read()
#     return file_contents

# def main():
#     contents_of_book = get_book_text("books/frankenstein.txt")
#     print(contents_of_book)

# main()


from stats import *
import sys


# show a nice page of book anaylze
def print_message(filepath):
    num_words = get_num_words(filepath)
    num_characters = get_num_characters(filepath)
    character_list = get_list(num_characters)
    sorted_list = sort(character_list)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print_alphabet_characters(sorted_list)
    print("============= END ===============")
   
# input filepath and get information of book    
def get_information_book():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        print_message(sys.argv[1])

get_information_book()


# Prints ['main.py']
# # print contents of book
# def get_book_text(filepath):
#     with open(filepath) as f:
#         file_contents = f.read()
#     return file_contents

# def main():
#     contents_of_book = get_book_text("books/frankenstein.txt")
#     print(contents_of_book)

# main()

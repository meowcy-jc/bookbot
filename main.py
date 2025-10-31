from stats import *


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
   
    

print_message("books/frankenstein.txt")


# # print contents of book
# def get_book_text(filepath):
#     with open(filepath) as f:
#         file_contents = f.read()
#     return file_contents

# def main():
#     contents_of_book = get_book_text("books/frankenstein.txt")
#     print(contents_of_book)

# main()


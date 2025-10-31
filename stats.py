def count_words(filepath):
    with open(filepath) as f:
        contents_of_book = f.read()
        words_of_book = contents_of_book.split()

        nums_of_words = len(words_of_book)

    return nums_of_words


def get_num_characters(filepath):
    num_characters = {}

    #--Lowvercarse Alphabet--
    # import string

    # lowercase_alphabet = string.ascii_lowercase
    # list_alphabet = list(lowercase_alphabet)

    # for letter in list_alphabet:
    #     if letter not in num_characters:
    #         num_characters[letter] = 0

    with open(filepath) as f:
        book_contents = f.read()
        lowercase_words = book_contents.lower()
        book_characters = list(lowercase_words)
        # print(book_characters)

        for character in book_characters:
            if character not in num_characters:
                num_characters[character] = 0
        
        for character in book_characters:
            if character in num_characters:
                num_characters[character] += 1

    return num_characters

# create a new dictionary has two values
def new_list(num_characters):
    new_list = []

    for character in num_characters:
        new_list.append({"char": character, "num": num_characters[character]})
    
    return new_list


# sort by num
def sort_on(new_list):
    return new_list["num"]


# sort the list
def sort(new_list):
    new_list.sort(reverse=True, key=sort_on)
    return new_list


# only take alphabet
def print_alphabet_characters(new_list):
    # get a list contains only alphabet
    #--easy way--
    # for item in new_list:
    #     char = item["char"]
    #     count = item["num"]
    #     if char.isalpha():
    #         print(f"{char}: {count}")
    final_dintionary = {}

    #--difficult way one--
    # for item in new_list:
    #     char = item["char"]
    #     count = item["num"]
    #     if char.isalpha():
    #         final_dintionary[char] = count

    # #--bad way--
    # # for k in final_dintionary:
    # #     v = final_dintionary.get(k)
    # #     print(f"{k}: {v}")
    
    # for k, v in final_dintionary.items():
    #     print(f"{k}: {v}")
    
    # Stupidest way...
    print(new_list)
    index = 0
    current_char = new_list[0]["char"]
    last_char = new_list[-1]["char"]

    # while index < len(new_list):
    while True:
        print(f"Checking {current_char} at index {index}")
        if not current_char.isalpha():
            print(f"Removing {new_list[index]}, len {len(new_list)}")
            del new_list[index]
        else:
            print(f"Keeping {new_list[index]}, len {len(new_list)}")   
            index +=1
        
        if current_char == last_char:
            break

        current_char = new_list[index]["char"]

    print(new_list)

# count how many words in this book
def get_num_words(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        book_words = book_contents.split()
        num_words = len(book_words)

    return num_words


# get num of each character
def get_num_characters(filepath):
    num_characters = {}

    with open(filepath) as f:
        book_contents = f.read()
        lowercase_words = book_contents.lower()
        book_characters = list(lowercase_words)

        for character in book_characters:
            if character not in num_characters:
                num_characters[character] = 0
        
        for character in book_characters:
            if character in num_characters:
                num_characters[character] += 1

    return num_characters


# get num of each alphabet character in book
def get_num_alphabet_characters(filepath):

    num_characters = {}

    import string

    lowercase_alphabet = string.ascii_lowercase
    list_alphabet = list(lowercase_alphabet)

    for character in list_alphabet:
        if character not in num_characters:
            num_characters[character] = 0

    with open(filepath) as f:
        book_contents = f.read()
        lowercase_words = book_contents.lower()
        book_characters = list(lowercase_words)
        
        for character in book_characters:
            if character in num_characters:
                num_characters[character] += 1

    return num_characters


# create a new list has two keys
def get_list(num_characters):
    character_list = []

    for character in num_characters:
        character_list.append({"char": character, "num": num_characters[character]})
    
    return character_list


# sort new list by "num"
def sort_on(charcter_list):
    return charcter_list["num"]


# sort the list
def sort(character_list):
    character_list.sort(reverse=True, key=sort_on)
    return character_list


# print alphabet character in list -- 1.easiet way
def print_alphabet_characters(sorted_list):
    for item in sorted_list:
        char = item["char"]
        count = item["num"]

        if char.isalpha():
            print(f"{char}: {count}")

            
# print alphabet character in list -- 2.transfer list to dictionary
def print_alphabet_characters_hard(sorted_list):
    final_dictionary = {}

    for item in sorted_list:
        char = item["char"]
        count = item["num"]

        if char.isalpha():
            final_dictionary[char] = count
    
    for char, count in final_dictionary.items():
        print(f"{char}: {count}")

    # other way to print
    # for char in final_dintionary:
    #     count = final_dintionary.get(char)
    #     print(f"{char}: {count}")
    

# print alphabet character in list -- 3. delete non alphabet character
def print_alphabet_characters_bad(sorted_list):
    index = 0
    current_char = sorted_list[0]["char"]
    last_char = sorted_list[-1]["char"]

    while index < len(sorted_list):
        if not current_char.isalpha():
            del sorted_list[index]
        else:  
            index +=1
        
        # if current_char == last_char:
        #     break 

        # current_char = sorted_list[index]["char"]

        if current_char != last_char:
            current_char = sorted_list[index]["char"] 

    for item in sorted_list:
        char = item["char"]
        count = item["num"]
        print(f"{char}: {count}")

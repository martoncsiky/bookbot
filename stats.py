def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def get_num_words(filepath):
    num_words = 0
    words = str.split(get_book_text(filepath))
    for word in words:
        num_words += 1
    return num_words

def count_characters(filepath):
    letter_dict = {}
    raw_string = get_book_text(filepath).lower()
    for char in raw_string:
        if char in letter_dict:
            letter_dict[char] += 1
        else:
            letter_dict[char] = 1
    return letter_dict

def sort_on(dict):
    # This should return the count value from each dictionary
    return list(dict.values())[0]

def report(filepath):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(filepath)} total words")
    print("--------- Character Count -------")
    letter_dict = count_characters(filepath)

    letters_list = []
    for key, value in letter_dict.items():
        if key.isalpha():
            letters_list.append({key: value})

    letters_list.sort(reverse=True, key=sort_on)

    for char_dict in letters_list:
        for key, value in char_dict.items():
            print(f"{key}: {value}")

    print("============= END ===============")
    

    



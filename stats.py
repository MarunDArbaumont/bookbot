def count_words(file_content):
    words = file_content.split()
    return len(words)

def count_character(file_content):
    characters = {}
    for char in file_content:
        char = char.lower()
        if char in characters:
            characters[char] += 1
        else:
            characters[char] = 1
    return characters

def sort_on(char_count):
    char_list = []
    for char, count in char_count.items():
        if char.isalpha():
            char_dict = {"char": char, "count" : count}
            char_list.append(char_dict)

    def sort_on(dict):
        return dict["count"]
    char_list.sort(reverse=True, key=sort_on)
    return char_list

def print_word(characters):
        print("--------- Character Count -------")
        for character in characters:
            print(f"{character["char"]}: {character["count"]}")

def report(book, word_counter, characters):
    print(f"============ BOOKBOT ============\nAnalyzing book found at {book}... \n ---------- Word Count ----------\nFound {word_counter} total words")
    print_word(characters)
    print("============= END ===============")
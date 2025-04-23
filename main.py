from stats import count_words, count_character, report, sort_on
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content




def main():
    try:
        file_content = get_book_text(sys.argv[1])
        word_counter = count_words(file_content)
        characters = count_character(file_content)
        characters = sort_on(characters)
        return report(sys.argv[1], word_counter, characters)
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
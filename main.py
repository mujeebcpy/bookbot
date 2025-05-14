from stats import get_no_of_words
from stats import get_num_charecters
from stats import get_sorted_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        file_content = f.read()
    return file_content

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>    ")
        sys.exit(1)
    book_path = sys.argv[1]
    
    text = get_book_text(book_path)
    num_words = get_no_of_words(text)
    print(f"{num_words} words found in the document")
    char_count = get_num_charecters(text)
    dic_list = get_sorted_dict(char_count)
    print_report(book_path, num_words, dic_list)
    
    
            
def print_report(book_path, num_words, chars_sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in chars_sorted_list:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["num"]}")
    print("============= END ===============")        



main()    

def get_no_of_words(text):
    num_words = text.split()
    return len(num_words)

def get_num_charecters(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
def sort_on(dict) -> int:
    return dict["num"]        

def get_sorted_dict(char_dict:dict) -> dict:
    char_list = []
    for key, value in char_dict.items():
        single_dict = {}
        single_dict["char"] = key
        single_dict["num"] = value
        char_list.append(single_dict)
       
    char_list.sort(reverse=True, key=sort_on) 
    return char_list



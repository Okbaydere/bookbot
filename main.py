def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    words = get_text_length(text)
    char_counts = text_char_counter(text)
    
    # Print the formatted report
    print(f"--- Begin report of {book_path} ---")
    print(f"{words} words found in the document")
    print("")
    
    for char, count in char_counts:
        print(f"The '{char}' character was found {count} times")
    
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_text_length(text):
    text = text.split()
    return len(text)


def text_char_counter(text):    
    text = text.lower()
    text = only_alphabet(text)
    char_count_dict = {}
    for char in text:
        if char in char_count_dict:
            char_count_dict[char] +=1
        else:
            char_count_dict[char] = 1
    sorted_text= sorted(char_count_dict.items(),key=lambda item: item[1],reverse=True)
    return sorted_text

def only_alphabet(text):
    char_only = ""
    for char in text:
        if char.isalpha() == True:
            char_only += char
        else:
            continue
    return char_only

            
main()


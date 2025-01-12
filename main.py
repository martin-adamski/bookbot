def main():
    
    file_path = "books/frankenstein.txt" 
    text = get_book(file_path)
    num_words = get_num_words(text)
    
    print (f"--- Begin report of {file_path} ---")
    print(f"{num_words} words were found in the document")
    printCharacterReport(get_chars_dict(text))
    print("--- End report ---")
    
    
def get_book(book):
    with open(book) as f:
        return f.read()
        
def get_num_words(text):
    text = text.split()        
    return len(text)

def get_chars_dict(text: str):
    
    # Model Solution
    
    # chars = {}
    # for c in text:
    #     lowered = c.lower()
    #     if lowered in chars:
    #         chars[lowered] += 1
    #     else:
    #         chars[lowered] = 1
    # return chars
    
    # My Solution
    
    text = text.lower()
    dict = {}
    
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    
    for a_letter in alphabet:
        sum = 0
        for t_letter in text:
            if a_letter == t_letter:
               sum += 1
        dict[a_letter] = sum
    return dict 

def printCharacterReport(char_dict: dict):
    for key, value in char_dict.items():
        print(f"The character '{key}' was found {value} times")
     
        
main()
def get_num_words(file_string):
    return len(file_string.split())

def char_count(file_string):
    dictionary = {}

    for char in file_string.lower():
        if char in dictionary.keys():
            dictionary[char] += 1
        else:
            dictionary[char] = 1

    return dictionary

def sorted_dictionary(dicts):
    dict_list = []

    for key, value in dicts.items():
        small_dict = {}
        small_dict["char"] = key
        small_dict["num"] = value
        dict_list.append(small_dict)

    def sort_on(items):
        return items["num"]

    dict_list.sort(reverse = True, key = sort_on)

    return dict_list

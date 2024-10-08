def index_of(word, list):
    i = 0
    while i < len(list):
        if word == list[i]:
            return i
        i += 1
    return -1





def index_of_by_index(word, list, index):
    i = 0
    new_list = list[index:]
    while i < len(new_list):
        actual_word = new_list[i]
        if actual_word == word:
            return i + index
        i += 1  
    return -1


def index_of_empty(list):
    i = 0
    while i < len(list):
        actual_element = list[i]
        if actual_element == "":
            return i
        i += 1
    return -1


def put(word, list):
    i = 0
    for elemento in list:
        if elemento == "":
            list[i] = word
            return i
        i += 1
    return -1


def remove(word, list):
    elim = 0
    for indice in range(len(list)):
        if list[indice] == word:
            list[indice] = ""
            elim += 1
    return elim

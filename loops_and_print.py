def enumerate_list(list):
    new_list = []
    i = 0
    for current_element in list:
        if current_element != "":
            nuevo_elemento = f"{i}. {current_element}"
            new_list.append(nuevo_elemento)
            i += 1

    return new_list


def enumerate_backwards(list):
    new_list = []
    i = 0
    for current_element in list:
        if current_element != "":
            atras = current_element[ : :-1]
            nuevo_elemento = f"{i}. {atras}"
            new_list.append(nuevo_elemento)
            i += 1

    return new_list

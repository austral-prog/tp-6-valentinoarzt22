def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements) >= 6:
        del list_to_remove_elements[5]
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif len(list_to_remove_elements) >= 5:
        del list_to_remove_elements[4]
        del list_to_remove_elements[0]
    elif len(list_to_remove_elements) >= 1:
        del list_to_remove_elements[0]
    return list_to_remove_elements

def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0, 'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements

def is_empty(list_to_check):
    return len(list_to_check) == 0

def check_lists(list_to_compare1, list_to_compare2):
    if len(list_to_compare1) >= 3 and len(list_to_compare2) >= 3:
        return list_to_compare1[2] == list_to_compare2[2]
    else:
        return False

def list_of_lists(lists_of_lists_to_modify):
    if len(lists_of_lists_to_modify) >= 1:
        lists_of_lists_to_modify[0] = lists_of_lists_to_modify[0][:2]  # primeros 2 elementos
    if len(lists_of_lists_to_modify) >= 2:
        lists_of_lists_to_modify[1] = lists_of_lists_to_modify[1][1:4]  # del 2° al 4° elemento
    if len(lists_of_lists_to_modify) >= 3:
        lists_of_lists_to_modify[2] = lists_of_lists_to_modify[2][-2:]  # últimos 2 elementos
    
    return lists_of_lists_to_modify

def create_an_empty_list():
    List = list()
    return List

def create_a_list():
    List = [1, 2, 3, 4]
    return List

def add_element_to_end_of_list(l, element):
    List = list()
    List.append(element)
    return List

def add_element_to_start_of_list(l, element):
    List = [1,2,3,4]
    List.insert(0, element)
    return List

def remove_element_from_end_of_list(l):
    List = [1,2,3,4]
    List.pop()
    return List

def remove_element_from_start_of_list(l):
    List = [1,2,3,4]
    List.pop(0)
    return List

def retrieve_first_element_from_list(l):
    List = [1,2,3,4]
    return List[0]

def retrieve_element_from_index(l, index):
    List = [1,2,3,4]
    return List[index]

def retrieve_last_element_from_list(l):
    List = [1,2,3,4]
    return List[-1]

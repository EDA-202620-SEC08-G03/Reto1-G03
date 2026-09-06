def new_list():
    newlist = {
        "first": None,

        "size": 0,
        "last": None
    } 
    return newlist

  
def get_element(my_list, pos):
    searchpos = 0
    node = my_list["first"]
    while searchpos < pos:
        node = node["next"]
        searchpos += 1
    return node["info"]

def is_present(my_list, element, cmp_function):
    is_in_array = False
    temp = my_list["first"]

    count = 0 
    while not is_in_array and temp is not None:
        if cmp_function(element, temp["info"]) == 0:
            is_in_array = True
        else:
            temp = temp["next"]
            count += 1 
    if not is_in_array:
        count = -1
    return count 

def add_first(my_list, element):
    
    new_node = {'info': element, 'next':None}
    if my_list['first'] is None:
        my_list['first'] = new_node
        my_list['last'] = new_node
    else:
        new_node['next'] = my_list['first']
        my_list['first'] = new_node
    my_list['size'] += 1
    return my_list

def add_last (my_list, element):
    new_node = {'info': element, 'next': None}
    if my_list["first"] is None:
        my_list["first"] = new_node
        my_list["last"]= new_node
    else:
        my_list["last"]["next"]= new_node   
        my_list["last"] = new_node
    my_list["size"] += 1
    return my_list

def size(my_list):
    return my_list["size"]

    
def first_element(my_list):
    size= my_list["size"]
    if size <0:
        return None
    else:
        primero= my_list["first"]
    return my_list["first"]["info"]
    


def is_empty(my_list):
    return my_list["size"] == 0
def size(my_list):
    return my_list["size"]
def last_element(my_list):
    if is_empty(my_list):
        raise Exception("indexError: list index out of range")
    return my_list["last"]["info"]
def delete_element(my_list, pos):
    if pos < 0 or pos >= my_list["size"]:
        raise Exception('IndexError: list index out of range')
    if pos == 0:
        my_list["first"] = my_list["first"]["next"]
        if my_list["size"] == 1:
            my_list["last"] = None
    else:
        prev = my_list["first"]
        for _ in range(pos - 1):
            prev = prev["next"]
        node_to_delete = prev["next"]
        prev["next"] = node_to_delete["next"]
        if node_to_delete == my_list["last"]:
            my_list["last"] = prev
    my_list["size"] -= 1
    return my_list

def remove_first(my_list):
    if is_empty(my_list):
        raise Exception("indexError: list index out of range")
    element = my_list["first"]["info"]
    my_list["first"] = my_list["first"]["next"]
    my_list["size"] -= -1
    if my_list["size"] == 0:
        my_list["last"] = None
    return element 

def remove_last(my_list):
    if is_empty(my_list):
            raise Exception("indexError: list index out of range")
    element = my_list["last"]["info"]
    if my_list["size"] == 1:
        my_list["first"] = None
        my_list["last"] = None
    else:
        node = my_list["first"]
        while node["next"] != my_list["last"]:
            node = node["next"]
        node["next"] = None
        my_list["last"] = node
    my_list["size"] -= 1
    return element
    
    
def insert_element(my_list, element, pos):
    if pos < 0 or pos > my_list["size"]:
        raise Exception("indexError: list index out of range")
    if pos == 0:
        return add_first(my_list, element)
    elif pos == my_list["size"]:
        return add_last(my_list, element)
    else:
        new_node = {"info": element, "next": None}
        prev = my_list["first"]
        for _ in range(pos - 1):
            prev = prev["next"]
        new_node["next"] = prev["next"]
        prev["next"] = new_node
        my_list["size"] += 1
        return my_list


def change_info(my_list, pos, new_info):
    
    if pos < 0 or pos >= my_list["size"]:
        raise Exception("indexError: list index out of range")
    node = my_list["first"]
    for i in range(pos):
        node = node["next"]
    node["info"] = new_info
    return my_list

def exchange(my_list, pos1, pos2):
    if pos1 < 0 or pos1 >= my_list["size"] or pos2 < 0 or pos2 >= my_list["size"]:
        raise Exception("indexError: list index out of range")
    node_1 = my_list["first"]
    for _ in range(pos1):
        node_1 = node_1["next"]

    node_2 = my_list["first"]
    for _ in range(pos2):
        node_2 = node_2["next"]

    node_1["info"], node_2["info"] = node_2["info"], node_1["info"]
    return my_list

def sub_list(my_list, pos, num_elements):
    if pos < 0 or pos >= my_list["size"]:
        raise Exception('IndexError: list index out of range')

    new_l = new_list()
    node = my_list["first"]
    for _ in range(pos):
        node = node["next"]

    for _ in range(num_elements):
        if node is None:
            break
        new_l = add_last(new_l, node["info"])
        node = node["next"]

    return new_l

"""sinl"""


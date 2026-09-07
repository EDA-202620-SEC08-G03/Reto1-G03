from DataStructures.List import single_linked_list as sll
def new_stack():
    stack = sll.new_list()
    return stack
def push(my_stack,element):
    sll.add_last(my_stack,element)
    return my_stack
def pop(my_stack):
    if is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty')
    primer_elemento = sll.get_element(my_stack, sll.size(my_stack) - 1)
    sll.delete_element(my_stack,sll.size(my_stack)-1)
    return primer_elemento
def size(my_stack):
    return sll.size(my_stack)
def is_empty(my_stack):
    return sll.is_empty(my_stack)
    
def top(my_stack):
    if is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty')
    primer = sll.get_element(my_stack, sll.size(my_stack) -1)
    return primer
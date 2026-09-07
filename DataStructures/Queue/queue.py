from DataStructures.List import array_list as array

def new_queue():
    queue = array.new_list()
    return queue

def enqueue(queue,element):
    array.add_last(queue,element)
    return queue

def peek (my_queue):
    
    if my_queue["size"] == 0:
        raise Exception('EmptyStructureError: queue is empty')
    
    primer = array.get_element(my_queue, 0)
    return primer


def size (my_queue):
    
    return array.size(my_queue)

def dequeue(my_queue):
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    x = array.get_element(my_queue,0)
    array.delete_element(my_queue,0)
    return x

def is_empty(my_queue):
    y = array.is_empty(my_queue)
    return y

from DataStructures.List import single_linked_list as st

def new_queue():
    new = st.new_list()
    return new 

def enqueue (my_queue, element):
    st.add_last(my_queue["elements"], element)
    return my_queue

def dequeue(my_queue):
    if is_empty(my_queue):
        raise Exception('EmptyStructureError: queue is empty')
    st.remove_first(my_queue)
    return my_queue
    
    
def is_empty(my_queue):
    if my_queue["size"] == 0:
        return True
    else: 
        return False  
    
    
def peek(new):
    if st.is_empty(new):
        raise Exception('EmptyStructureError: queue is empty')
    else:
        return st.get_element(new,0)
    
def size(new):
    return st.size(new)
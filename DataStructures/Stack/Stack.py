
from DataStructures.List import single_linked_list as st

def new_stack():
    new = st.new_list()
    return new

def push(my_stack, element):
     st.add_last(my_stack, element)
     return my_stack
 
 
def pop( my_stack):
    if st.is_empty(my_stack):
        raise Exception('EmptyStructureError: stack is empty')
    
    return st.remove_last(my_stack)
    
     
def is_empty(my_stack):
    if st.is_empty(my_stack):
        return True
    else:
        return False
def top(my_stack):
   if st.is_empty(my_stack):
       raise Exception('EmptyStructureError: stack is empty')
   else:
         return st.last_element(my_stack)
     
def size(my_stack):
    l = st.size(my_stack)
    return l


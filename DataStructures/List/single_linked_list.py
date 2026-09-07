def new_list():
    newlist={
        "first":None,"last":None,"size":0,
    }
    return newlist
def add_first(lista,element):
    new={
        "info":element,"next":lista["first"]
    }
    lista["first"]=new
    if lista["size"]==0:
        lista["last"]=new
    lista["size"]+=1
    return lista
def add_last(lista,element):
    new={
        "info":element,"next":None
    }
    if lista["size"]==0:
        lista["first"]=new
    else:
        lista["last"]["next"]=new
    lista["size"]+=1
    lista["last"]=new
    return lista
def size(lista):
    return lista["size"]
def first_element(lista):
    if is_empty(lista):
      raise Exception('IndexError: list index out of range')
    return lista["first"]["info"]
def is_empty(lista):
    if lista["size"]==0:
        return True
    return False
def last_element(lista):
    if is_empty(lista):
      raise Exception('IndexError: list index out of range')
    return lista["last"]["info"]
def delete_element(lista,pos):
    if pos < 0 or pos >= size(lista):
        raise Exception('IndexError: list index out of range')
    if pos ==0:
        
        borrado=lista["first"]
        lista["first"]=lista["first"]["next"]
        lista["size"]-=1
        if lista["size"]==0:
            lista["last"]=None
    
    else:
        actual=lista["first"]
        i=0
        while i<pos-1:
            actual=actual["next"]
            i+=1
        borrado=actual["next"]
        actual["next"]=borrado["next"]
        if pos == lista["size"]-1:
            lista["last"]=actual
        lista["size"]-=1
    return lista
def remove_first(lista):
    if is_empty(lista):
        raise Exception("IndexError: list index out of range")
    
    borrado=lista["first"]
    lista["first"]=lista["first"]["next"]
    if lista ["first"] is None:
        lista["last"]=None
    lista["size"]-=1
    return borrado["info"]
def remove_last(lista):
    if is_empty(lista):
        raise Exception("IndexError: list index out of range")
    borrado=lista["last"]
    if lista["size"]==1:
        lista["first"]=None
        lista["last"]=None
    else:
        actual=lista["first"]
        while actual["next"] != lista["last"]:
            actual=actual["next"]
        
        actual["next"]=None
        lista["last"]=actual
    lista["size"]-=1
    return borrado["info"]
def insert_element(lista,elemento,pos):
    if pos < 0 or pos > size(lista):
        raise Exception('IndexError: list index out of range')
    else:
        new={
            "info":elemento,
            "next":None
        }
        if pos==0:
            new["next"]=lista["first"]
            lista["first"]=new
            if lista["size"]==0:
                lista["last"] = new
        else:
            i=0
            actual=lista["first"]
            while i<pos-1:
                actual=actual["next"]
                i+=1
            new["next"]=actual["next"]
            actual["next"]=new
            if pos ==lista["size"]:
                lista["last"]=new
    lista["size"]+=1

    return lista
def change_info(lista,pos,nueva_info):
    if pos <0 or pos >=lista["size"]:

        raise Exception ("IndexError: list index out of range")

    anterior=lista["first"]
    i=0
    while i<pos:
        anterior=anterior["next"]
        i+=1
    anterior["info"]=nueva_info
    return lista
def exchange(lista,pos1,pos2):
    if pos1<0 or pos2<0 or pos1>=lista["size"] or pos2>=lista["size"]:
        raise Exception("IndexError. list index out of range")
    i=0
    elemento1=lista["first"]
    while i<pos1:
        elemento1=elemento1["next"]
        i+=1
    j=0
    elemento2=lista["first"]
    while j<pos2:
        elemento2=elemento2["next"]
        j+=1
    cambio=elemento1

    elemento1["info"]=elemento2["info"]
    elemento2["info"]=cambio["info"]
    
    return lista
def sub_list(lista,pos,num_elements):
    if pos<0 or pos>=lista["size"] or num_elements>lista["size"]-pos:
        raise Exception ("IndexError:list index out of range")
    primero_sub=lista["first"]
    for i in range(pos):
        primero_sub=primero_sub["next"]
    
    if num_elements==0:
        sublista=new_list()
        
    else:
        sublista=new_list()
    
        elemento_sub=primero_sub
        for i in range(num_elements):
            
            add_last(sublista,elemento_sub["info"])
            elemento_sub=elemento_sub["next"]    
        
    return sublista        
def get_element(lista,pos):
    searchpos=0
    node=lista["first"]
    while searchpos<pos:
        node=node["next"]
        searchpos+=1
    return node["info"]
def is_present(lista,elemento,cmp_function):
    is_in_array=False
    temp=lista["first"]
    count=0
    while not is_in_array and temp is not None:
        if cmp_function(elemento,temp["info"])==0:
            is_in_array=True
        else:
            temp=temp["next"]
            count+=1
    if not is_in_array:
        count= -1
    return count


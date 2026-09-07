import time
import csv
import os

from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q 
from DataStructures.Stack import stack as st
from DataStructures.List import single_linked_list as sll
def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {
        "orders": lt.newList()
    }
    return catalog
    


# Funciones para la carga de datos

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    # TODO: Realizar la carga de datos
    pass

# Funciones de consulta sobre el catálogo


def req_1(catalog):
    """
    Retorna el resultado del requerimiento 1
    """
    # TODO: Modificar el requerimiento 1
    pass


def req_2(catalog, min_price, max_price):
    """
    Retorna el resultado del requerimiento 2
    """
    start=get_time()
    orders = catalog['orders']
    lista_filtrada = lt.newlist()
    for i in range(lt.size(orders)):
        actual = lt.getelement(orders, i)
        if min_price <= float(actual['Price_per_Box']) <= max_price:
            lt.addlast(lista_filtrada, actual)
    if lt.size(lista_filtrada) > 0:
        descuento_total = 0
        marketing_total = 0
        precio_total = 0
        for i in range(lt.size(lista_filtrada)):
            actual = lt.get_element(lista_filtrada, i)
            descuento_total += float(actual["Discount_Pct"])
            marketing_total += float(actual["Marketing_Spend"])
            precio_total += float(actual["Price_per_Box"])
        pmd_descuento = descuento_total / lt.size(lista_filtrada)
        pmd_marketing = marketing_total / lt.size(lista_filtrada)
        pmd_precio = precio_total / lt.size(lista_filtrada)
        recent = lt.get_element(lista_filtrada, 0)
        for i in range(1,lt.size(lista_filtrada)):
            actual = lt.get_element(lista_filtrada, i)
            if actual["Order_Date"] > recent["Order_Date"]:
                recent = actual
            elif actual["Order_Date"] == recent["Order_Date"]:
                if float(actual["Amount"]) > float(recent["Amount"])    :
                    recent = actual
        min_order = lt.get_element(lista_filtrada, 0)
        max_order = lt.get_element(lista_filtrada, 0)
        for i in range(1,lt.size(lista_filtrada)):
            actual = lt.get_element(lista_filtrada, i)
            if float(actual["Amount"]) < float(min_order["Amount"]) or (
            float(actual["Amount"]) == float(min_order["Amount"]) and float(actual["Price_per_Box"]) < float(min_order["Price_per_Box"])
            ):
                min_order = actual
            if float(actual["Amount"]) > float(max_order["Amount"]) or (float(actual["Amount"]) == float(max_order["Amount"]) and float(actual["Price_per_Box"]) < float(max_order["Price_per_Box"])
            ):
                max_order = actual
    end=get_time()
    elapsed = delta_time(start, end)
    return {"elapsed_time": elapsed,
            "pmd_descuento": pmd_descuento,
            "pmd_marketing": pmd_marketing,
            "pmd_precio": pmd_precio,
            "recent_order": recent,
            "min_order": min_order,
            "max_order": max_order}


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog):
    """
    Retorna el resultado del requerimiento 4
    """
    # TODO: Modificar el requerimiento 4
    pass


def req_5(catalog):
    """
    Retorna el resultado del requerimiento 5
    """
    # TODO: Modificar el requerimiento 5
    pass

def req_6(catalog):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

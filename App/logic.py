import time
import csv
import os

from DataStructures.List import array_list as lt
from DataStructures.Queue import queue as q 
from DataStructures.Stack import stack as st
from DataStructures.List import single_linked_list as sll

csv.field_size_limit(2147483647)
data_dir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..', 'Data')

def new_logic():
    """
    Crea el catalogo para almacenar las estructuras de datos
    """
    catalog = {

        'sales': None,
        'sales_sublist': None
    }
    
    
    catalog['sales'] = lt.new_list()
    catalog['sales_sublist'] = lt.new_list()
    return catalog


# Funciones para la carga de datos

def extrañer_año (fecha):
    
    if not fecha or fecha == 'Unknown':
        resultado = 'Unknown'
    if '-' in fecha:
        resultado = fecha.split('-')
    elif '/' in fecha:
        resultado = fecha.split('/')[-1]
    else:
        resultado = 'Unknown'
    return resultado

def load_data(catalog, filename):
    """
    Carga los datos del reto
    """
    
    filepath = os.path.join(data_dir, filename)

    start_time = get_time()
    
    total_registros = 0
    min_order = None
    max_order = None

    # Apertura y lectura en una única pasada de disco
    with open(filepath, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for fila in reader:
            orden = {
                'Order_ID': fila.get('Order_ID') or 'Unknown',
                'Product': fila.get('Product') or 'Unknown',
                'Country': fila.get('Country') or 'Unknown',
                'Channel': fila.get('Channel') or 'Unknown',
                'Order_Date': fila.get('Order_Date') or 'Unknown',
                'Discount_Pct': float(fila['Discount_Pct']) if fila.get('Discount_Pct') else 0.0,
                'Price_per_Box': float(fila['Price_per_Box']) if fila.get('Price_per_Box') else 0.0,
                'Marketing_Spend': float(fila['Marketing_Spend']) if fila.get('Marketing_Spend') else 0.0,
                'Boxes_Shipped': int(fila['Boxes_Shipped']) if fila.get('Boxes_Shipped') else 0,
                'Amount': float(fila['Amount']) if fila.get('Amount') else 0.0
            }
            
            lt.add_last(catalog['sales'], orden)
            total_records += 1

            if min_order is None:
                min_order = orden
            elif orden['Amount'] < min_order['Amount']:
                min_order = orden
            elif orden['Amount'] == min_order['Amount']:
                if orden['Price_per_Box'] < min_order['Price_per_Box']:
                    min_order = orden

            if max_order is None:
                max_order = orden
            elif orden['Amount'] > max_order['Amount']:
                max_order = orden
            elif orden['Amount'] == max_order['Amount']:
                if orden['Price_per_Box'] < max_order['Price_per_Box']:
                    max_order = orden

    end_time = get_time()
    tiempo_ms = delta_time(start_time, end_time)

    return {
        'tiempo_transcurrido_ms': tiempo_ms,
        'registros_totales': total_registros,
        'orden_minima': min_order,
        'orden_maxima': max_order
    }

# Funciones de consulta sobre el catálogo

def req_1(catalog, producto):
    """
    Retorna el resultado del requerimiento 1
    """

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

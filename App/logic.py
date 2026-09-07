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
  
    start_time = get_time()
    
    sales_lista = catalog['sales']
    tamaño = lt.size(sales_lista)
    
    catalog['sales_sublist'] = lt.new_list()
    
    total_filtrados = 0
    sum_price = 0.0
    sum_discount = 0.0
    sum_boxes = 0.0
    sum_marketing = 0.0
    
    min_price, max_price = float('inf'), float('-inf')
    min_discount, max_discount = float('inf'), float('-inf')
    min_boxes, max_boxes = float('inf'), float('-inf')
    min_mkt, max_mkt = float('inf'), float('-inf')
    
    years_count = {}
    
    orden_mayorcosto = None
    orden_menorcosto = None
    
    for i in range(tamaño):
        order = lt.get_element(sales_lista, i)
        
        if order['Product'].strip().lower() == producto.strip().lower():
            
            lt.add_last(catalog['sales_sublist'], order)
            total_filtrados += 1
            
            price = order['Price_per_Box']
            discount = order['Discount_Pct']
            boxes = order['Boxes_Shipped']
            mkt = order['Marketing_Spend']
            amount = order['Amount']
            
            sum_price += price
            if price < min_price: min_price = price
            if price > max_price: max_price = price
            
            sum_discount += discount
            if discount < min_discount: min_discount = discount
            if discount > max_discount: max_discount = discount
            
            sum_boxes += boxes
            if boxes < min_boxes: min_boxes = boxes
            if boxes > max_boxes: max_boxes = boxes
            
            sum_mkt += mkt
            if mkt < min_mkt: min_mkt = mkt
            if mkt > max_mkt: max_mkt = mkt
            
            year = extrañer_año(order['Order_Date'])
            if year != 'Unknown':
                years_count[year] = years_count.get(year, 0) + 1
            
            if orden_mayorcosto is None:
                orden_mayorcosto = order
            elif amount > orden_mayorcosto['Amount']:
                orden_mayorcosto = order
            elif amount == orden_mayorcosto['Amount']:
                if mkt < orden_mayorcosto['Marketing_Spend']:
                    orden_mayorcosto = order
                    
            if orden_menorcosto is None:
                orden_menorcosto = order
            elif amount < orden_menorcosto['Amount']:
                orden_menorcosto = order
            elif amount == orden_menorcosto['Amount']:
                if mkt < orden_menorcosto['Marketing_Spend']:
                    orden_menorcosto = order

    end_time = get_time()
    elapsed_time = delta_time(start_time, end_time)
    
    if total_filtrados == 0:
        return {
            'tiempo_ejecucion_ms': elapsed_time,
            'total_pedidos': 0
        }
        
    prom_costo = sum_price / total_filtrados
    prom_descuento = sum_discount / total_filtrados
    prom_boxes = sum_boxes / total_filtrados
    prom_marketing = sum_marketing / total_filtrados
    
    best_year = "Unknown"
    if years_count:
        best_year = max(years_count, key=years_count.get)
        
    dic_res = {
        'tiempo_ejecucion_ms': elapsed_time,
        'total_pedidos': total_filtrados,
        'promedio_precio': prom_costo,
        'precio_minimo': min_price,
        'precio_maximo': max_price,
        'promedio_descuento': prom_descuento,
        'descuento_minimo': min_discount,
        'descuento_maximo': max_discount,
        'promedio_cajas': prom_boxes,
        'cajas_minimo': min_boxes,
        'cajas_maximo': max_boxes,
        'promedio_marketing': prom_marketing,
        'marketing_minimo': min_mkt,
        'marketing_maximo': max_mkt,
        'año_mas_pedidos': best_year,
        'pedido_mayor_monto': orden_mayorcosto,
        'pedido_menor_monto': orden_menorcosto
    }
    
    return dic_res

def req_2(catalog, min_price, max_price):
    """
    Retorna el resultado del requerimiento 2
    """
    start=get_time()
    orders = catalog['sales']
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

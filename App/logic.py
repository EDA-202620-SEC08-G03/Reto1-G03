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
    lista_filtrada = lt.new_list()
    for i in range(lt.size(orders)):
        actual = lt.get_element(orders, i)
        if min_price <= float(actual['Price_per_Box']) <= max_price:
            lt.add_last(lista_filtrada, actual)
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
            if float(actual["Order_Date"]) > float(recent["Order_Date"]):
                recent = actual
            elif float(actual["Order_Date"]) == float(recent["Order_Date"]):
                if float(actual["Amount"]) > float(recent["Amount"]):
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
    dicreciente={"Producto": recent["Product"], "Pais": recent["Country"], "Canal": recent["Channel"], "Fecha": recent["Order_Date"], "Amount": recent["Amount"],"Price_per_box": recent["Price_per_Box"]}
    dicminimo={"Producto": min_order["Product"], "Pais": min_order["Country"], "Canal": min_order["Channel"], "Fecha": min_order["Order_Date"], "Amount": min_order["Amount"],"Price_per_box": min_order["Price_per_Box"]}
    dicmaximo={"Producto": max_order["Product"], "Pais": max_order["Country"], "Canal": max_order["Channel"], "Fecha": max_order["Order_Date"], "Amount": max_order["Amount"],"Price_per_box": max_order["Price_per_Box"]}
    end=get_time()
    elapsed = delta_time(start, end)
    return {"Elapsed_time": elapsed,
            "Pmd_descuento": pmd_descuento,
            "Pmd_marketing": pmd_marketing,
            "Pmd_precio": pmd_precio,
            "Recent_order": dicreciente,
            "Min_order": dicminimo,
            "Max_order": dicmaximo, 
            "total_orders": lt.size(lista_filtrada)}


def req_3(catalog):
    """
    Retorna el resultado del requerimiento 3
    """
    # TODO: Modificar el requerimiento 3
    pass


def req_4(catalog,product, country):
    """
    Retorna el resultado del requerimiento 4
    """
    start= get_time()
    orders = catalog['sales']
    lista_filtrada = lt.new_list()
    suma_price_per_box = 0
    suma_discount_pct = 0
    suma_marketing_spend = 0
    suma_boxes_shipped = 0
    for i in range(lt.size(orders)):
        actual = lt.get_element(orders, i)
        if actual["Product"].lower() == product.lower() and actual["Country"].lower() == country.lower():
            lt.add_last(lista_filtrada, actual)
    n = lt.size(lista_filtrada)
    if n == 0:
        return {"elapsed_time": delta_time(start, get_time()), "message": "No hay pedidos que cumplan el filtro"}
    max1 = lt.get_element(lista_filtrada, 0)
    max2 = lt.get_element(lista_filtrada, 0)
    suma_price_per_box = float(max1["Price_per_Box"])
    suma_discount_pct = float(max1["Discount_Pct"])
    suma_marketing_spend = float(max1["Marketing_Spend"])
    suma_boxes_shipped = float(max1["Boxes_Shipped"])
    for i in range(1, lt.size(lista_filtrada)):
        actual = lt.get_element(lista_filtrada, i)
        suma_price_per_box += float(actual["Price_per_Box"])
        suma_discount_pct += float(actual["Discount_Pct"])
        suma_marketing_spend += float(actual["Marketing_Spend"])
        suma_boxes_shipped += float(actual["Boxes_Shipped"])
        if float(actual["Amount"]) > float(max1["Amount"]):
            max2 = max1
            max1 = actual
        elif float(actual["Amount"]) == float(max1["Amount"]):
            if float(actual["marketing_spend"]) < float(max1["marketing_spend"]):
                max2 = max1
                max1 = actual
            elif float(actual["marketing_spend"]) == float(max1["marketing_spend"]):
                if float(actual["order_id"]) < float(max1["order_id"]):
                    max2 = max1
                    max1 = actual
        elif float(actual["Amount"]) > float(max2["Amount"]):
            max2 = actual
        elif float(actual["Amount"]) == float(max2["Amount"]):
                if float(actual["marketing_spend"]) < float(max2["marketing_spend"]):
                    max2 = actual
                elif float(actual["marketing_spend"]) == float(max2["marketing_spend"]):
                    if float(actual["order_id"]) < float(max2["order_id"]):
                        max2 = actual
    pmd_price_per_box = suma_price_per_box / lt.size(lista_filtrada)
    pmd_discount_pct = suma_discount_pct / lt.size(lista_filtrada)
    pmd_marketing_spend = suma_marketing_spend / lt.size(lista_filtrada)
    pmd_boxes_shipped = suma_boxes_shipped / lt.size(lista_filtrada)
    dict1={ "Order_ID": max1["Order_ID"],"  Canal": max1["Channel"],"Fecha": max1["Order_Date"],"Cajas enviadas": max1["Boxes_Shipped"],"Monto": max1["Amount"] }
    dict2={ "Order_ID": max2["Order_ID"],"  Canal": max2["Channel"],"Fecha": max2["Order_Date"],"Cajas enviadas": max2["Boxes_Shipped"],"Monto": max2["Amount"] }
    end= get_time()
    elapsed= delta_time(start, end)
    
    return {"Elapsed_time": elapsed,
            "Pmd_price_per_box": pmd_price_per_box,
            "Pmd_discount_pct": pmd_discount_pct,
            "Pmd_marketing_spend": pmd_marketing_spend,
            "Pmd_boxes_shipped": pmd_boxes_shipped,
            "Max1": dict1,
            "Max2": dict2,
            "total_orders": lt.size(lista_filtrada)} 


def req_5(catalog,filtro, producto,fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 5
    """
    start= get_time()
    orders = catalog['sales']   
    lista_filtrada = lt.new_list()
    for i in range(lt.size(orders)):
        actual = lt.get_element(orders, i)
        if (actual["Product"].lower() == producto.lower()) and (fecha_inicial <= order_date <= fecha_final):
                lt.add_last(lista_filtrada, actual)
    if lt.size(lista_filtrada) == 0:
        return {
        "Tiempo_ejecucion_ms": delta_time(start, get_time()),
        "Total_pedidos": 0,
        "Mensaje": "No se encontraron pedidos en el rango de fechas"
    }
     
    suma_price_per_box = 0
    suma_boxes_shipped = 0
    suma_marketing_spend = 0
    actual = lt.get_element(lista_filtrada, 0)
    respuesta = actual
    for i in range(lt.size(lista_filtrada)):
        actual = lt.get_element(lista_filtrada, i)
        
        suma_price_per_box += float(actual["Price_per_Box"])
        suma_boxes_shipped += float(actual["Boxes_Shipped"])
        suma_marketing_spend += float(actual["Marketing_Spend"])
        if filtro == "MAYOR":
            
            if float(actual["Amount"]) > float(respuesta["Amount"]):
                respuesta = actual
            elif (float(actual["Amount"]) == float(respuesta["Amount"])):
                if float(actual["Price_per_Box"]) < float(respuesta["Price_per_Box"]):
                    respuesta = actual
                elif (float(actual["Price_per_Box"]) == float(respuesta["Price_per_Box"])):
                    if float(actual["Marketing_Spend"]) < float(respuesta["Marketing_Spend"]):
                        respuesta = actual
        elif filtro == "MENOR":
            
            if float(actual["Amount"]) < float(respuesta["Amount"]):
                respuesta = actual
            elif (float(actual["Amount"]) == float(respuesta["Amount"])):
                if float(actual["Price_per_Box"]) < float(respuesta["Price_per_Box"]):
                    respuesta = actual
                elif (float(actual["Price_per_Box"]) == float(respuesta["Price_per_Box"])):
                    if float(actual["Marketing_Spend"]) < float(respuesta["Marketing_Spend"]):
                        respuesta = actual
    pmd_price_per_box = suma_price_per_box / lt.size(lista_filtrada)
    pmd_boxes_shipped = suma_boxes_shipped / lt.size(lista_filtrada)
    pmd_marketing_spend = suma_marketing_spend / lt.size(lista_filtrada)
    dic_respuesta={"Price_per_box": respuesta["Price_per_Box"], "Cajas_enviadas": respuesta["Boxes_Shipped"], "Canal": respuesta["Channel"], "Fecha": respuesta["Order_Date"], "Monto": respuesta["Amount"],"Marketing_Spend": respuesta["Marketing_Spend"]}
    end= get_time()
    elapsed= delta_time(start, end)
    return {"Elapsed_time": elapsed,
            "Filtro": filtro,
            "Pmd_price_per_box": pmd_price_per_box,
            "Pmd_marketing_spend": pmd_marketing_spend,
            "Pmd_boxes_shipped": pmd_boxes_shipped,
            "Total_orders": lt.size(lista_filtrada),
            "respuesta": dic_respuesta 
            }

def req_6(catalog,fecha_inicial, fecha_final):
    """
    Retorna el resultado del requerimiento 6
    """
    start= get_time()
    orders = catalog['sales']
    canales = {}
    lista_filtrada = lt.new_list()
    for i in range(lt.size(orders)):
        actual = lt.get_element(orders, i)
        order_date = actual["Order_Date"]
        
        
        if fecha_inicial <= order_date <= fecha_final:
            lt.add_last(lista_filtrada, actual)
            
            if actual["Channel"] not in canales:
                canales[actual["Channel"]] = {"total_amount": 0, "total_price_per_box": 0, "total_marketing_spend": 0, "max_order": None, "min_order": None, "total_orders": 0}
            canales[actual["Channel"]]["total_amount"] += float(actual["Amount"])
            canales[actual["Channel"]]["total_price_per_box"] += float(actual["Price_per_Box"])
            canales[actual["Channel"]]["total_marketing_spend"] += float(actual["Marketing_Spend"])
            canales[actual["Channel"]]["total_orders"] += 1
            if canales[actual["Channel"]]["max_order"] is None or float(actual["Amount"]) > float(canales[actual["Channel"]]["max_order"]["Amount"]):
                canales[actual["Channel"]]["max_order"] = actual
            if canales[actual["Channel"]]["min_order"] is None or float(actual["Amount"]) < float(canales[actual["Channel"]]["min_order"]["Amount"]):
                canales[actual["Channel"]]["min_order"] = actual
            
    canal_mas_usado= None
    max_pedidos = 0
    canal_mayor_amount = None
    max_amount = 0   
    
    for ch, datos in  canales.items():
        if datos["total_orders"] > max_pedidos:
            max_pedidos = datos["total_orders"]
            canal_mas_usado = ch
        if datos["total_amount"] > max_amount:
            max_amount = datos["total_amount"]
            canal_mayor_amount = ch
    reporte_canales = {}
    for ch, datos in canales.items():
        max_ord = datos["max_order"]
        min_ord = datos["min_order"]
        reporte_canales[ch] = {
            "Promedio_Price_per_Box": datos["total_price_per_box"] / datos["total_orders"],
            "Promedio_Marketing_Spend": datos["total_marketing_spend"] / datos["total_orders"],
            "Pedido_mas_costoso": {
                "Order_ID": max_ord["Order_ID"],
                "Product": max_ord["Product"],
                "Country": max_ord["Country"],
                "Order_Date": max_ord["Order_Date"],
                "Boxes_Shipped": max_ord["Boxes_Shipped"],
                "Amount": float(max_ord["Amount"])
            },
            "Pedido_mas_barato": {
                "Order_ID": min_ord["Order_ID"],
                "Product": min_ord["Product"],
                "Country": min_ord["Country"],
                "Order_Date": min_ord["Order_Date"],
                "Boxes_Shipped": min_ord["Boxes_Shipped"],
                "Amount": float(min_ord["Amount"])
            }
        }
    end= get_time()
    elapsed= delta_time(start, end)
    return {
        "Tiempo_ejecucion_ms": elapsed,
        "Total_pedidos": lt.size(lista_filtrada),
        "Canal_mas_usado": {
            "Nombre": canal_mas_usado,
            "Total_pedidos": canales[canal_mas_usado]["total_orders"],
            "Total_recaudo": canales[canal_mas_usado]["total_amount"]
        },
        "Canal_mas_recauda": {
            "Nombre": canal_mayor_amount,
            "Total_pedidos": canales[canal_mayor_amount]["total_orders"],
            "Total_recaudo": canales[canal_mayor_amount]["total_amount"]
        },
        "Reporte_por_canal": reporte_canales
    }

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

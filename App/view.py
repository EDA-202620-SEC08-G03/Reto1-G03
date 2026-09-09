import sys
import App.logic as logic
from DataStructures.List import array_list as lt

archivos = {
    "1": "chocolate_sale_100_elementos.csv",
    "2": "chocolate_sale_20_ptc.csv",
    "3": "chocolate_sale_40_ptc.csv",
    "4": "chocolate_sale_60_ptc.csv",
    "5": "chocolate_sale_80_ptc.csv",
    "6": "chocolate_sale_100_ptc.csv",
}

def new_logic():
    """
        Se crea una instancia del controlador
    """
    control = logic.new_logic()
    return control

def print_menu():
    print("Bienvenido")
    print("0- Cargar información")
    print("1- Ejecutar Requerimiento 1")
    print("2- Ejecutar Requerimiento 2")
    print("3- Ejecutar Requerimiento 3")
    print("4- Ejecutar Requerimiento 4")
    print("5- Ejecutar Requerimiento 5")
    print("6- Ejecutar Requerimiento 6")
    print("7- Salir")

def load_data(control):
    """
    Carga los datos
    """
    print("\n¿Qué archivo desea cargar?\n")
    print("1- 100 elementos (pruebas rápidas)")
    print("2- 20%")
    print("3- 40%")
    print("4- 60%")
    print("5- 80%")
    print("6- 100% (Definitivo)")
    opcion = input("Seleccione una opción: ")
    filename = archivos.get(opcion, archivos["1"])

    start_time = logic.get_time()
    logic.load_data(control, filename)
    end_time = logic.get_time()
    tiempo = logic.delta_time(start_time, end_time)

    resumen = logic.resumen_carga(control)
    print_resumen_datos(tiempo, resumen)
    
def print_resumen_datos(tiempo, resumen):
    
    print("\nTiempo de carga: {0:.2f} ms".format(tiempo))
    print("Total de pedidos cargados: {0}".format(resumen["total"]))

    print("\nPedido de menor cantidad:")
    print_pedido(resumen["menor"])

    print("\nPedido de mayor cantidad:")
    print_pedido(resumen["mayor"])

    print("\nPrimeros 5 registros:")
    for p in resumen["primeros_5"]:
        print_pedido(p)

    print("\nÚltimos 5 registros:")
    for p in resumen["ultimos_5"]:
        print_pedido(p)

def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    
    pedidos = control["ordenes"]
    total = lt.size(pedidos)
    
    encontrado = None
    i = 0
    while encontrado is None and i < total:
        actual = lt.get_element(pedidos, i)
        if actual["Order_ID"] == id:
            encontrado = actual
        i += 1

    if encontrado is not None:
        print("\nPedido encontrado:")
        print_pedido(encontrado)
    else:
        print("\nNo se encontró ningún pedido con Order_ID = {0}".format(id))

def print_pedido(p):
    print(" {0} | {1} | {2} | {3} | {4} | ${5:.2f} | ${6:.2f}".format(p["Order_ID"], p["Product"], p["Country"], p["Channel"],p["Order_Date"], p["Price_per_Box"], p["Amount"]))

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    
    producto = input("\nIngrese el nombre del producto: ")
    resultado = logic.req_1(control, producto)

    if resultado["total_orders"] == 0:
        print("\n{0}".format(resultado["Mensaje"]))
        return

    print("\nTiempo de ejecución: {0:.2f} ms".format(resultado["Elapsed_time"]))
    print("Total de pedidos: {0}".format(resultado["total_orders"]))

    print("\nPrice_per_Box -> Promedio: {0:.2f} | Min: {1:.2f} | Max: {2:.2f}".format(
        resultado["Pmd_price_per_box"], resultado["Min_price_per_box"], resultado["Max_price_per_box"]))

    print("Discount_Pct -> Promedio: {0:.2f} | Min: {1:.2f} | Max: {2:.2f}".format(
        resultado["Pmd_discount_pct"], resultado["Min_discount_pct"], resultado["Max_discount_pct"]))

    print("Boxes_Shipped -> Promedio: {0:.2f} | Min: {1} | Max: {2}".format(
        resultado["Pmd_boxes_shipped"], resultado["Min_boxes_shipped"], resultado["Max_boxes_shipped"]))

    print("Marketing_Spend -> Promedio: {0:.2f} | Min: {1:.2f} | Max: {2:.2f}".format(
        resultado["Pmd_marketing_spend"], resultado["Min_marketing_spend"], resultado["Max_marketing_spend"]))

    print("\nAño con más pedidos: {0}".format(resultado["Anio_mas_pedidos"]))

    print("\nPedido de mayor Amount:")
    mayor = resultado["Pedido_mayor_amount"]
    print("  Order_ID: {0} | Country: {1} | Order_Date: {2} | Price_per_Box: {3:.2f} | Amount: {4:.2f}".format(
        mayor["Order_ID"], mayor["Country"], mayor["Order_Date"], mayor["Price_per_Box"], mayor["Amount"]))

    print("\nPedido de menor Amount:")
    menor = resultado["Pedido_menor_amount"]
    print("  Order_ID: {0} | Country: {1} | Order_Date: {2} | Price_per_Box: {3:.2f} | Amount: {4:.2f}".format(
        menor["Order_ID"], menor["Country"], menor["Order_Date"], menor["Price_per_Box"], menor["Amount"]))

def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    print("\nIngrese el Precio Minimo del rango en el que desea buscar:")
    min_price = float(input("Precio Mínimo: "))
    print("\nIngrese el Precio Máximo del rango en el que desea buscar:")
    max_price = float(input("Precio Máximo: "))
    print(logic.req_2(control, min_price, max_price))


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    print("\nIngrese la fecha inicial del rango para conocer la cantidad de pedidos:")
    fecha_inicial = input("Fecha Inicial: ")
    print("\nIngrese la fecha final del rango para conocer la cantidad de pedidos:")
    fecha_final = input("Fecha Final: ")
    print(logic.req_3(control,fecha_inicial,fecha_final))


def print_req_4(control):
    """
        Función que imprime la solución del Requerimiento 4 en consola
    """
    print("\nIngrese el país del que desea conocer la cantidad de pedidos:")
    country = input("País: ")
    print("\nIngrese el producto del que desea conocer la cantidad de pedidos:")
    product = input("Producto: ")
    print(logic.req_4(control,product,country))


def print_req_5(control):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    print("\nIngrese el producto del que desea conocer la cantidad de pedidos:")
    product = input("Producto: ")
    print("\nIngrese el filtro para conocer el monto, mayor o menor:")
    filtro = input("FILTRO (MAYOR O MENOR): ")
    print("\nIngrese la fecha inicial del rango para conocer la cantidad de pedidos:")
    fecha_inicial = input("Fecha Inicial: ")
    print("\nIngrese la fecha final del rango para conocer la cantidad de pedidos:")
    fecha_final = input("Fecha Final: ")
    print(logic.req_5(control, filtro, product, fecha_inicial, fecha_final))

def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    
    print("\nIngrese la fecha inicial del rango para conocer la cantidad de pedidos:")
    fecha_inicial = input("Fecha Inicial: ")
    print("\nIngrese la fecha final del rango para conocer la cantidad de pedidos:")
    fecha_final = input("Fecha Final: ")
    print(logic.req_6(control,fecha_inicial,fecha_final))

# Se crea la lógica asociado a la vista
control = new_logic()

# main del ejercicio
def main():
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    while working:
        print_menu()
        inputs = input('Seleccione una opción para continuar\n')
        if int(inputs) == 0:
            print("Cargando información de los archivos ....\n")
            data = load_data(control)
        elif int(inputs) == 1:
            print_req_1(control)

        elif int(inputs) == 2:
            print_req_2(control)

        elif int(inputs) == 3:
            print_req_3(control)

        elif int(inputs) == 4:
            print_req_4(control)

        elif int(inputs) == 5:
            print_req_5(control)

        elif int(inputs) == 6:
            print_req_6(control)

        elif int(inputs) == 7:
            working = False
            print("\nGracias por utilizar el programa") 
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)

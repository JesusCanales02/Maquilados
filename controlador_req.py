# from bd import obtener_conexion


# def insertar_req(id, fecha, area, usuario, descripcion, proceso, ETA):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("INSERT INTO usuarios(fecha, area, usuario, descripcion, proceso, ETA) VALUES (%s, %s, %s, %s, %s, %s, %s)",
#                (fecha, area, usuario, descripcion, proceso, ETA))
#     conexion.commit()
#     conexion.close()


# def obtener_req():
#     conexion = obtener_conexion()
#     requesiciones = []
#     with conexion.cursor() as cursor:
#         cursor.execute("SELECT id, fecha, area, usuario, descripcion, proceso, ETA FROM usuarios")
#         requesiciones = cursor.fetchall()
#     conexion.close()
#     return requesiciones


# def eliminar_req(id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
#     conexion.commit()
#     conexion.close()


# def obtener_req_por_id(id):
#     conexion = obtener_conexion()
#     requesicion = None
#     with conexion.cursor() as cursor:
#         cursor.execute(
#             "SELECT id, fecha, area, usuario, descripcion, proceso, ETA FROM usuarios WHERE id = %s", (id,))
#         requesicion = cursor.fetchone()
#     conexion.close()
#     return requesicion

# def actualizar_req(id, fecha, area, usuario, descripcion, proceso, ETA):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("UPDATE usuarios SET fecha = %s, area = %s, usuario = %s, descripcion = %s, proceso = %s, ETA = %s WHERE id = %s",
#                        (fecha, area, usuario, descripcion, proceso, ETA, id))
#     conexion.commit()
#     conexion.close()
    
# def insertar_item(requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("""
#             INSERT INTO items (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """, (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion))
#     conexion.commit()
#     conexion.close()

# def obtener_items():
#     conexion = obtener_conexion()
#     items = []
#     with conexion.cursor() as cursor:
#         cursor.execute("SELECT * FROM items") 
#         items = cursor.fetchall()
#     conexion.close()
#     return items

# def eliminar_item(id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("DELETE FROM items WHERE id = %s", (id,))
#     conexion.commit()
#     conexion.close()

# def obtener_item_por_id(id):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("SELECT * FROM items WHERE id = %s", (id,))
#         item = cursor.fetchone()
#     conexion.close()
#     return item

# #En la parte de recibos para poder solicitar en la base de datos las variables de oc y cotizacion
# def obtener_items_filtrados(oc, cotizacion):
#     conexion = obtener_conexion()
#     query = "SELECT * FROM items WHERE 1=1" 

#     params = []
    
#     if oc:
#         query += " AND oc = %s"
#         params.append(oc)
    
#     if cotizacion:
#         query += " AND cotizacion = %s"
#         params.append(cotizacion)

#     with conexion.cursor() as cursor:
#         cursor.execute(query, tuple(params))
#         items = cursor.fetchall()

#     conexion.close()
#     return items
from bd import obtener_conexion


def insertar_req(id, fecha, area, usuario, descripcion, proceso, ETA):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(
            "INSERT INTO usuarios(fecha, area, usuario, descripcion, proceso, ETA) VALUES (%s, %s, %s, %s, %s, %s, %s)",
            (fecha, area, usuario, descripcion, proceso, ETA))
    conexion.commit()
    conexion.close()


def obtener_req():
    conexion = obtener_conexion()
    requisiciones = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, fecha, area, usuario, descripcion, proceso, ETA FROM usuarios")
        requisiciones = cursor.fetchall()
    conexion.close()
    return requisiciones


def eliminar_req(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_req_por_id(id):
    conexion = obtener_conexion()
    requisicion = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, fecha, area, usuario, descripcion, proceso, ETA FROM usuarios WHERE id = %s", (id,))
        requisicion = cursor.fetchone()
    conexion.close()
    return requisicion


def actualizar_req(id, fecha, area, usuario, descripcion, proceso, ETA):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET fecha = %s, area = %s, usuario = %s, descripcion = %s, proceso = %s, ETA = %s WHERE id = %s",
                       (fecha, area, usuario, descripcion, proceso, ETA, id))
    conexion.commit()
    conexion.close()


# def insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas):
#     conexion = obtener_conexion()  # Conexión a la base de datos
#     with conexion.cursor() as cursor:
#         cursor.execute("""
#             INSERT INTO requisiciones (fecha, usuario, descripcion, cotizacion, autorizacion, OC, estado, eta, facturas) 
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """, (fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas))
#         requisicion_id = cursor.lastrowid  # Obtenemos el ID de la requisición recién insertada
#     conexion.commit()  # Guardar los cambios
#     conexion.close()  # Cerrar la conexión
#     return requisicion_id  # Devolvemos el ID de la requisición

# def insertar_item(requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute("""
#             INSERT INTO items (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion)
#             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
#         """, (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion))
#     conexion.commit()
#     conexion.close()
def insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas):
    conexion = obtener_conexion()  # Conexión a la base de datos
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO requisiciones (fecha, usuario, descripcion, cotizacion, autorizacion, OC, estado, eta, facturas) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas))
        requisicion_id = cursor.lastrowid  # Obtén el ID generado para la nueva requisición
    conexion.commit()  # Guardar los cambios
    conexion.close()  # Cerrar la conexión
    return requisicion_id  # Retorna el ID generado

def insertar_item(requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO items (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion))
    conexion.commit()
    conexion.close()


def obtener_items():
    conexion = obtener_conexion()
    items = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM items")
        items = cursor.fetchall()
    conexion.close()
    return items


def eliminar_item(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM items WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_item_por_id(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM items WHERE id = %s", (id,))
        item = cursor.fetchone()
    conexion.close()
    return item


def obtener_items_filtrados(oc, cotizacion):
    conexion = obtener_conexion()
    query = "SELECT * FROM items WHERE 1=1"

    params = []

    if oc:
        query += " AND oc = %s"
        params.append(oc)

    if cotizacion:
        query += " AND cotizacion = %s"
        params.append(cotizacion)

    with conexion.cursor() as cursor:
        cursor.execute(query, tuple(params))
        items = cursor.fetchall()

    conexion.close()
    return items

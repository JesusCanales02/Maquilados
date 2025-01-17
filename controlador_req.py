from bd import obtener_conexion

def insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, prioridad, eta, facturas):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO requisiciones (fecha, usuario, descripcion, cotizacion, autorizacion, OC, proceso, prioridad, eta, facturas)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, prioridad, eta, facturas))
    conexion.commit()
    requisicion_id = cursor.lastrowid
    conexion.close()
    return requisicion_id

# Aqui obtenemos el ítem por el id
def obtener_item_por_id(item_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM items WHERE id = %s", (item_id,))
        item = cursor.fetchone()
    conexion.close()
    return item

# Insertarmos los ítems para una requisición
def insertar_item(requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, estado=None, cotizacion=None, autorizacion=None, imagen=None):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            INSERT INTO items (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, estado, cotizacion, autorizacion, imagen)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, estado, cotizacion, autorizacion, imagen))
    conexion.commit()
    conexion.close()



# Obtenemos los ítems
def obtener_items_por_requisicion(requisicion_id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT id, requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, estado, cotizacion, autorizacion, imagen
            FROM items WHERE requisicion_id = %s
        """, (requisicion_id,))
        items = cursor.fetchall()
    conexion.close()
    return items


# Se actualizar el ítem por su ID
def actualizar_item(id, requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, imagen=None):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE items
            SET requisicion_id = %s, descripcion = %s, marca = %s, modelo = %s, cantidad = %s, udm = %s, 
                proveedor = %s, oc = %s, imagen = %s
            WHERE id = %s
        """, (requisicion_id, descripcion, marca, modelo, cantidad, udm, proveedor, oc, imagen, id))
    conexion.commit()
    conexion.close()


# Actualizar el estado de un ítem por su id 
def actualizar_estado_item(item_id, nuevo_estado):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE items
            SET estado = %s
            WHERE id = %s
        """, (nuevo_estado, item_id))
    conexion.commit()
    conexion.close()

def obtener_requisiciones():
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT id, fecha, usuario, descripcion, cotizacion, autorizacion, OC, proceso, prioridad, eta, facturas
            FROM requisiciones
        """)
        requisiciones = cursor.fetchall()
    conexion.close()
    return requisiciones

def obtener_requisiciones_pendientes():
    conexion = obtener_conexion()
    requisiciones = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, descripcion, cantidad, estado
                FROM items
                WHERE estado = 'Pendiente'
            """)
            requisiciones = cursor.fetchall()
    except Exception as e:
        print(f"Error al obtener requisiciones pendientes: {e}")
    finally:
        conexion.close()
    return requisiciones

def actualizar_estado_requisiciones(ids):
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            for id_requisicion in ids:
                cursor.execute("""
                    UPDATE items
                    SET estado = 'Entregado'
                    WHERE id = %s
                """, (id_requisicion,))
        conexion.commit()
    except Exception as e:
        conexion.rollback()
        print(f"Error al actualizar estados: {e}")
        raise e
    finally:
        conexion.close()

def obtener_requisicion_por_id(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("SELECT * FROM requisiciones WHERE id = %s", (id,))
        requisicion = cursor.fetchone()
    conexion.close()
    return requisicion

def actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, prioridad, eta, facturas):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("""
            UPDATE requisiciones 
            SET fecha = %s, usuario = %s, descripcion = %s, cotizacion = %s, autorizacion = %s, OC = %s, 
                proceso = %s, prioridad = %s, eta = %s, facturas = %s
            WHERE id = %s
        """, (fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, prioridad, eta, facturas, id))
    conexion.commit()
    conexion.close()

def eliminar_requisicion(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM requisiciones WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()

def obtener_items_por_area(area_usuario, oc=None, solicitante=None, cotizacion=None):
    conexion = obtener_conexion()
    query = """
        SELECT i.id, i.descripcion, i.marca, i.modelo, i.cantidad, i.udm, i.proveedor, i.estado 
        FROM items i
        JOIN requisiciones r ON i.requisicion_id = r.id
        JOIN empleado e ON r.usuario = e.Nombre
        JOIN area a ON e.IdArea = a.IdArea
        WHERE a.NombreArea = %s
    """
    params = [area_usuario]

    if oc:
        query += " AND r.oc = %s"
        params.append(oc)
    if solicitante:
        query += " AND r.usuario = %s"
        params.append(solicitante)
    if cotizacion:
        query += " AND r.cotizacion = %s"
        params.append(cotizacion)

    with conexion.cursor() as cursor:
        cursor.execute(query, tuple(params))
        items = cursor.fetchall()
    conexion.close()
    return items

def obtener_archivo_por_campo(id, campo):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute(f"SELECT {campo} FROM requisiciones WHERE id = %s", (id,))
        archivo = cursor.fetchone()
    conexion.close()
    return archivo


from bd import obtener_conexion


def insertar_req(id, fecha, area, usuario, descripcion, proceso, ETA):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("INSERT INTO usuarios(id, fecha, area, usuario, descripcion, proceso, ETA) VALUES (%s, %s, %s, %s, %s, %s, %s)",
               (id, fecha, area, usuario, descripcion, proceso, ETA))
    conexion.commit()
    conexion.close()


def obtener_req():
    conexion = obtener_conexion()
    requesiciones = []
    with conexion.cursor() as cursor:
        cursor.execute("SELECT id, fecha, area, usuario, descripcion, proceso, ETA FROM usuarios")
        requesiciones = cursor.fetchall()
    conexion.close()
    return requesiciones


def eliminar_req(id):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("DELETE FROM usuarios WHERE id = %s", (id,))
    conexion.commit()
    conexion.close()


def obtener_req_por_id(id):
    conexion = obtener_conexion()
    requesicion = None
    with conexion.cursor() as cursor:
        cursor.execute(
            "SELECT id, fecha, area, usuario, descripcion, proceso, ETA FROM usuarios WHERE id = %s", (id,))
        requesicion = cursor.fetchone()
    conexion.close()
    return requesicion


def actualizar_req(id, fecha, area, usuario, descripcion, proceso, ETA):
    conexion = obtener_conexion()
    with conexion.cursor() as cursor:
        cursor.execute("UPDATE usuarios SET fecha = %s, area = %s, usuario = %s, descripcion = %s, proceso = %s, ETA = %s WHERE id = %s",
                       (fecha, area, usuario, descripcion, proceso, ETA, id))
    conexion.commit()
    conexion.close()

from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
import controlador_req
from bd import obtener_conexion
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def guardar_archivo(file):
    """Función para guardar un archivo y devolver su ruta."""
    if file and file.filename != '':
        filename = secure_filename(file.filename)
        path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(path)
        return path
    return None

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        try:
            no_empleado = int(request.form['noEmpleado'])  
        except ValueError:
            flash('Por favor, ingresa un número válido de empleado', 'danger')
            return render_template('login.html')

        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT empleado.*, area.NombreArea 
                FROM empleado
                JOIN area ON empleado.IdArea = area.IdArea
                WHERE empleado.IdEmpleado = %s
            """, (no_empleado,))
            empleado = cursor.fetchone()

        conexion.close()

        if empleado and empleado['Estatus'] != 'BAJA':
            session['empleado_id'] = empleado['IdEmpleado']
            session['empleado_nombre'] = empleado['Nombre']
            session['empleado_area'] = empleado['NombreArea']
            return redirect(url_for('requesiciones'))
        else:
            flash('Número de empleado incorrecto', 'danger')
    return render_template('login.html')

@app.route("/logout")
def logout():
    session.pop('empleado_id', None)
    session.pop('empleado_nombre', None)
    return redirect(url_for('login'))

@app.route('/actualizar_estado_recibo', methods=['POST'])
def actualizar_estado_recibo():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))

    item_ids = request.form.getlist('item_ids[]')
    estados = request.form.getlist('estados[]')

    print("IDs recibidos:", item_ids) 
    print("Estados recibidos:", estados)  

    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            for item_id, estado in zip(item_ids, estados):
                print(f"Actualizando item_id={item_id} con estado={estado}")
                cursor.execute(
                    "UPDATE items SET estado = %s WHERE id = %s",
                    (estado, item_id)
                )
        conexion.commit()
        flash("Los estados se actualizaron correctamente.", "success")
    except Exception as e:
        conexion.rollback()
        print("Error al actualizar:", str(e))
        flash(f"Error al actualizar los estados: {e}", "danger")
    finally:
        conexion.close()

    return redirect(url_for('formulario_recibo'))



@app.route('/entregas', methods=['GET', 'POST'])
def formulario_entregas():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))

    conexion = obtener_conexion()

    if request.method == 'POST':
        confirmados = request.form.getlist('confirmar')
        if confirmados:
            try:
                with conexion.cursor() as cursor:
                    for id_requisicion in confirmados:
                        cursor.execute("""
                            UPDATE items
                            SET estado = 'Entregado'
                            WHERE id = %s
                        """, (id_requisicion,))
                conexion.commit()
                flash(f"{len(confirmados)} entrega(s) confirmada(s) exitosamente.", "success")
            except Exception as e:
                conexion.rollback()
                flash(f"Error al confirmar entregas: {str(e)}", "danger")
        else:
            flash("No seleccionaste ninguna entrega para confirmar.", "warning")

    requisiciones = []
    try:
        with conexion.cursor() as cursor:
            cursor.execute("""
                SELECT id, descripcion, cantidad, estado
                FROM items
                WHERE estado IN ('Pendiente', 'Recibido')
            """)
            requisiciones = cursor.fetchall()
    except Exception as e:
        flash(f"Error al obtener requisiciones: {str(e)}", "danger")
    finally:
        conexion.close()

    return render_template("entregas.html", requisiciones=requisiciones)



@app.route("/agregar_req")
def formulario_agregar_req():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))
    return render_template("agregar_req.html", usuario=session['empleado_nombre'])

@app.route("/descargar_archivo/<int:id>/<campo>")
def descargar_archivo(id, campo):
    campos_permitidos = ["cotizacion", "autorizacion", "oc"]
    if campo not in campos_permitidos:
        flash("Campo no válido para descarga.", "danger")
        return redirect(url_for("requesiciones"))
    
    archivo = controlador_req.obtener_archivo_por_campo(id, campo)
    if archivo and archivo[campo]:
        archivo_path = archivo[campo]
        if os.path.exists(archivo_path):
            return send_file(archivo_path, as_attachment=True)
        else:
            flash("Archivo no encontrado en el servidor.", "danger")
    else:
        flash("Archivo no disponible.", "danger")
    
    return redirect(url_for("editar_req", id=id))


@app.route("/guardar_req", methods=["POST"])
def guardar_req():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))

    cotizacion_file = request.files.get("cotizacion")
    autorizacion_file = request.files.get("autorizacion")
    oc_file = request.files.get("oc_file")
    cotizacion_data = cotizacion_file.read() if cotizacion_file and cotizacion_file.filename != '' else None
    autorizacion_data = autorizacion_file.read() if autorizacion_file and autorizacion_file.filename != '' else None
    oc_file_path = guardar_archivo(oc_file) if oc_file and oc_file.filename != '' else None

    fecha = request.form.get("fecha_solicitud")
    usuario = session['empleado_nombre']
    descripcion = request.form.get("descripcion_general")
    proceso = request.form.get("proceso") or None
    prioridad = request.form.get("prioridad") or None
    eta = request.form.get("eta") or None
    facturas = request.form.get("facturas") or None

    requisicion_id = controlador_req.insertar_requisicion(
        fecha, usuario, descripcion, cotizacion_data, autorizacion_data, oc_file_path, proceso, prioridad, eta, facturas
    )

    descripciones = request.form.getlist('descripcion[]')
    marcas = request.form.getlist('marca[]')
    modelos = request.form.getlist('modelo[]')
    cantidades = request.form.getlist('cantidad[]')
    udms = request.form.getlist('udm[]')
    proveedores = request.form.getlist('proveedor[]')
    ocs = request.form.getlist('oc[]')  
    imagenes = request.files.getlist('imagen[]')

    for i in range(len(descripciones)):
        imagen_path = guardar_archivo(imagenes[i]) if imagenes[i].filename != '' else None
        controlador_req.insertar_item(
            requisicion_id, descripciones[i], marcas[i], modelos[i], cantidades[i],
            udms[i], proveedores[i], ocs[i], None, None, imagen_path
        )

    return redirect("/requesiciones")



# @app.route("/recibo")
# def formulario_recibo():
#     if 'empleado_id' not in session:  
#         return redirect(url_for('login'))  # Verificar si el usuario está logueado
#     area_usuario = session.get('empleado_area')  # Obtener el área del usuario desde la sesión

#     # Obtener ítems relacionados con el área del usuario
#     conexion = obtener_conexion()
#     query = """
#         SELECT i.id, i.descripcion, i.marca, i.modelo, i.cantidad, i.udm, i.proveedor, i.estado
#         FROM items i
#         JOIN requisiciones r ON i.requisicion_id = r.id
#         JOIN empleado e ON r.usuario = e.Nombre
#         JOIN area a ON e.IdArea = a.IdArea
#         WHERE a.NombreArea = %s
#     """
#     params = [area_usuario]

#     with conexion.cursor() as cursor:
#         cursor.execute(query, tuple(params))
#         items = cursor.fetchall()
#     conexion.close()

#     return render_template("recibo.html", items=items)



@app.route("/requesiciones")
def requesiciones():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))

    conexion = obtener_conexion()
    requisiciones = []
    area_usuario = session['empleado_area']
    nombre_usuario = session['empleado_nombre']

    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT r.id, r.fecha, a.NombreArea AS area, r.usuario, r.descripcion, r.proceso, r.ETA 
            FROM requisiciones r
            JOIN empleado e ON r.usuario = e.Nombre
            JOIN area a ON e.IdArea = a.IdArea
            WHERE a.NombreArea = %s AND e.Estatus != 'BAJA'
        """, (area_usuario,))
        requisiciones = cursor.fetchall()

    conexion.close()

    return render_template("requesiciones.html", requisiciones=requisiciones, usuario=nombre_usuario)

@app.route("/recibo", methods=["GET", "POST"])
def formulario_recibo():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))

    items = []
    if request.method == "POST":
        oc = request.form.get("oc")
        solicitante = request.form.get("solicitante")
        cotizacion = request.form.get("cotizacion")

        conexion = obtener_conexion()
        query = """
            SELECT i.id, i.descripcion, i.marca, i.modelo, i.cantidad, i.udm, i.proveedor, i.oc, i.estado
            FROM items i
            JOIN requisiciones r ON i.requisicion_id = r.id
            WHERE 1=1
        """
        params = []
        if oc:
            query += " AND i.oc = %s"
            params.append(oc)
        if solicitante:
            query += " AND r.usuario LIKE %s"
            params.append(f"%{solicitante}%")
        if cotizacion:
            query += " AND r.cotizacion = %s"
            params.append(cotizacion)

        with conexion.cursor() as cursor:
            cursor.execute(query, tuple(params))
            items = cursor.fetchall()

        conexion.close()
        if not items:
            flash("No se encontraron resultados para tu búsqueda.", "danger")

    return render_template("recibo.html", items=items)



@app.route("/eliminar_req", methods=["POST"])
def eliminar_req():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))
    controlador_req.eliminar_requisicion(request.form["id"])
    return redirect("/requesiciones")

@app.route("/editar_req/<int:id>")
def editar_req(id):
    if 'empleado_id' not in session:
        return redirect(url_for('login'))
    requisicion = controlador_req.obtener_requisicion_por_id(id)
    items = controlador_req.obtener_items_por_requisicion(id)  # Incluye el campo OC aquí
    return render_template("editar_req.html", requisicion=requisicion, items=items)


@app.route("/actualizar_req", methods=["POST"])
def actualizar_req():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))

    id = request.form["id"]
    fecha = request.form["fecha"]
    usuario = session['empleado_nombre']
    descripcion = request.form["descripcion_general"]
    proceso = request.form.get("proceso") or None
    prioridad = request.form.get("prioridad") or None
    eta = request.form.get("eta") or None
    facturas = request.form.get("facturas") or None

    controlador_req.actualizar_requisicion(
        id, fecha, usuario, descripcion, None, None, None, proceso, prioridad, eta, facturas
    )

    # Manejar los ítems
    item_ids = request.form.getlist('item_id[]')  
    descripciones = request.form.getlist('descripcion[]')
    marcas = request.form.getlist('marca[]')
    modelos = request.form.getlist('modelo[]')
    cantidades = request.form.getlist('cantidad[]')
    udms = request.form.getlist('udm[]')
    proveedores = request.form.getlist('proveedor[]')
    ocs = request.form.getlist('oc[]')
    imagenes = request.files.getlist('imagen[]')

    for i in range(len(item_ids)):
        nueva_imagen = guardar_archivo(imagenes[i]) if imagenes[i].filename != '' else None
        imagen_actual = controlador_req.obtener_item_por_id(item_ids[i])['imagen'] if nueva_imagen is None else nueva_imagen

        controlador_req.actualizar_item(
            id=item_ids[i],  
            requisicion_id=id,
            descripcion=descripciones[i],
            marca=marcas[i],
            modelo=modelos[i],
            cantidad=cantidades[i],
            udm=udms[i],
            proveedor=proveedores[i],
            oc=ocs[i],
            imagen=imagen_actual
        )

    return redirect("/requesiciones")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

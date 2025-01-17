#--------------------------------------------------------------------------------------------------------

# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import controlador_req
# from bd import obtener_conexion

# app = Flask(__name__)
# app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para manejar sesiones

# # Ruta principal redirige al login
# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# # Ruta para el login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         try:
#             no_empleado = int(request.form['noEmpleado'])  # Convertir el número de empleado a entero
#         except ValueError:
#             flash('Por favor, ingresa un número válido de empleado', 'danger')
#             return render_template('login.html')

#         conexion = obtener_conexion()
#         with conexion.cursor() as cursor:
#             # Consulta con JOIN para obtener el área
#             cursor.execute("""
#                 SELECT empleado.*, area.NombreArea 
#                 FROM empleado
#                 JOIN area ON empleado.IdArea = area.IdArea
#                 WHERE empleado.IdEmpleado = %s
#             """, (no_empleado,))
#             empleado = cursor.fetchone()

#         conexion.close()

#         if empleado and empleado['Estatus'] != 'BAJA':  # Verificar que el empleado no esté en BAJA
#             session['empleado_id'] = empleado['IdEmpleado']
#             session['empleado_nombre'] = empleado['Nombre']
#             session['empleado_area'] = empleado['NombreArea']  # Guardar el área en la sesión
#             return redirect(url_for('requesiciones'))  # Redirigir a la página de requisiciones
#         else:
#             flash('Número de empleado incorrecto', 'danger')  # Mostrar advertencia
#     return render_template('login.html')


# @app.route("/agregar_req")
# def formulario_agregar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
#     return render_template("agregar_req.html", usuario=session['empleado_nombre'])

# @app.route("/logout")
# def logout():
#     session.pop('empleado_id', None)  # Limpiar la sesión del empleado
#     session.pop('empleado_nombre', None)  # Limpiar el nombre del empleado en la sesión
#     return redirect(url_for('login'))  # Redirigir al login después de salir

# @app.route("/recibo")
# def formulario_recibo():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     items = controlador_req.obtener_items()
#     return render_template("recibo.html", items=items)

# @app.route("/entregas")
# def formulario_entregas():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     return render_template("entregas.html")

# # Ruta para guardar una nueva requisición
# @app.route("/guardar_req", methods=["POST"])
# def guardar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login

#     # Capturamos los valores del formulario
#     fecha = request.form.get("fecha_solicitud")
#     usuario = session['empleado_nombre']  # Usamos el nombre del usuario de la sesión
#     descripcion = request.form.get("descripcion_general")
#     cotizacion = request.form.get("cotizacion") or None
#     autorizacion = request.form.get("autorizacion") or None
#     oc = request.form.get("oc") or None
#     proceso = request.form.get("proceso") or None
#     eta = request.form.get("eta") or None
#     facturas = request.form.get("facturas") or None

#     # Insertar la requisición en la tabla requisiciones
#     requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, eta, facturas)

#     # Capturamos los ítems de la requisición
#     descripciones = request.form.getlist('descripcion[]')
#     marcas = request.form.getlist('marca[]')
#     modelos = request.form.getlist('modelo[]')
#     cantidades = request.form.getlist('cantidad[]')
#     udms = request.form.getlist('udm[]')
#     proveedores = request.form.getlist('proveedor[]')
#     ocs = request.form.getlist('oc[]')

#     # Insertar los ítems en la tabla items asociados con la requisición
#     for i in range(len(descripciones)):
#         controlador_req.insertar_item(requisicion_id, descripciones[i], marcas[i], modelos[i], cantidades[i], udms[i], proveedores[i], ocs[i], cotizacion, autorizacion)

#     return redirect("/requesiciones")

# @app.route("/requesiciones")
# def requesiciones():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login

#     conexion = obtener_conexion()
#     requisiciones = []

#     # Obtener el área y el nombre del usuario logueado
#     area_usuario = session['empleado_area']
#     nombre_usuario = session['empleado_nombre']

#     # Consulta para obtener las requisiciones de la misma área y que no estén en estado de baja
#     with conexion.cursor() as cursor:
#         cursor.execute("""
#             SELECT r.id, r.fecha, a.NombreArea AS area, r.usuario, r.descripcion, r.proceso, r.ETA 
#             FROM requisiciones r
#             JOIN empleado e ON r.usuario = e.Nombre  -- Relacionamos con la tabla empleado
#             JOIN area a ON e.IdArea = a.IdArea  -- Relacionamos el área desde la tabla empleado
#             WHERE a.NombreArea = %s AND e.Estatus != 'BAJA'  -- Filtramos por área y que no estén de baja
#         """, (area_usuario,))
#         requisiciones = cursor.fetchall()

#     conexion.close()

#     # Pasar el nombre del usuario al contexto de la plantilla
#     return render_template("requesiciones.html", requisiciones=requisiciones, usuario=nombre_usuario)




# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/editar_req/<int:id>")
# def editar_req(id):
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     items = controlador_req.obtener_items_por_requisicion(id)
#     return render_template("editar_req.html", requisicion=requisicion, items=items)



# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
    
#     try:
#         id = request.form["id"]
#         fecha = request.form["fecha"]
#         usuario = session['empleado_nombre']
#         descripcion = request.form["descripcion_general"]
#         cotizacion = request.form.get("cotizacion") or None
#         autorizacion = request.form.get("autorizacion") or None
#         oc = request.form.get("oc") or None
#         proceso = request.form.get("proceso") or None
#         eta = request.form.get("eta") or None
#         facturas = request.form.get("facturas") or None

#         # Lógica para actualizar en la base de datos
#         controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, eta, facturas)
#         return redirect("/requesiciones")
#     except KeyError as e:
#         flash(f"Error: campo '{e.args[0]}' no encontrado en el formulario.", "danger")
#         return redirect(url_for('formulario_editar_req', id=id))


# # Ruta para filtrar recibos
# @app.route("/recibo", methods=["GET", "POST"])
# def filtrar_recibo():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     oc = request.form.get("oc")
#     cotizacion = request.form.get("cotizacion")

#     items = controlador_req.obtener_items_filtrados(oc, cotizacion)
#     return render_template("recibo.html", items=items)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000, debug=True)
#------------------------------------------------------------------- si funciona

# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import controlador_req
# from bd import obtener_conexion
# import os
# from werkzeug.utils import secure_filename

# app = Flask(__name__)
# app.secret_key = 'tu_clave_secreta_aqui'  
# UPLOAD_FOLDER = 'uploads'  
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# os.makedirs(UPLOAD_FOLDER, exist_ok=True) 

# # Ruta principal redirige al login
# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# # Ruta para el login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         try:
#             no_empleado = int(request.form['noEmpleado'])  # Convertir el número de empleado a entero
#         except ValueError:
#             flash('Por favor, ingresa un número válido de empleado', 'danger')
#             return render_template('login.html')

#         conexion = obtener_conexion()
#         with conexion.cursor() as cursor:
#             # Consulta con JOIN para obtener el área
#             cursor.execute("""
#                 SELECT empleado.*, area.NombreArea 
#                 FROM empleado
#                 JOIN area ON empleado.IdArea = area.IdArea
#                 WHERE empleado.IdEmpleado = %s
#             """, (no_empleado,))
#             empleado = cursor.fetchone()

#         conexion.close()

#         if empleado and empleado['Estatus'] != 'BAJA':  
#             session['empleado_id'] = empleado['IdEmpleado']
#             session['empleado_nombre'] = empleado['Nombre']
#             session['empleado_area'] = empleado['NombreArea'] 
#             return redirect(url_for('requesiciones'))  
#         else:
#             flash('Número de empleado incorrecto', 'danger')  
#     return render_template('login.html')


# @app.route("/agregar_req")
# def formulario_agregar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
#     return render_template("agregar_req.html", usuario=session['empleado_nombre'])

# @app.route("/logout")
# def logout():
#     session.pop('empleado_id', None)  # Limpiar la sesión del empleado
#     session.pop('empleado_nombre', None)  # Limpiar el nombre del empleado en la sesión
#     return redirect(url_for('login'))  # Redirigir al login después de salir

# @app.route("/recibo")
# def formulario_recibo():
#     if 'empleado_id' not in session:  
#         return redirect(url_for('login'))  
#     items = controlador_req.obtener_items()
#     return render_template("recibo.html", items=items)

# @app.route("/entregas")
# def formulario_entregas():
#     if 'empleado_id' not in session:  
#         return redirect(url_for('login'))
#     return render_template("entregas.html")


# import os
# from werkzeug.utils import secure_filename

# # Configuración para la carpeta de carga de imágenes
# UPLOAD_FOLDER = 'uploads'  # Asegúrate de que la carpeta 'uploads' exista y tenga permisos de escritura
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route("/guardar_req", methods=["POST"])
# def guardar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))

#     # Captura de archivos subidos
#     cotizacion_file = request.files.get("cotizacion")
#     autorizacion_file = request.files.get("autorizacion")
#     oc_file = request.files.get("oc")

#     # Ruta para guardar los archivos subidos
#     cotizacion_path = None
#     autorizacion_path = None
#     oc_path = None

#     # Guardar "Cotización" si se sube un archivo
#     if cotizacion_file and cotizacion_file.filename != '':
#         cotizacion_filename = secure_filename(cotizacion_file.filename)
#         cotizacion_path = os.path.join(app.config['UPLOAD_FOLDER'], cotizacion_filename)
#         cotizacion_file.save(cotizacion_path)

#     # Guardar "Autorización" si se sube un archivo
#     if autorizacion_file and autorizacion_file.filename != '':
#         autorizacion_filename = secure_filename(autorizacion_file.filename)
#         autorizacion_path = os.path.join(app.config['UPLOAD_FOLDER'], autorizacion_filename)
#         autorizacion_file.save(autorizacion_path)

#     # Guardar "OC" si se sube un archivo
#     if oc_file and oc_file.filename != '':
#         oc_filename = secure_filename(oc_file.filename)
#         oc_path = os.path.join(app.config['UPLOAD_FOLDER'], oc_filename)
#         oc_file.save(oc_path)

#     # Otros campos del formulario
#     fecha = request.form.get("fecha_solicitud")
#     usuario = session['empleado_nombre']
#     descripcion = request.form.get("descripcion_general")
#     proceso = request.form.get("proceso") or None
#     prioridad = request.form.get("prioridad") or None
#     eta = request.form.get("eta") or None
#     facturas = request.form.get("facturas") or None

#     # Insertar en la base de datos
#     requisicion_id = controlador_req.insertar_requisicion(
#         fecha, usuario, descripcion, cotizacion_path, autorizacion_path, oc_path, proceso, prioridad, eta, facturas
#     )

#     # Manejo de ítems (no cambian)
#     descripciones = request.form.getlist('descripcion[]')
#     marcas = request.form.getlist('marca[]')
#     modelos = request.form.getlist('modelo[]')
#     cantidades = request.form.getlist('cantidad[]')
#     udms = request.form.getlist('udm[]')
#     proveedores = request.form.getlist('proveedor[]')
#     imagenes = request.files.getlist('imagen[]')

#     rutas_imagenes = []
#     for imagen in imagenes:
#         if imagen and imagen.filename != '':
#             nombre_archivo = secure_filename(imagen.filename)
#             ruta_completa = os.path.join(app.config['UPLOAD_FOLDER'], nombre_archivo)
#             imagen.save(ruta_completa)
#             rutas_imagenes.append(nombre_archivo)
#         else:
#             rutas_imagenes.append(None)

#     for i in range(len(descripciones)):
#         ruta_imagen = rutas_imagenes[i] if i < len(rutas_imagenes) else None
#         controlador_req.insertar_item(requisicion_id, descripciones[i], marcas[i], modelos[i], cantidades[i], udms[i], proveedores[i], None, None, ruta_imagen)

#     return redirect("/requesiciones")

# @app.route("/requesiciones")
# def requesiciones():
#     if 'empleado_id' not in session:  
#         return redirect(url_for('login'))

#     conexion = obtener_conexion()
#     requisiciones = []

#     # Obtener el área y el nombre del usuario logueado
#     area_usuario = session['empleado_area']
#     nombre_usuario = session['empleado_nombre']

#     # Consulta para obtener las requisiciones de la misma área y que no estén en estado de baja
#     with conexion.cursor() as cursor:
#         cursor.execute("""
#             SELECT r.id, r.fecha, a.NombreArea AS area, r.usuario, r.descripcion, r.proceso, r.ETA 
#             FROM requisiciones r
#             JOIN empleado e ON r.usuario = e.Nombre  -- Relacionamos con la tabla empleado
#             JOIN area a ON e.IdArea = a.IdArea  -- Relacionamos el área desde la tabla empleado
#             WHERE a.NombreArea = %s AND e.Estatus != 'BAJA'  -- Filtramos por área y que no estén de baja
#         """, (area_usuario,))
#         requisiciones = cursor.fetchall()

#     conexion.close()

#     return render_template("requesiciones.html", requisiciones=requisiciones, usuario=nombre_usuario)




# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     if 'empleado_id' not in session:  
#         return redirect(url_for('login'))  
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/editar_req/<int:id>")
# def editar_req(id):
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     items = controlador_req.obtener_items_por_requisicion(id)
#     return render_template("editar_req.html", requisicion=requisicion, items=items)



# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
    
#     try:
#         id = request.form["id"]
#         fecha = request.form["fecha"]
#         usuario = session['empleado_nombre']
#         descripcion = request.form["descripcion_general"]
#         cotizacion = request.form.get("cotizacion") or None
#         autorizacion = request.form.get("autorizacion") or None
#         oc = request.form.get("oc") or None
#         proceso = request.form.get("proceso") or None
#         prioridad = request.form.get("prioridad") or None  # Agrega esto
#         eta = request.form.get("eta") or None
#         facturas = request.form.get("facturas") or None

#         # Llama a la función del controlador con todos los argumentos
#         controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, prioridad, eta, facturas)
        
#         return redirect("/requesiciones")
#     except KeyError as e:
#         flash(f"Error: campo '{e.args[0]}' no encontrado en el formulario.", "danger")
#         return redirect(url_for('formulario_editar_req', id=id))



# # Ruta para filtrar recibos
# @app.route("/recibo", methods=["GET", "POST"])
# def filtrar_recibo():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     oc = request.form.get("oc")
#     cotizacion = request.form.get("cotizacion")

#     items = controlador_req.obtener_items_filtrados(oc, cotizacion)
#     return render_template("recibo.html", items=items)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000, debug=True)
#------------------------------------------------------------------------funciona
# from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
# import controlador_req
# from bd import obtener_conexion
# import os
# from flask import make_response
# from werkzeug.utils import secure_filename

# # Inicialización de la app y configuración
# app = Flask(__name__)
# app.secret_key = 'tu_clave_secreta_aqui'
# UPLOAD_FOLDER = 'uploads'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
# os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# def guardar_archivo(file):
#     """Función para guardar un archivo y devolver su ruta."""
#     if file and file.filename != '':
#         filename = secure_filename(file.filename)
#         path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
#         file.save(path)
#         return path
#     return None

# # Ruta para descargar archivos
# @app.route("/descargar/<int:id>/<string:campo>")
# def descargar_archivo(id, campo):
#     conexion = obtener_conexion()
#     with conexion.cursor() as cursor:
#         cursor.execute(f"SELECT {campo} FROM requisiciones WHERE id = %s", (id,))
#         archivo = cursor.fetchone()
#     conexion.close()

#     if archivo and archivo[campo]:
#         # Devolver el archivo almacenado en la carpeta de uploads
#         return send_file(archivo[campo], as_attachment=True)
#     else:
#         flash('Archivo no encontrado', 'danger')
#         return redirect(url_for('requesiciones'))

# # Ruta principal redirige al login
# @app.route('/')
# def index():
#     return redirect(url_for('login'))

# # Ruta para el login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         try:
#             no_empleado = int(request.form['noEmpleado'])  # Convertir el número de empleado a entero
#         except ValueError:
#             flash('Por favor, ingresa un número válido de empleado', 'danger')
#             return render_template('login.html')

#         conexion = obtener_conexion()
#         with conexion.cursor() as cursor:
#             # Consulta con JOIN para obtener el área
#             cursor.execute("""
#                 SELECT empleado.*, area.NombreArea 
#                 FROM empleado
#                 JOIN area ON empleado.IdArea = area.IdArea
#                 WHERE empleado.IdEmpleado = %s
#             """, (no_empleado,))
#             empleado = cursor.fetchone()

#         conexion.close()

#         if empleado and empleado['Estatus'] != 'BAJA':
#             session['empleado_id'] = empleado['IdEmpleado']
#             session['empleado_nombre'] = empleado['Nombre']
#             session['empleado_area'] = empleado['NombreArea']
#             return redirect(url_for('requesiciones'))
#         else:
#             flash('Número de empleado incorrecto', 'danger')
#     return render_template('login.html')

# @app.route("/logout")
# def logout():
#     session.pop('empleado_id', None)
#     session.pop('empleado_nombre', None)
#     return redirect(url_for('login'))

# @app.route("/entregas")
# def formulario_entregas():
#     if 'empleado_id' not in session:  
#         return redirect(url_for('login'))
#     return render_template("entregas.html")

# @app.route("/agregar_req")
# def formulario_agregar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
#     return render_template("agregar_req.html", usuario=session['empleado_nombre'])

# @app.route("/guardar_req", methods=["POST"])
# def guardar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))

#     # Captura de archivos subidos
#     cotizacion_file = request.files.get("cotizacion")
#     autorizacion_file = request.files.get("autorizacion")
#     oc_file = request.files.get("oc")

#     # Leer contenido binario de los archivos
#     cotizacion_data = cotizacion_file.read() if cotizacion_file and cotizacion_file.filename != '' else None
#     autorizacion_data = autorizacion_file.read() if autorizacion_file and autorizacion_file.filename != '' else None
#     oc_data = oc_file.read() if oc_file and oc_file.filename != '' else None

#     # Otros campos del formulario
#     fecha = request.form.get("fecha_solicitud")
#     usuario = session['empleado_nombre']
#     descripcion = request.form.get("descripcion_general")
#     proceso = request.form.get("proceso") or None
#     prioridad = request.form.get("prioridad") or None
#     eta = request.form.get("eta") or None
#     facturas = request.form.get("facturas") or None

#     # Insertar en la base de datos
#     requisicion_id = controlador_req.insertar_requisicion(
#         fecha, usuario, descripcion, cotizacion_data, autorizacion_data, oc_data, proceso, prioridad, eta, facturas
#     )

#     # Manejo de ítems (no cambian)
#     descripciones = request.form.getlist('descripcion[]')
#     marcas = request.form.getlist('marca[]')
#     modelos = request.form.getlist('modelo[]')
#     cantidades = request.form.getlist('cantidad[]')
#     udms = request.form.getlist('udm[]')
#     proveedores = request.form.getlist('proveedor[]')
#     imagenes = request.files.getlist('imagen[]')

#     rutas_imagenes = [img.read() if img and img.filename != '' else None for img in imagenes]

#     for i in range(len(descripciones)):
#         controlador_req.insertar_item(
#             requisicion_id, descripciones[i], marcas[i], modelos[i], cantidades[i], udms[i], proveedores[i], None, None, rutas_imagenes[i]
#         )

#     return redirect("/requesiciones")


# @app.route("/recibo")
# def formulario_recibo():
#     if 'empleado_id' not in session:  
#         return redirect(url_for('login'))  
#     items = controlador_req.obtener_items()
#     return render_template("recibo.html", items=items)

# @app.route("/requesiciones")
# def requesiciones():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))

#     conexion = obtener_conexion()
#     requisiciones = []

#     # Obtener el área y el nombre del usuario logueado
#     area_usuario = session['empleado_area']
#     nombre_usuario = session['empleado_nombre']

#     # Consulta para obtener las requisiciones
#     with conexion.cursor() as cursor:
#         cursor.execute("""
#             SELECT r.id, r.fecha, a.NombreArea AS area, r.usuario, r.descripcion, r.proceso, r.ETA 
#             FROM requisiciones r
#             JOIN empleado e ON r.usuario = e.Nombre
#             JOIN area a ON e.IdArea = a.IdArea
#             WHERE a.NombreArea = %s AND e.Estatus != 'BAJA'
#         """, (area_usuario,))
#         requisiciones = cursor.fetchall()

#     conexion.close()

#     return render_template("requesiciones.html", requisiciones=requisiciones, usuario=nombre_usuario)

# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/editar_req/<int:id>")
# def editar_req(id):
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     items = controlador_req.obtener_items_por_requisicion(id)
#     return render_template("editar_req.html", requisicion=requisicion, items=items)

# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     if 'empleado_id' not in session:
#         return redirect(url_for('login'))

#     id = request.form["id"]
#     fecha = request.form["fecha"]
#     usuario = session['empleado_nombre']
#     descripcion = request.form["descripcion_general"]
#     proceso = request.form.get("proceso") or None
#     prioridad = request.form.get("prioridad") or None
#     eta = request.form.get("eta") or None
#     facturas = request.form.get("facturas") or None

#     controlador_req.actualizar_requisicion(
#         id, fecha, usuario, descripcion, None, None, None, proceso, prioridad, eta, facturas
#     )

#     return redirect("/requesiciones")
# @app.route("/recibo", methods=["GET", "POST"])
# def filtrar_recibo():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     oc = request.form.get("oc")
#     cotizacion = request.form.get("cotizacion")

#     items = controlador_req.obtener_items_filtrados(oc, cotizacion)
#     return render_template("recibo.html", items=items)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000, debug=True)
#--------------------------------------------------------------------si funcionaaaa
from flask import Flask, render_template, request, redirect, url_for, flash, session, send_file
import controlador_req
from bd import obtener_conexion
import os
from werkzeug.utils import secure_filename

# Inicialización de la app y configuración
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
            no_empleado = int(request.form['noEmpleado'])  # Convertir el número de empleado a entero
        except ValueError:
            flash('Por favor, ingresa un número válido de empleado', 'danger')
            return render_template('login.html')

        conexion = obtener_conexion()
        with conexion.cursor() as cursor:
            # Consulta con JOIN para obtener el área
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

    print("IDs recibidos:", item_ids)  # Para depuración
    print("Estados recibidos:", estados)  # Para depuración

    # Conexión a la base de datos
    conexion = obtener_conexion()
    try:
        with conexion.cursor() as cursor:
            # Actualiza cada ítem en la base de datos
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
        # Confirmar entregas
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

    # Obtener requisiciones pendientes o recibidas
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
    # Verificar si el campo solicitado es válido
    campos_permitidos = ["cotizacion", "autorizacion", "oc"]
    if campo not in campos_permitidos:
        flash("Campo no válido para descarga.", "danger")
        return redirect(url_for("requesiciones"))
    
    # Obtener el archivo desde la base de datos
    archivo = controlador_req.obtener_archivo_por_campo(id, campo)
    if archivo and archivo[campo]:
        # Ruta al archivo almacenado
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

    # Captura de archivos subidos y otros datos generales
    cotizacion_file = request.files.get("cotizacion")
    autorizacion_file = request.files.get("autorizacion")
    oc_file = request.files.get("oc_file")
    cotizacion_data = cotizacion_file.read() if cotizacion_file and cotizacion_file.filename != '' else None
    autorizacion_data = autorizacion_file.read() if autorizacion_file and autorizacion_file.filename != '' else None
    oc_file_path = guardar_archivo(oc_file) if oc_file and oc_file.filename != '' else None

    # Datos de la requisición
    fecha = request.form.get("fecha_solicitud")
    usuario = session['empleado_nombre']
    descripcion = request.form.get("descripcion_general")
    proceso = request.form.get("proceso") or None
    prioridad = request.form.get("prioridad") or None
    eta = request.form.get("eta") or None
    facturas = request.form.get("facturas") or None

    # Insertar la requisición en la base de datos
    requisicion_id = controlador_req.insertar_requisicion(
        fecha, usuario, descripcion, cotizacion_data, autorizacion_data, oc_file_path, proceso, prioridad, eta, facturas
    )

    # Manejo de ítems
    descripciones = request.form.getlist('descripcion[]')
    marcas = request.form.getlist('marca[]')
    modelos = request.form.getlist('modelo[]')
    cantidades = request.form.getlist('cantidad[]')
    udms = request.form.getlist('udm[]')
    proveedores = request.form.getlist('proveedor[]')
    ocs = request.form.getlist('oc[]')  # Aquí capturamos los valores de OC
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

    # Obtener el área y el nombre del usuario logueado
    area_usuario = session['empleado_area']
    nombre_usuario = session['empleado_nombre']

    # Consulta para obtener las requisiciones
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

    # Obtener los datos de la requisición principal
    id = request.form["id"]
    fecha = request.form["fecha"]
    usuario = session['empleado_nombre']
    descripcion = request.form["descripcion_general"]
    proceso = request.form.get("proceso") or None
    prioridad = request.form.get("prioridad") or None
    eta = request.form.get("eta") or None
    facturas = request.form.get("facturas") or None

    # Actualizar la requisición principal
    controlador_req.actualizar_requisicion(
        id, fecha, usuario, descripcion, None, None, None, proceso, prioridad, eta, facturas
    )

    # Manejar los ítems
    item_ids = request.form.getlist('item_id[]')  # Asegúrate de recibir todos los IDs de los ítems
    descripciones = request.form.getlist('descripcion[]')
    marcas = request.form.getlist('marca[]')
    modelos = request.form.getlist('modelo[]')
    cantidades = request.form.getlist('cantidad[]')
    udms = request.form.getlist('udm[]')
    proveedores = request.form.getlist('proveedor[]')
    ocs = request.form.getlist('oc[]')
    imagenes = request.files.getlist('imagen[]')

    for i in range(len(item_ids)):
        # Si hay una imagen nueva, guárdala
        nueva_imagen = guardar_archivo(imagenes[i]) if imagenes[i].filename != '' else None

        # Si no hay una nueva imagen, conservar la existente
        imagen_actual = controlador_req.obtener_item_por_id(item_ids[i])['imagen'] if nueva_imagen is None else nueva_imagen

        # Actualizar el ítem
        controlador_req.actualizar_item(
            id=item_ids[i],  # Aquí utilizamos los IDs obtenidos del formulario
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

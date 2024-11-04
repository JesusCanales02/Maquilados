# # from flask import Flask, render_template, request, redirect, flash
# # from flask import Flask, render_template, request, redirect, url_for, flash

# # import controlador_req

# # app = Flask(__name__)

# # @app.route("/agregar_req")
# # def formulario_agregar_req():
# #     return render_template("agregar_req.html")

# # @app.route("/recibo")
# # def formulario_recibo():
# #     items = controlador_req.obtener_items() 
# #     return render_template("recibo.html", items=items)

# # @app.route("/entregas")
# # def formulario_entregas():
# #     return render_template("entregas.html")


# # # id, cotizacion, autorizacion, descripcion, proceso, ETA
# # @app.route("/guardar_req", methods=["POST"])
# # def guardar_req():
# #     # Capturamos los valores del contenedor gris 
# #     cotizacion = request.form.get("cotización")
# #     autorizacion = request.form.get("autorización")
# #     estado = request.form.get("estado")
# #     eta = request.form.get("eta")
# #     facturas = request.form.get("facturas")

# #     # Capturamos los ítems de la requisición 
# #     descripciones = request.form.getlist('descripcion[]')
# #     marcas = request.form.getlist('marca[]')
# #     modelos = request.form.getlist('modelo[]')
# #     cantidades = request.form.getlist('cantidad[]')
# #     udms = request.form.getlist('udm[]')
# #     proveedores = request.form.getlist('proveedor[]')
# #     ocs = request.form.getlist('oc[]')

# #     # Aqui se inserta cada ítem en la base de datos
# #     for i in range(len(descripciones)):
# #         descripcion_item = descripciones[i]
# #         marca = marcas[i]
# #         modelo = modelos[i]
# #         cantidad = cantidades[i]
# #         udm = udms[i]
# #         proveedor = proveedores[i]
# #         oc = ocs[i]

# #         controlador_req.insertar_item(None, descripcion_item, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion)
    
# #     return redirect("/requesiciones")

# # @app.route("/")
# # @app.route("/requesiciones")
# # def requesiciones():
# #     requesiciones = controlador_req.obtener_req() 
# #     return render_template("requesiciones.html", requesiciones=requesiciones)

# # @app.route("/eliminar_req", methods=["POST"])
# # def eliminar_req():
# #     controlador_req.eliminar_req(request.form["id"]) 
# #     return redirect("/requesiciones")

# # @app.route("/formulario_editar_req/<int:id>")
# # def editar_req(id):
# #     requesicion = controlador_req.obtener_req_por_id(id) 
# #     return render_template("editar_req.html", requesicion=requesicion)

# # @app.route("/eliminar_item/<int:id>", methods=["POST"])
# # def eliminar_item(id):
# #     controlador_req.eliminar_item(id)  
# #     return redirect(url_for('formulario_recibo')) 

# # @app.route("/editar_item/<int:id>")
# # def editar_item(id):
# #     item = controlador_req.obtener_item_por_id(id)  
# #     return render_template("editar_item.html", item=item)


# # @app.route("/actualizar_req", methods=["POST"])
# # def actualizar_req():
# #     id = request.form["id"]
# #     fecha = request.form["fecha"]
# #     usuario = request.form["usuario"]
# #     descripcion = request.form["descripcion"]
# #     proceso = request.form["proceso"]
# #     ETA = request.form["ETA"]
# #     controlador_req.actualizar_req(id, fecha, usuario, descripcion, proceso, ETA)
# #     return redirect("/requesiciones")

# # # #Para la parte de recibos y pida un dato lo obtendra de la pesta;a de agregar_r
# # @app.route("/recibo", methods=["GET", "POST"])
# # def filtrar_recibo():
# #     oc = request.form.get("oc")
# #     cotizacion = request.form.get("cotizacion")
    
# #     items = controlador_req.obtener_items_filtrados(oc, cotizacion) 
# #     return render_template("recibo.html", items=items)



# # if __name__ == "__main__":
# #     app.run(host='0.0.0.0', port=8000, debug=True)


# # -----------------------------------------------------------------------------------------------------

# from flask import Flask, render_template, request, redirect, flash
# from flask import Flask, render_template, request, redirect, url_for, flash

# import controlador_req

# app = Flask(__name__)

# @app.route("/agregar_req")
# def formulario_agregar_req():
#     return render_template("agregar_req.html")

# @app.route("/recibo")
# def formulario_recibo():
#     items = controlador_req.obtener_items() 
#     return render_template("recibo.html", items=items)

# @app.route("/entregas")
# def formulario_entregas():
#     return render_template("entregas.html")


# # @app.route("/guardar_req", methods=["POST"])
# # def guardar_req():
# #     # Capturamos los valores del formulario (contenedor gris)
# #     fecha = request.form.get("fecha_solicitud")
# #     usuario = request.form.get("solicitante")
# #     descripcion = request.form.get("descripcion_general")
# #     cotizacion = request.form.get("cotizacion")
# #     autorizacion = request.form.get("autorizacion")
# #     oc = request.form.get("oc")
# #     estado = request.form.get("estado")
# #     eta = request.form.get("eta")
# #     facturas = request.form.get("facturas")

# #     # Insertar la requisición en la tabla requisiciones
# #     requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)

# #     # Capturamos los ítems de la requisición (de la tabla de ítems)
# #     descripciones = request.form.getlist('descripcion[]')
# #     marcas = request.form.getlist('marca[]')
# #     modelos = request.form.getlist('modelo[]')
# #     cantidades = request.form.getlist('cantidad[]')
# #     udms = request.form.getlist('udm[]')
# #     proveedores = request.form.getlist('proveedor[]')
# #     ocs = request.form.getlist('oc[]')

# #     # Insertar los ítems en la tabla items
# #     for i in range(len(descripciones)):
# #         descripcion_item = descripciones[i]
# #         marca = marcas[i]
# #         modelo = modelos[i]
# #         cantidad = cantidades[i]
# #         udm = udms[i]
# #         proveedor = proveedores[i]
# #         oc = ocs[i]

# #         # Asociar los ítems con la requisición insertada
# #         controlador_req.insertar_item(requisicion_id, descripcion_item, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion)
    
# #     return redirect("/requesiciones")

# @app.route("/guardar_req", methods=["POST"])
# def guardar_req():
#     # Capturamos los valores del formulario (contenedor gris)
#     fecha = request.form.get("fecha_solicitud")
#     usuario = request.form.get("solicitante")
#     descripcion = request.form.get("descripcion_general")
#     cotizacion = request.form.get("cotizacion")
#     autorizacion = request.form.get("autorizacion")
#     oc = request.form.get("oc")
#     estado = request.form.get("estado")
#     eta = request.form.get("eta")
#     facturas = request.form.get("facturas")

#     # Insertar la requisición y obtener su ID
#     requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)

#     # Capturamos los ítems de la requisición (de la tabla de ítems)
#     descripciones = request.form.getlist('descripcion[]')
#     marcas = request.form.getlist('marca[]')
#     modelos = request.form.getlist('modelo[]')
#     cantidades = request.form.getlist('cantidad[]')
#     udms = request.form.getlist('udm[]')
#     proveedores = request.form.getlist('proveedor[]')
#     ocs = request.form.getlist('oc[]')

#     # Insertar los ítems en la tabla items asociados con la requisición
#     for i in range(len(descripciones)):
#         descripcion_item = descripciones[i]
#         marca = marcas[i]
#         modelo = modelos[i]
#         cantidad = cantidades[i]
#         udm = udms[i]
#         proveedor = proveedores[i]
#         oc = ocs[i]

#         # Insertar cada ítem asociado a la requisición con los mismos valores de cotizacion, autorizacion y oc
#         controlador_req.insertar_item(requisicion_id, descripcion_item, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion)

#     return redirect("/requesiciones")



# @app.route("/")
# @app.route("/requesiciones")
# def requesiciones():
#     requesiciones = controlador_req.obtener_req() 
#     return render_template("requesiciones.html", requesiciones=requesiciones)

# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     controlador_req.eliminar_req(request.form["id"]) 
#     return redirect("/requesiciones")

# @app.route("/formulario_editar_req/<int:id>")
# def editar_req(id):
#     requesicion = controlador_req.obtener_req_por_id(id) 
#     return render_template("editar_req.html", requesicion=requesicion)

# @app.route("/eliminar_item/<int:id>", methods=["POST"])
# def eliminar_item(id):
#     controlador_req.eliminar_item(id)  
#     return redirect(url_for('formulario_recibo')) 

# @app.route("/editar_item/<int:id>")
# def editar_item(id):
#     item = controlador_req.obtener_item_por_id(id)  
#     return render_template("editar_item.html", item=item)


# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     id = request.form["id"]
#     fecha = request.form["fecha"]
#     usuario = request.form["usuario"]
#     descripcion = request.form["descripcion"]
#     proceso = request.form["proceso"]
#     ETA = request.form["ETA"]
#     controlador_req.actualizar_req(id, fecha, usuario, descripcion, proceso, ETA)
#     return redirect("/requesiciones")

# # Para la parte de recibos y filtrar por OC y Cotización
# @app.route("/recibo", methods=["GET", "POST"])
# def filtrar_recibo():
#     oc = request.form.get("oc")
#     cotizacion = request.form.get("cotizacion")
    
#     items = controlador_req.obtener_items_filtrados(oc, cotizacion) 
#     return render_template("recibo.html", items=items)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000, debug=True)


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000, debug=True)


# #------------------------------------------------------------------------------------------
# from flask import Flask, render_template, request, redirect, url_for, flash
# import controlador_req

# app = Flask(__name__)

# @app.route("/agregar_req")
# def formulario_agregar_req():
#     return render_template("agregar_req.html")

# @app.route("/recibo")
# def formulario_recibo():
#     items = controlador_req.obtener_items() 
#     return render_template("recibo.html", items=items)
    

# @app.route("/entregas")
# def formulario_entregas():
#     return render_template("entregas.html")

# # Ruta para guardar una nueva requisición
# @app.route("/guardar_req", methods=["POST"])
# def guardar_req():
#     # Capturamos los valores del formulario
#     fecha = request.form.get("fecha_solicitud")
#     usuario = request.form.get("usuario")
#     descripcion = request.form.get("descripcion_general")
#     cotizacion = request.form.get("cotizacion")
#     autorizacion = request.form.get("autorizacion")
#     oc = request.form.get("oc")
#     estado = request.form.get("estado")
#     eta = request.form.get("eta")
#     facturas = request.form.get("facturas")

#     # Insertar la requisición en la tabla requisiciones
#     requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)

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

# @app.route("/")
# @app.route("/requesiciones")
# def requesiciones():
#     requisiciones = controlador_req.obtener_requisiciones()
#     return render_template("requesiciones.html", requisiciones=requisiciones)

# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/formulario_editar_req/<int:id>")
# def editar_req(id):
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     return render_template("editar_req.html", requisicion=requisicion)

# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     id = request.form["id"]
#     fecha = request.form["fecha"]
#     usuario = request.form["usuario"]
#     descripcion = request.form["descripcion"]
#     cotizacion = request.form["cotizacion"]
#     autorizacion = request.form["autorizacion"]
#     oc = request.form["oc"]
#     estado = request.form["estado"]
#     eta = request.form["eta"]
#     facturas = request.form["facturas"]

#     controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)
#     return redirect("/requesiciones")

# # Ruta para filtrar recibos
# @app.route("/recibo", methods=["GET", "POST"])
# def filtrar_recibo():
#     oc = request.form.get("oc")
#     cotizacion = request.form.get("cotizacion")

#     items = controlador_req.obtener_items_filtrados(oc, cotizacion)
#     return render_template("recibo.html", items=items)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=8000, debug=True)

#-----------------------------------------------------------------------

# from flask import Flask, render_template, request, redirect, url_for, flash, session
# import controlador_req
# from bd import obtener_conexion

# app = Flask(__name__)
# app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para manejar sesiones

# # Ruta principal redirige al login
# @app.route('/')
# def index():
#     if 'empleado_id' in session:  # Si ya hay un empleado logueado
#         return redirect(url_for('requesiciones'))  # Redirigir a requisiciones
#     return redirect(url_for('login'))  # Redirigir al login si no está logueado

# # Ruta para el login
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         no_empleado = request.form['noEmpleado']  # Capturamos el número de empleado
#         # Conectar a la base de datos y verificar el número de empleado en la tabla 'empleado'
#         conexion = obtener_conexion()
#         with conexion.cursor() as cursor:
#             cursor.execute("SELECT * FROM empleado WHERE idEmpleado = %s", (no_empleado,))
#             empleado = cursor.fetchone()  # Verificamos si existe el empleado
        
#         conexion.close()

#         if empleado:
#             session['empleado_id'] = no_empleado  # Guardamos el número de empleado en la sesión
#             return redirect(url_for('requesiciones'))  # Redirige a requisiciones si es correcto
#         else:
#             flash('Número de empleado incorrecto', 'danger')  # Mensaje de error si es incorrecto
#     return render_template('login.html')

# @app.route("/logout")
# def logout():
#     session.pop('empleado_id', None)  # Limpiar la sesión del empleado
#     return redirect(url_for('login'))  # Redirigir al login después de salir

# @app.route("/agregar_req")
# def formulario_agregar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     return render_template("agregar_req.html")

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
#     usuario = request.form.get("usuario")
#     descripcion = request.form.get("descripcion_general")
#     cotizacion = request.form.get("cotizacion")
#     autorizacion = request.form.get("autorizacion")
#     oc = request.form.get("oc")
#     estado = request.form.get("estado")
#     eta = request.form.get("eta")
#     facturas = request.form.get("facturas")

#     # Insertar la requisición en la tabla requisiciones
#     requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)

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
#     requisiciones = controlador_req.obtener_requisiciones()
#     return render_template("requesiciones.html", requisiciones=requisiciones)

# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/formulario_editar_req/<int:id>")
# def editar_req(id):
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     return render_template("editar_req.html", requisicion=requisicion)

# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     id = request.form["id"]
#     fecha = request.form["fecha"]
#     usuario = request.form["usuario"]
#     descripcion = request.form["descripcion"]
#     cotizacion = request.form["cotizacion"]
#     autorizacion = request.form["autorizacion"]
#     oc = request.form["oc"]
#     estado = request.form["estado"]
#     eta = request.form["eta"]
#     facturas = request.form["facturas"]

#     controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)
#     return redirect("/requesiciones")

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
    
#---------------------------------------------------------------- funcional

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
#         no_empleado = request.form['noEmpleado']
#         conexion = obtener_conexion()
#         with conexion.cursor() as cursor:
#             cursor.execute("SELECT * FROM empleado WHERE IdEmpleado = %s", (no_empleado,))
#             empleado = cursor.fetchone()

#         conexion.close()

#         if empleado:
#             session['empleado_id'] = empleado['IdEmpleado']
#             session['empleado_nombre'] = empleado['Nombre']  # Guardamos el nombre del empleado en la sesión
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
#     estado = request.form.get("estado") or None
#     eta = request.form.get("eta") or None
#     facturas = request.form.get("facturas") or None

#     # Insertar la requisición en la tabla requisiciones
#     requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)

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
#     requisiciones = controlador_req.obtener_requisiciones()
#     return render_template("requesiciones.html", requisiciones=requisiciones)

# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/formulario_editar_req/<int:id>")
# def editar_req(id):
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     return render_template("editar_req.html", requisicion=requisicion)

# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     id = request.form["id"]
#     fecha = request.form["fecha"]
#     usuario = session['empleado_nombre']  # Usamos el nombre del usuario de la sesión
#     descripcion = request.form["descripcion"]
#     cotizacion = request.form["cotizacion"] or None
#     autorizacion = request.form["autorizacion"] or None
#     oc = request.form["oc"] or None
#     estado = request.form["estado"] or None
#     eta = request.form["eta"] or None
#     facturas = request.form["facturas"] or None

#     controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)
#     return redirect("/requesiciones")

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
# #---------------------------------------------------------------- por si acaso
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
#             flash('Número de empleado incorrecto o empleado en estado de baja', 'danger')  # Mostrar advertencia
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
#     estado = request.form.get("estado") or None
#     eta = request.form.get("eta") or None
#     facturas = request.form.get("facturas") or None

#     # Insertar la requisición en la tabla requisiciones
#     requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)

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
#     requisiciones = controlador_req.obtener_requisiciones()
#     return render_template("requesiciones.html", requisiciones=requisiciones)

# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/formulario_editar_req/<int:id>")
# def editar_req(id):
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     return render_template("editar_req.html", requisicion=requisicion)

# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     id = request.form["id"]
#     fecha = request.form["fecha"]
#     usuario = session['empleado_nombre']  # Usamos el nombre del usuario de la sesión
#     descripcion = request.form["descripcion"]
#     cotizacion = request.form["cotizacion"] or None
#     autorizacion = request.form["autorizacion"] or None
#     oc = request.form["oc"] or None
#     estado = request.form["estado"] or None
#     eta = request.form["eta"] or None
#     facturas = request.form["facturas"] or None

#     controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)
#     return redirect("/requesiciones")

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
#------------------------------------------------------------------------------------------------------Si funciona

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
#             flash('Número de empleado incorrecto o empleado en estado de baja', 'danger')  # Mostrar advertencia
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
#     estado = request.form.get("estado") or None
#     eta = request.form.get("eta") or None
#     facturas = request.form.get("facturas") or None

#     # Insertar la requisición en la tabla requisiciones
#     requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)

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

#     # Consulta para obtener las requisiciones y asociar el área correcta basada en el IdArea
#     with conexion.cursor() as cursor:
#         cursor.execute("""
#             SELECT r.id, r.fecha, a.NombreArea AS area, r.usuario, r.descripcion, r.ETA 
#             FROM requisiciones r
#             JOIN empleado e ON r.usuario = e.Nombre  -- Relacionamos con la tabla empleado
#             JOIN area a ON e.IdArea = a.IdArea  -- Relacionamos el área desde la tabla empleado
#         """)
#         requisiciones = cursor.fetchall()

#     conexion.close()

#     return render_template("requesiciones.html", requisiciones=requisiciones)



# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/formulario_editar_req/<int:id>")
# def editar_req(id):
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     return render_template("editar_req.html", requisicion=requisicion)

# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     id = request.form["id"]
#     fecha = request.form["fecha"]
#     usuario = session['empleado_nombre']  # Usamos el nombre del usuario de la sesión
#     descripcion = request.form["descripcion"]
#     cotizacion = request.form["cotizacion"] or None
#     autorizacion = request.form["autorizacion"] or None
#     oc = request.form["oc"] or None
#     estado = request.form["estado"] or None
#     eta = request.form["eta"] or None
#     facturas = request.form["facturas"] or None

#     controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)
#     return redirect("/requesiciones")

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
#------------------------------------------------------------------------------------------Este es el bueno 
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
#             flash('Número de empleado incorrecto o empleado en estado de baja', 'danger')  # Mostrar advertencia
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

#     # Consulta para obtener las requisiciones y asociar el área correcta basada en el IdArea
#     with conexion.cursor() as cursor:
#         cursor.execute("""
#             SELECT r.id, r.fecha, a.NombreArea AS area, r.usuario, r.descripcion, r.proceso, r.ETA 
#             FROM requisiciones r
#             JOIN empleado e ON r.usuario = e.Nombre  -- Relacionamos con la tabla empleado
#             JOIN area a ON e.IdArea = a.IdArea  -- Relacionamos el área desde la tabla empleado
#         """)
#         requisiciones = cursor.fetchall()

#     conexion.close()

#     return render_template("requesiciones.html", requisiciones=requisiciones)



# @app.route("/eliminar_req", methods=["POST"])
# def eliminar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     controlador_req.eliminar_requisicion(request.form["id"])
#     return redirect("/requesiciones")

# @app.route("/formulario_editar_req/<int:id>")
# def editar_req(id):
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     requisicion = controlador_req.obtener_requisicion_por_id(id)
#     return render_template("editar_req.html", requisicion=requisicion)

# @app.route("/actualizar_req", methods=["POST"])
# def actualizar_req():
#     if 'empleado_id' not in session:  # Verificar si el usuario está logueado
#         return redirect(url_for('login'))  # Si no, redirigir al login
#     id = request.form["id"]
#     fecha = request.form["fecha"]
#     usuario = session['empleado_nombre']  # Usamos el nombre del usuario de la sesión
#     descripcion = request.form["descripcion"]
#     cotizacion = request.form["cotizacion"] or None
#     autorizacion = request.form["autorizacion"] or None
#     oc = request.form["oc"] or None
#     proceso = request.form["proceso"] or None
#     eta = request.form["eta"] or None
#     facturas = request.form["facturas"] or None

#     controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, eta, facturas)
#     return redirect("/requesiciones")

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
#------------------------------------------------------------------------------- si sirve este muy bien

from flask import Flask, render_template, request, redirect, url_for, flash, session
import controlador_req
from bd import obtener_conexion

app = Flask(__name__)
app.secret_key = 'tu_clave_secreta_aqui'  # Necesario para manejar sesiones

# Ruta principal redirige al login
@app.route('/')
def index():
    return redirect(url_for('login'))

# Ruta para el login
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

        if empleado and empleado['Estatus'] != 'BAJA':  # Verificar que el empleado no esté en BAJA
            session['empleado_id'] = empleado['IdEmpleado']
            session['empleado_nombre'] = empleado['Nombre']
            session['empleado_area'] = empleado['NombreArea']  # Guardar el área en la sesión
            return redirect(url_for('requesiciones'))  # Redirigir a la página de requisiciones
        else:
            flash('Número de empleado incorrecto', 'danger')  # Mostrar advertencia
    return render_template('login.html')


@app.route("/agregar_req")
def formulario_agregar_req():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))
    return render_template("agregar_req.html", usuario=session['empleado_nombre'])

@app.route("/logout")
def logout():
    session.pop('empleado_id', None)  # Limpiar la sesión del empleado
    session.pop('empleado_nombre', None)  # Limpiar el nombre del empleado en la sesión
    return redirect(url_for('login'))  # Redirigir al login después de salir

@app.route("/recibo")
def formulario_recibo():
    if 'empleado_id' not in session:  # Verificar si el usuario está logueado
        return redirect(url_for('login'))  # Si no, redirigir al login
    items = controlador_req.obtener_items()
    return render_template("recibo.html", items=items)

@app.route("/entregas")
def formulario_entregas():
    if 'empleado_id' not in session:  # Verificar si el usuario está logueado
        return redirect(url_for('login'))  # Si no, redirigir al login
    return render_template("entregas.html")

# Ruta para guardar una nueva requisición
@app.route("/guardar_req", methods=["POST"])
def guardar_req():
    if 'empleado_id' not in session:  # Verificar si el usuario está logueado
        return redirect(url_for('login'))  # Si no, redirigir al login

    # Capturamos los valores del formulario
    fecha = request.form.get("fecha_solicitud")
    usuario = session['empleado_nombre']  # Usamos el nombre del usuario de la sesión
    descripcion = request.form.get("descripcion_general")
    cotizacion = request.form.get("cotizacion") or None
    autorizacion = request.form.get("autorizacion") or None
    oc = request.form.get("oc") or None
    proceso = request.form.get("proceso") or None
    eta = request.form.get("eta") or None
    facturas = request.form.get("facturas") or None

    # Insertar la requisición en la tabla requisiciones
    requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, eta, facturas)

    # Capturamos los ítems de la requisición
    descripciones = request.form.getlist('descripcion[]')
    marcas = request.form.getlist('marca[]')
    modelos = request.form.getlist('modelo[]')
    cantidades = request.form.getlist('cantidad[]')
    udms = request.form.getlist('udm[]')
    proveedores = request.form.getlist('proveedor[]')
    ocs = request.form.getlist('oc[]')

    # Insertar los ítems en la tabla items asociados con la requisición
    for i in range(len(descripciones)):
        controlador_req.insertar_item(requisicion_id, descripciones[i], marcas[i], modelos[i], cantidades[i], udms[i], proveedores[i], ocs[i], cotizacion, autorizacion)

    return redirect("/requesiciones")

@app.route("/requesiciones")
def requesiciones():
    if 'empleado_id' not in session:  # Verificar si el usuario está logueado
        return redirect(url_for('login'))  # Si no, redirigir al login

    conexion = obtener_conexion()
    requisiciones = []

    # Obtener el área y el nombre del usuario logueado
    area_usuario = session['empleado_area']
    nombre_usuario = session['empleado_nombre']

    # Consulta para obtener las requisiciones de la misma área y que no estén en estado de baja
    with conexion.cursor() as cursor:
        cursor.execute("""
            SELECT r.id, r.fecha, a.NombreArea AS area, r.usuario, r.descripcion, r.proceso, r.ETA 
            FROM requisiciones r
            JOIN empleado e ON r.usuario = e.Nombre  -- Relacionamos con la tabla empleado
            JOIN area a ON e.IdArea = a.IdArea  -- Relacionamos el área desde la tabla empleado
            WHERE a.NombreArea = %s AND e.Estatus != 'BAJA'  -- Filtramos por área y que no estén de baja
        """, (area_usuario,))
        requisiciones = cursor.fetchall()

    conexion.close()

    # Pasar el nombre del usuario al contexto de la plantilla
    return render_template("requesiciones.html", requisiciones=requisiciones, usuario=nombre_usuario)




@app.route("/eliminar_req", methods=["POST"])
def eliminar_req():
    if 'empleado_id' not in session:  # Verificar si el usuario está logueado
        return redirect(url_for('login'))  # Si no, redirigir al login
    controlador_req.eliminar_requisicion(request.form["id"])
    return redirect("/requesiciones")

@app.route("/editar_req/<int:id>")
def editar_req(id):
    if 'empleado_id' not in session:
        return redirect(url_for('login'))
    requisicion = controlador_req.obtener_requisicion_por_id(id)
    items = controlador_req.obtener_items_por_requisicion(id)
    return render_template("editar_req.html", requisicion=requisicion, items=items)



@app.route("/actualizar_req", methods=["POST"])
def actualizar_req():
    if 'empleado_id' not in session:
        return redirect(url_for('login'))
    
    try:
        id = request.form["id"]
        fecha = request.form["fecha"]
        usuario = session['empleado_nombre']
        descripcion = request.form["descripcion_general"]
        cotizacion = request.form.get("cotizacion") or None
        autorizacion = request.form.get("autorizacion") or None
        oc = request.form.get("oc") or None
        proceso = request.form.get("proceso") or None
        eta = request.form.get("eta") or None
        facturas = request.form.get("facturas") or None

        # Lógica para actualizar en la base de datos
        controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, proceso, eta, facturas)
        return redirect("/requesiciones")
    except KeyError as e:
        flash(f"Error: campo '{e.args[0]}' no encontrado en el formulario.", "danger")
        return redirect(url_for('formulario_editar_req', id=id))


# Ruta para filtrar recibos
@app.route("/recibo", methods=["GET", "POST"])
def filtrar_recibo():
    if 'empleado_id' not in session:  # Verificar si el usuario está logueado
        return redirect(url_for('login'))  # Si no, redirigir al login
    oc = request.form.get("oc")
    cotizacion = request.form.get("cotizacion")

    items = controlador_req.obtener_items_filtrados(oc, cotizacion)
    return render_template("recibo.html", items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

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
from flask import Flask, render_template, request, redirect, url_for, flash
import controlador_req

app = Flask(__name__)

@app.route("/agregar_req")
def formulario_agregar_req():
    return render_template("agregar_req.html")

@app.route("/recibo")
def formulario_recibo():
    items = controlador_req.obtener_items() 
    return render_template("recibo.html", items=items)
    

@app.route("/entregas")
def formulario_entregas():
    return render_template("entregas.html")

# Ruta para guardar una nueva requisición
@app.route("/guardar_req", methods=["POST"])
def guardar_req():
    # Capturamos los valores del formulario
    fecha = request.form.get("fecha_solicitud")
    usuario = request.form.get("usuario")
    descripcion = request.form.get("descripcion_general")
    cotizacion = request.form.get("cotizacion")
    autorizacion = request.form.get("autorizacion")
    oc = request.form.get("oc")
    estado = request.form.get("estado")
    eta = request.form.get("eta")
    facturas = request.form.get("facturas")

    # Insertar la requisición en la tabla requisiciones
    requisicion_id = controlador_req.insertar_requisicion(fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)

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

@app.route("/")
@app.route("/requesiciones")
def requesiciones():
    requisiciones = controlador_req.obtener_requisiciones()
    return render_template("requesiciones.html", requisiciones=requisiciones)

@app.route("/eliminar_req", methods=["POST"])
def eliminar_req():
    controlador_req.eliminar_requisicion(request.form["id"])
    return redirect("/requesiciones")

@app.route("/formulario_editar_req/<int:id>")
def editar_req(id):
    requisicion = controlador_req.obtener_requisicion_por_id(id)
    return render_template("editar_req.html", requisicion=requisicion)

@app.route("/actualizar_req", methods=["POST"])
def actualizar_req():
    id = request.form["id"]
    fecha = request.form["fecha"]
    usuario = request.form["usuario"]
    descripcion = request.form["descripcion"]
    cotizacion = request.form["cotizacion"]
    autorizacion = request.form["autorizacion"]
    oc = request.form["oc"]
    estado = request.form["estado"]
    eta = request.form["eta"]
    facturas = request.form["facturas"]

    controlador_req.actualizar_requisicion(id, fecha, usuario, descripcion, cotizacion, autorizacion, oc, estado, eta, facturas)
    return redirect("/requesiciones")

# Ruta para filtrar recibos
@app.route("/recibo", methods=["GET", "POST"])
def filtrar_recibo():
    oc = request.form.get("oc")
    cotizacion = request.form.get("cotizacion")

    items = controlador_req.obtener_items_filtrados(oc, cotizacion)
    return render_template("recibo.html", items=items)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)

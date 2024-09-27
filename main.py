from flask import Flask, render_template, request, redirect, flash
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


# id, cotizacion, autorizacion, descripcion, proceso, ETA
@app.route("/guardar_req", methods=["POST"])
def guardar_req():
    # Capturamos los valores del contenedor gris 
    cotizacion = request.form.get("cotización")
    autorizacion = request.form.get("autorización")
    estado = request.form.get("estado")
    eta = request.form.get("eta")
    facturas = request.form.get("facturas")

    # Capturamos los ítems de la requisición 
    descripciones = request.form.getlist('descripcion[]')
    marcas = request.form.getlist('marca[]')
    modelos = request.form.getlist('modelo[]')
    cantidades = request.form.getlist('cantidad[]')
    udms = request.form.getlist('udm[]')
    proveedores = request.form.getlist('proveedor[]')
    ocs = request.form.getlist('oc[]')

    # Aqui se inserta cada ítem en la base de datos
    for i in range(len(descripciones)):
        descripcion_item = descripciones[i]
        marca = marcas[i]
        modelo = modelos[i]
        cantidad = cantidades[i]
        udm = udms[i]
        proveedor = proveedores[i]
        oc = ocs[i]

        controlador_req.insertar_item(None, descripcion_item, marca, modelo, cantidad, udm, proveedor, oc, cotizacion, autorizacion)
    
    return redirect("/requesiciones")

@app.route("/")
@app.route("/requesiciones")
def requesiciones():
    requesiciones = controlador_req.obtener_req() 
    return render_template("requesiciones.html", requesiciones=requesiciones)

@app.route("/eliminar_req", methods=["POST"])
def eliminar_req():
    controlador_req.eliminar_req(request.form["id"]) 
    return redirect("/requesiciones")

@app.route("/formulario_editar_req/<int:id>")
def editar_req(id):
    requesicion = controlador_req.obtener_req_por_id(id) 
    return render_template("editar_req.html", requesicion=requesicion)

@app.route("/eliminar_item/<int:id>", methods=["POST"])
def eliminar_item(id):
    controlador_req.eliminar_item(id)  
    return redirect(url_for('formulario_recibo')) 

@app.route("/editar_item/<int:id>")
def editar_item(id):
    item = controlador_req.obtener_item_por_id(id)  
    return render_template("editar_item.html", item=item)


@app.route("/actualizar_req", methods=["POST"])
def actualizar_req():
    id = request.form["id"]
    fecha = request.form["fecha"]
    usuario = request.form["usuario"]
    descripcion = request.form["descripcion"]
    proceso = request.form["proceso"]
    ETA = request.form["ETA"]
    controlador_req.actualizar_req(id, fecha, usuario, descripcion, proceso, ETA)
    return redirect("/requesiciones")

# #Para la parte de recibos y pida un dato lo obtendra de la pesta;a de agregar_r
@app.route("/recibo", methods=["GET", "POST"])
def filtrar_recibo():
    oc = request.form.get("oc")
    cotizacion = request.form.get("cotizacion")
    
    items = controlador_req.obtener_items_filtrados(oc, cotizacion) 
    return render_template("recibo.html", items=items)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
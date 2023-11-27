from flask import Flask, render_template, request, redirect, url_for
from referenciales.ciudad.CiudadDAO import ciudadDao
from referenciales.cargo.CargoDAO import CargosDao
from referenciales.pais.PaisDAO import paisDao
from referenciales.grado.GradoDAO import GradoDao
from referenciales.personas.PersonasDAO import personasDAO

app = Flask(__name__)


#MENU PRINCIPAL
@app.route('/')
def menu_principal():
    return render_template('modulo_views/index.html')

#TABLAS
@app.route('/tablas')
def menu_tablas():
    return render_template('Vista_tablas/index.html')

#LOGIN
@app.route('/login')
def login():
    return render_template('login_views/login.html')

@app.route('/register')
def register():
    return render_template('login_views/register.html')

@app.route('/recuperar')
def recuperar():
    return render_template('login_views/recuperar.html')

@app.route('/ayuda')
def ayuda():
    return render_template('login_views/ayuda.html')


#REFERENCIAL - CIUDADES
cdao=ciudadDao()
@app.route('/ciudades')
def index():
    return render_template('/mantenimiento_views/ciudadViews/index.html', lista_ciudades = cdao.getCiudades())

@app.route('/add-ciudad')
def add_ciudad():
    return render_template('/mantenimiento_views/ciudadViews/form-add.html')


@app.route('/save-ciudad', methods=['POST'])
def save_ciudad():
    txtciudad = request.form['txtciudad']
    guardado = False
    if txtciudad != None and len(txtciudad.strip()) > 0:
        guardado = cdao.insertCiudad(txtciudad.strip().upper())
    if guardado:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('add_ciudad'))


@app.route('/eliminar-ciudad/<idciudad>')
def eliminar_ciudad(idciudad):
    cdao.deleteCiudad(idciudad)
    return redirect(url_for('index'))

@app.route('/edit-ciudad/<idciudad>')
def edit_ciudad(idciudad):
    diccionario_ciudad = cdao.getCiudadesById(idciudad)
    return render_template('/mantenimiento_views/ciudadViews/form-edit.html' , ciudad = diccionario_ciudad)

@app.route('/update-ciudad', methods=['POST'])
def update_ciudad():
    idciudad = request.form['idtxtciudad']
    txtciudad = request.form['txtciudad']
    guardado = False
    if txtciudad != None and len(txtciudad.strip()) > 0:
        guardado = cdao.updateCiudad(idciudad,txtciudad.strip().upper())
    if guardado:
        return redirect(url_for('index'))
    else:
        return redirect(url_for('edit_ciudad', idciudad=idciudad))



#REFERENCIAL CARGOS
@app.route('/cargos')
def indexCg():
    cadao = CargosDao()
    return render_template('/mantenimiento_views/CargosViews/index.html', lista_cargos = cadao.getCargos())

@app.route('/add-cargo')
def add_cargo():
    return render_template('/mantenimiento_views/CargosViews/form-add.html')

@app.route('/save-cargo', methods=['POST'])
def save_cargos():
    cadao = CargosDao()

    txtcargo = request.form['txt-cargo']
    guardado = False
    if txtcargo != None and len(txtcargo.strip()) > 0:
        guardado = cadao.insertCargos(txtcargo.strip().upper())
    if guardado:
        return redirect(url_for('indexCg'))
    else:
        return redirect(url_for('add_cargo'))



#REFERENCIAL PAIS
@app.route('/paises')
def paisex():
    padao = paisDao()
    return render_template('/mantenimiento_views/PaisViews/index.html', lista_paises = padao.getPaises())

@app.route('/add-paises')
def add_pais():
    return render_template('/mantenimiento_views/PaisViews/form-add.html')

@app.route('/save-pais', methods=['POST'])
def save_pais():
    print(request.form)
    return redirect(url_for('paisex'))

#REFERENCIAL GRADO ACADEMICO
@app.route('/grados')
def grados():
    gadao = GradoDao()
    return render_template('/mantenimiento_views/gradoViews/grado.html', tuplas_grado = gadao.getGrado())

#REFERENCIAL PERSONAS
@app.route('/personas')
def personas():
    pedao = personasDAO()
    return render_template('/mantenimiento_views/Personaviews/persona.html', lista_personas = pedao.getPersonas())

@app.route('/add-personas')
def add_personas():
    lista_ciudades = cdao.getCiudades()
    padao = paisDao()
    lista_paises = padao.getPaises()
    return render_template('/mantenimiento_views/Personaviews/form-add.html', lista_ciudades = lista_ciudades, lista_paises = lista_paises)

@app.route('/save-personas', methods=['POST'])
def save_personas():
    pedao = personasDAO()
    txtcedula = request.form['txtcedula']
    txtnombre = request.form['txtnombre']
    txtapellido = request.form['txtapellido']
    txtfecha = request.form['txtfecha']
    txtdireccion = request.form['txtdireccion']
    txttelefono = request.form['txttelefono']
    txtciudad = request.form['txtciudad']
    txtpais = request.form['txtpais']
    guardado = False
    if txtcedula and txtnombre and txtapellido and txtfecha and txtdireccion and txttelefono and txtciudad and txtpais != None and len(txtcedula.strip()) > 0:
        guardado = pedao.insertPersonas(txtcedula.strip().upper(), txtnombre.strip().upper(),
                                        txtapellido.strip().upper(), txtfecha.strip().upper(), txtdireccion.strip().upper(), txttelefono.strip().upper(),
                                        txtciudad.strip().upper(), txtpais.strip().upper())

    #if txtnombre != None and len(txtnombre.strip()) > 0:
     #   guardado = pedao.insertPersonas(txtnombre.strip().upper())

    #if txtapellido != None and len(txtapellido.strip()) > 0:
     #   guardado = pedao.insertPersonas(txtapellido.strip().upper())

    #if txtfecha != None and len(txtfecha.strip()) > 0:
    #    guardado = pedao.insertPersonas(txtfecha.strip())

    #if txtdireccion != None and len(txtdireccion.strip()) > 0:
    #    guardado = pedao.insertPersonas(txtdireccion.strip())

   # if txttelefono != None and len(txttelefono.strip()) > 0:
    #    guardado = pedao.insertPersonas(txttelefono.strip())

   # if txtciudad != None and len(txtciudad.strip()) > 0:
    #    guardado = pedao.insertPersonas(txtciudad.strip())

  #  if txtpais != None and len(txtpais.strip()) > 0:
   #     guardado = pedao.insertPersonas(txtpais.strip())

    if guardado:
        return redirect(url_for('personas'))
    else:
        return redirect(url_for('add_personas'))




if __name__ == '__main__':
    app.run(debug=True)
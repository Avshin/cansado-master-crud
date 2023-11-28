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

@app.route('/eliminar-cargo/<idcargo>')
def eliminar_cargo(idcargo):
    cadao = CargosDao()
    cadao.deleteCargo(idcargo)
    return redirect(url_for('indexCg'))


@app.route('/edit-cargo/<idcargo>')
def edit_cargo(idcargo):
    cadao = CargosDao()
    diccionario_cargo = cadao.getCargosById(idcargo)
    return render_template('/mantenimiento_views/CargosViews/form-edit.html' , cargos = diccionario_cargo)

@app.route('/update-cargo', methods=['POST'])
def update_cargo():
    print(request.form)
    cadao = CargosDao()
    idcargo = request.form['txtidcargos']
    txtcargos = request.form['txtcargos']
    guardado = False
    if txtcargos != None and len(txtcargos.strip()) > 0:
        guardado = cadao.updateCargos(idcargo,txtcargos.strip().upper())
    if guardado:
        return redirect(url_for('indexCg'))
    else:
        return redirect(url_for('edit_cargo', idcargo=idcargo))




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
    padao = paisDao()
    print(request.form)
    txtpais = request.form['txtpais']
    guardado = False
    if txtpais != None and len(txtpais.strip()) > 0:
        guardado = padao.insertPais(txtpais.strip().upper())
    if guardado:
        return redirect(url_for('paisex'))
    else:
        return redirect(url_for('add_pais'))


@app.route('/eliminar-pais/<idpais>')
def eliminar_pais(idpais):
    padao = paisDao()
    padao.deletePais(idpais)
    return redirect(url_for('paisex'))



@app.route('/edit-pais/<idpais>')
def edit_pais(idpais):
    padao = paisDao()
    diccionario_pais = padao.getPaisById(idpais)
    return render_template('/mantenimiento_views/PaisViews/form-edit.html' , pais = diccionario_pais)

@app.route('/update-pais', methods=['POST'])
def update_pais():
    print(request.form)
    padao = paisDao()
    idpais = request.form['idtxtpais']
    txtpais = request.form['txtpais']
    guardado = False
    if txtpais != None and len(txtpais.strip()) > 0:
        guardado = padao.updatePais(idpais,txtpais.strip().upper())
    if guardado:
        return redirect(url_for('paisex'))
    else:
        return redirect(url_for('edit_cargo', idpais=idpais))



#REFERENCIAL GRADO ACADEMICO
@app.route('/grados')
def grados():
    gadao = GradoDao()
    return render_template('/mantenimiento_views/gradoViews/grado.html', tuplas_grado = gadao.getGrado())

@app.route('/add-grado')
def add_grado():
    return render_template('/mantenimiento_views/gradoViews/form-add.html')

@app.route('/save-grado', methods=['POST'])
def save_grado():
    gadao = GradoDao()
    print(request.form)
    txtgrado = request.form['txtgrado']
    guardado = False
    if txtgrado != None and len(txtgrado.strip()) > 0:
        guardado = gadao.insertGrado(txtgrado.strip().upper())
    if guardado:
        return redirect(url_for('grados'))
    else:
        return redirect(url_for('add_grado'))

@app.route('/eliminar-grado/<idgrado>')
def eliminar_grado(idgrado):
    gadao = GradoDao()
    gadao.deleteGrado(idgrado)
    return redirect(url_for('grados'))


@app.route('/edit-grado/<idgrado>')
def edit_grado(idgrado):
    gadao = GradoDao()
    diccionario_grado = gadao.getGradoById(idgrado)
    return render_template('/mantenimiento_views/gradoViews/edit-form.html', grado =  diccionario_grado)


@app.route('/update-grado', methods=['POST'])
def update_grado():
    print(request.form)
    gadao = GradoDao()
    idgrado = request.form['idtxtgrado']
    txtgrado = request.form['txtgrado']
    guardado = False
    if txtgrado != None and len(txtgrado.strip()) > 0:
        guardado = gadao.updateGrado(idgrado,txtgrado.strip().upper())
    if guardado:
        return redirect(url_for('grados'))
    else:
        return redirect(url_for('edit_grado', idgrado=idgrado))



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

    if guardado:
        return redirect(url_for('personas'))
    else:
        return redirect(url_for('add_personas'))


@app.route('/eliminar-persona/<idpersona>')
def eliminar_persona(idpersona):
    pedao = personasDAO()
    pedao.deletePersona(idpersona)
    return redirect(url_for('personas'))




@app.route('/edit-persona/<idpersona>')
def edit_persona(idpersona):
    pedao = personasDAO()
    lista_ciudades = cdao.getCiudades()
    padao = paisDao()
    diccionario_persona = pedao.getPersonatById(idpersona)
    return render_template('/mantenimiento_views/PersonaViews/form-edit.html', lista_paises = padao.getPaises(), lista_ciudades = cdao.getCiudades(), persona =  diccionario_persona)


@app.route('/update-persona', methods=['POST'])
def update_persona():
    print(request.form)
    pedao = personasDAO()
    txtidpersona = request.form['txtidpersona']
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
    if guardado:
        return redirect(url_for('personas'))
    else:
        return redirect(url_for('edit_persona', idpersona = txtidpersona))







if __name__ == '__main__':
    app.run(debug=True)
from flask import Flask, render_template, request, redirect, url_for
from referenciales.ciudad.CiudadDAO import ciudadDao
from referenciales.cargo.CargoDAO import CargosDao
from referenciales.pais.PaisDAO import paisDao

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


#REFERENCIAL - CIUDADES
@app.route('/ciudades')
def index():
    cdao = ciudadDao()
    lista = cdao.getCiudades()
    diccionario = []
    if len (lista) >0:
        for item in lista:
            diccionario.append(
                {
                    'id_ciudad': item[0],
                    'detalle_ciudad': item[1]
                }
            )
    return render_template('/mantenimiento_views/CiudadViews/index.html', ciudades=diccionario)


@app.route('/add-ciudad')
def add_ciudad():
    cdao = ciudadDao()
    txtciudad = request.form['txtciudad']
    guardado = False
    if txtciudad != None and len(txtciudad.strip()) > 0:
        guardado = cdao.insertCiudad(txtciudad.strip().upper())
    if guardado:
        return redirect(url_for('index'))
    else:
        return redirect(url_for(add_ciudad))

@app.route('/save-ciudad', methods=['POST'])
def save_ciudad():
    print(request.form)
    return redirect(url_for('index'))



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
    print(request.form)
    return redirect(url_for('indexCg'))



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


if __name__ == '__main__':
    app.run(debug=True)
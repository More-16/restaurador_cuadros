from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Cadena de conexión a MySQL usando PyMySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://morenasalamonini:S4lam0nini@localhost:3306/mi_base'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)


# Modelo de tabla
class Cliente(db.Model):
    __tablename__ = 'Cliente'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    dni = db.Column(db.Integer)
    numero = db.Column(db.Integer)
class Empleado(db.Model):
    __tablename__ = 'Empleado'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    nacimiento = db.Column(db.Date )
    dni = db.Column(db.Integer)
    numero = db.Column(db.Integer)
class CUADRO(db.Model):
    __tablename__ = 'CUADRO'
    id = db.Column(db.Integer, primary_key=True)
    Titulo = db.Column(db.String(50))
    autor = db.Column(db.String(50))
    año = db.Column(db.Integer)
    altura = db.Column(db.Integer)
    Ancho = db.Column(db.Integer)
class venta(db.Model):
    __tablename__ = 'venta'
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer)
    empleado_id = db.Column(db.Integer)
    CUADRO_id = db.Column(db.Integer)
    estado_actual = db.Column(db.String(200) )
    servicio = db.Column(db.String(200) )
    fecha_entrada = db.Column(db.Date )
    fecha_entrega_estimada = db.Column(db.Date)
cliente = db.relationship('Cliente', backref=db.backref('venta', lazy=True))
empleado = db.relationship('Empleado', backref=db.backref('venta', lazy=True))
cuadro = db.relationship('cuadro', backref=db.backref('venta', lazy=True))

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/clientes')
def clientes():
    return render_template('clientes.html')
@app.route('/empleados')
def empleados():
    return render_template('empleados.html')
@app.route('/cuadros')
def cuadros():
    return render_template('cuadros.html')
@app.route('/ventas')
def ventas():
    return render_template('ventas.html')


if __name__ == '__main__':
    app.run(debug=True)


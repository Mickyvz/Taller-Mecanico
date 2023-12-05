from flask import Flask, render_template, url_for, request

# app es una variable, se crea una instancia 
# Flask (argumento)
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


# Se crea una ruta
@app.route('/verlogin')
def verlogin():
   return render_template('html/login.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
    return f"Correo Electronico: {email}, Contraseña: {password}"
    


@app.route('/registrar')
def registrar():
    return render_template('html/signup.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        tel = request.form['tel']
        email = request.form['email']
        passwrd = request.form['passwrd']
        rtpassword = request.form['rtpassword']
    return f"Su nombre es: {name}, Telefono: {tel}, Su correo es: {email}, Su contraseña: {passwrd}, Verificar si esta bien su contraseña: {rtpassword}"


@app.route('/promociones/<promociones>')
def promociones(promociones):
    return promociones

@app.route('/servicios/<servicios>')
def servicios(servicios):
    return servicios

@app.route('/about')
def about():
    return render_template('html/about.html')

if __name__ == '__main__':
    app.run(debug=True)


from flask import Flask, redirect, render_template, request, url_for
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.secret_key = "secret_key"   # Flask WTF

csrf = CSRFProtect()

@app.route("/")
def index():
    return render_template('index.html')

# CSRF: Solicitud de informacion entre otros sitios - Flask WTF
@app.route("/login", methods=['GET', 'POST'])
def login():
    #print(request.method)
    if request.method == "POST": 
        if request.form['usuario'] == 'admin1' and request.form['password'] == '123456':
        #print(request.form['usuario'])
        #print(request.form['password'])
            return redirect(url_for('index'))
        else:
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404

if __name__ == '__main__':  
    app.register_error_handler(404, pagina_no_encontrada)   # Manejador de errores
    csrf.init_app(app)  # Proteccion contra ataques
    app.run(debug=True, port=5005)  

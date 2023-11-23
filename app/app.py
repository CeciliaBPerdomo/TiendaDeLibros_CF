from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

def pagina_no_encontrada(error):
    return render_template('errores/404.html'), 404

if __name__ == '__main__':  
    app.register_error_handler(404, pagina_no_encontrada)   # Manejador de errores
    app.run(debug=True, port=5005)  

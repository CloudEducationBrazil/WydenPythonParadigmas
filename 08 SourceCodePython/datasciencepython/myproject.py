# pip install Flask
# pip install gunicorn
# routes, functions, templates
# Procfile # web: gunicorn myproject:app
# pip freeze > requirements.txt # depois de instalado gunicorn

from flask import Flask, render_template

app = Flask(__name__)

# route/Function
@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/contatos")
def contatos():
    return render_template("contatos.html")

@app.route("/usuarios/<nome_user>,<celular>")
def usuarios(nome_user, celular):
    return render_template("usuarios.html", nome_user = nome_user, celular=celular)

if __name__ == "__main__":
  app.run(debug=True)
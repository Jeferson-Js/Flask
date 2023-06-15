# Criando uma api com flask

> Faça o import do flask

````
pip install flask
````
````
from flask import Flask, render_templates

app = Flask(__name__)

@app.route("/")
def index():
  return render_templates("index.html")
  
if __name__ == "__main__":
      app.run(port=5000, host="localhost", debug=True)
````
> Para rodar a aplicação basta copiar o comando abaixo em seu terminal e precionar ENTER
````
python main.py 
````
> Resultado da aplicação

![resultado](https://github.com/Jeferson-Js/Flask/assets/82729145/cda81b51-3d53-4fda-87c6-09e4ecb3b650)

[Tecnologias utilizadas](#tecnologias-utilizadas%color=green)
> 🔨 Python<br>
> 🔨 Flask<br>
> 🔨 Html5

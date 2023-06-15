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
[Tecnologias utilizadas](#tecnologias-utilizadas%color=green)
🔨 Python
🔨 Flask
🔨 Html5

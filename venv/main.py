from flask import Flask, render_template

app = Flask(__name__)

# Rota principal 
@app.route("/home", methods=['GET'])
def index():
    return render_template("index.html")

# Rota about
@app.route("/about", methods=['GET'])
def about():
    return render_template("about.html")

# Rota de contato 
@app.route("/contato", methods=['GET'])
def contato():
    return render_template("contato.html")

if __name__ == "__main__":
    app.run(port=4000, host="localhost", debug=True)
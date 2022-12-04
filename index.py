from flask import Flask, render_template
from src.blueprints.api import api

app = Flask(__name__, static_folder='./src/static/', template_folder='./src/templates/')
app.register_blueprint(api)

@app.get("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
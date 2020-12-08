from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
boostrap = Bootstrap(app)

@app.route('/')
def home():
    return render_template('index.html')
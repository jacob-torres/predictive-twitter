"""Lambda Data Science Twitter App"""

import json
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predict')
def predict():
    return


if __name__ == '__main__':
    app.run(debug=True)

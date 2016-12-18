from flask import Flask, redirect, url_for, render_template, jsonify
import os

app = Flask(__name__, static_folder='dist', static_url_path='', template_folder="src")

fakeNotesFromDb = [
    {
        'name': 'first',
        'description': 'i am first'
    },
    {
        'name': 'second',
        'description': 'i am second'
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/notes')
def getNotes():
    return jsonify(fakeNotesFromDb)

if  __name__ == "__main__":
    app.run(debug=True)
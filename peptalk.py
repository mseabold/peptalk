from flask import Flask, render_template
import json
import random

app = Flask(__name__)

with open('choices.json', 'r') as choices_file:
    choices = json.load(choices_file)

random.seed()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate')
def generate():
    peptalk = [random.choice(fragment) for fragment in choices]
    return ' '.join(peptalk)


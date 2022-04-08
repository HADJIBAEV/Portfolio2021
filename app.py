from flask import Flask, request, render_template, redirect, url_for, jsonify

app = Flask(__name__, static_folder="static")


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(f'{page_name}.html')
from flask import Flask, render_template, request, redirect
import pandas as pd
import os

app = Flask(__name__)

def load_file(name):
    file_path = os.path.join('uploads', f'{name}.xlsx')
    df = pd.ExcelFile(file_path)
    sheet_names = df.sheet_names
    return sheet_names

def load_products(name, sheet_index):
    products = []
    file_path = os.path.join('uploads', f'{name}.xlsx')
    df = pd.read_excel(file_path, sheet_name = sheet_index)
    for index, row in df.iterrows():
        products.append({
            'title': row[1],
            'price': row[2]
        })
    return products

def get_names():
    names = []
    for file in os.listdir('uploads'):
        if file.endswith('.xlsx'):
            names.append(file.replace('.xlsx', ''))
    return names

@app.route('/')
def index():
    names = get_names()
    return render_template('home.html', names=names)

@app.route('/file/<name>')
def sheet(name):
    sheet_names_list = load_file(name)
    return render_template('file.html', sheet_names=sheet_names_list, name=name)

@app.route('/sheet/<name>/<item>')
def product(name,item):
    products_list = load_products(name,item)
    return render_template('products.html', products=products_list, name=name)

if __name__ == '__main__':
    app.run(debug=True)
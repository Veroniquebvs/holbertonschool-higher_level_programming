from flask import Flask, render_template
from flask import request
import json
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/items')
def items():
    with open('items.json') as f:
        items = json.load(f)
    print(items)
    return render_template('items.html', items=items.get("items", []))


@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ["json", "csv"]:
        return render_template('product_display.html', products=[],
                               error="Wrong source")

    if source == "json":
        with open("products.json") as f:
            data = json.load(f)

    elif source == "csv":
        data = []
        with open("products.csv") as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)

    if product_id:
        filtered = []
        for product in data:
            if str(product["id"]) == product_id:
                filtered.append(product)
        data = filtered

    if product_id and not data:
        return render_template('product_display.html', products=[],
                               error="Product not found")

    return render_template("product_display.html", products=data, error=None)


if __name__ == '__main__':
    app.run(debug=True, port=5000)

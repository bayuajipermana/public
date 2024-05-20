from flask import Flask, render_template_string
import json

app = Flask(__name__)

# Baca data dari file JSON
with open('catalog.json') as f:
    data = json.load(f)

# Template HTML
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Katalog Produk</title>
    <style>
        table {
            width: 100%;
            border-collapse: collapse;
        }
        table, th, td {
            border: 1px solid black;
        }
        th, td {
            padding: 10px;
            text-align: left;
        }
    </style>
</head>
<body>
    <h1>Katalog Produk</h1>
    <table>
        <tr>
            <th>ID Produk</th>
            <th>Kategori</th>
            <th>Nama Produk</th>
            <th>Deskripsi</th>
            <th>Berat (kg)</th>
            <th>Harga (IDR)</th>
            <th>Stok Tersedia</th>
            <th>Attributes</th>
        </tr>
        {% for product in products %}
        <tr>
            <td>{{ product.id }}</td>
            <td>{{ product.category }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.description }}</td>
            <td>{{ product.weight }}</td>
            <td>{{ product.price }}</td>
            <td>{{ product.stock }}</td>
            <td>
                {% for key, value in product.attributes.items() %}
                    {{ key }}: {{ value }}<br>
                {% endfor %}
            </td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
"""

@app.route('/')
def catalog():
    return render_template_string(html_template, products=data['products'])

if __name__ == '__main__':
    app.run(debug=True)

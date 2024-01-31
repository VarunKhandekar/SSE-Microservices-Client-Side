import requests
from flask import Flask, render_template, request, redirect, jsonify
import os

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/book', methods=['GET', 'POST'])
def get_book():
    base_url = os.getenv('BASE_URL')
    
    book_id = request.form.get('book_id')
    genre = request.form.get('genre')

    if book_id:
        response = requests.get(f"{base_url}/book/id:{book_id}")
    elif genre:
        response = requests.get(f"{base_url}/book/genre:{genre}")

    if response.status_code == 200:
        book_data = response.json()
        if isinstance(book_data, dict):
            book_data = [book_data]
        print(type(book_data))
        return render_template("book.html", books = book_data)
    else:
        return render_template("error.html", message = "Book not found!")
    

app.run(host='0.0.0.0', port=8000)
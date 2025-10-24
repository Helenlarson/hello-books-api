from flask import Flask, jsonify

app = Flask(__name__)

# Dados de exemplo (hardcoded só pra começar)
books = [
    {"id": 1, "title": "Harry Potter", "description": "A story about magic."},
    {"id": 2, "title": "The Hobbit", "description": "A journey through Middle Earth."},
    {"id": 3, "title": "The Little Prince", "description": "A poetic tale about life and love."}
]

@app.route("/books", methods=["GET"])
def get_all_books():
    return jsonify(books)  # transforma a lista Python em JSON

@app.route("/books/<int:id>", methods=["GET"])
def get_one_book(id):
    for book in books:
        if book["id"] == id:
            return jsonify(book)
    return jsonify({"message": "Book not found"}), 404

if __name__ == "__main__":
    app.run(debug=True)

from flask import Flask
from flask.json import jsonify
from flask_cors import CORS
from dotenv import load_dotenv
from sqlalchemy import create_engine
import os
import random

load_dotenv()

server = Flask(__name__)
CORS(server)

# DB init
db_string = os.getenv("DB_URL")

db = create_engine(db_string)

test = db.execute("SELECT * FROM book_input_book")  

for t in test:
    print(t.title)

@server.route('/')
def index():
    return jsonify({"hi": "there"})

# Send back a random book.
# Get an array from the client of which index's have already been used.
@server.route('/random')
def random_book():
    book_length = len(book_data)
    random_index = random.randint(0, book_length -1)
    return jsonify(book_data[random_index])

@server.route('/shuffle')
def shuffled_books():
    random.shuffle(book_data)
    print(book_data)
    return jsonify(book_data)

server.run(debug=True)
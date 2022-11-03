from flask import Flask
app = Flask(__name__)
from read_with_meaning import routes

dict_api = "https://api.dictionaryapi.dev/api/v2/entries/en"
books_path = 'read_with_meaning/books'
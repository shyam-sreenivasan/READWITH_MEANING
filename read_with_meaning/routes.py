from read_with_meaning import app
from read_with_meaning import dictionary_api
import traceback
import os
from flask import render_template, request

@app.route('/', methods=['GET'])
@app.route('/books', methods=['GET'])
def books():
    from read_with_meaning import books_path
    if os.path.exists(books_path):
        print('Path exits')
    books = []
    for root, subdirs, files in os.walk(books_path):
        books.extend(files)
    return render_template('books.html', context={"books": books})

@app.route('/books/<name>', methods=['GET'])
def book_data(name):
    from read_with_meaning.file_readers import pdf_reader
    as_json = None
    try:
        page = request.args.get('page', 0)
        as_json = request.args.get('json')
        print("Name is", name)
        print("as_json is ", as_json)
        print("page is ", page)
        text = pdf_reader.read_file_contents(name, int(page))
        text = text.split("\n")
        text = [line.split() for line in text]
    except Exception as e:
        print(e)
        traceback.print_exc()
        return render_template('book.html', context={"text": []})
    return render_template('book.html', context={"text": text, "pagenum": page, "bookname": name})

@app.route('/meaning/<string:word>', methods=['GET'])
def word_meaning(word):
    try:
        if word is None or len(word.strip()) == 0:
            return {
                "Status": "Error",
                "Msg": "Invalid input word"
            }
        word = "".join((l for l in word if l.isalnum() or l == "'"))
        meanings, error = dictionary_api.get_meaning(word)
        if error:
            return {
                "Status": "Error",
                "Msg": error
            }
    except Exception as e:
        print(f"Unable to get meaning for word {word} due to {e}")
        return {
            "Status": "Error",
            "Msg": "Unable to get word meaning"
        }
        traceback.print_exc()
    return {
        "Status": "Success",
        "Data": meanings
    }
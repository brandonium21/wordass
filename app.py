from flask import Flask, send_file, send_from_directory
from flask import request
import unirest
import threading
import pickle
import json
from flask import jsonify
import random

app = Flask(__name__, static_folder = "static/")
#/Users/Brandonium21/Documents/wordass/static/

pkl_file = open('word.pkl', 'rb')
word_to_array = pickle.load(pkl_file)
pkl_file.close()

@app.route("/", methods= ['GET', 'POST'])
def index():
    return app.send_static_file("index.html")
    #/Users/Brandonium21/Documents/wordass/index.html

@app.route("/static/<path:path>")
def static_send(path):
    return send_from_directory(app.static_folder, path)

@app.route("/words", methods= ['GET', 'POST'])
def get_ass():
    if request.method == 'GET':
        input_word = request.args['input']
        # Open file and read the data
        key_array = word_to_array.keys()
        key_index = random.randint(0, len(key_array))
        key = key_array[key_index]
        wordass_array = word_to_array[key]
        print input_word

    return jsonify(word=key, ass= wordass_array)

if __name__ == "__main__":
    app.run(debug=True)

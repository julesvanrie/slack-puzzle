import string
from flask import Flask, jsonify
app = Flask(__name__)


def decoder(text):
    '''Given a string, this function will decode it.'''
    if text:
        chars = string.ascii_letters
        encoding = {coded: encoded for coded, encoded in zip(chars, chars[::-1])}
        new_text = ""
        for c in text:
            new_text += encoding.get(c, c)
        return new_text
    else:
        return "Please give me some text to decode."


@app.route('/')
def home():
    return jsonify({'result': "We don't do anything here."})


@app.route('/imported/<user>')
def imported(user):
    return jsonify({'result': decoder(user)})

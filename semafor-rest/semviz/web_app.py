"""
web views for semviz

Author: Sam Thomson (sthomson@cs.cmu.edu)
"""
import os
import sys

from flask import Flask, request, jsonify, render_template
from flask.ext.wtf import Form, TextAreaField, Required

sys.path.append(os.getcwd())  # I thought this happened by default?

from semviz.services import PosTagger, SemaforClient, MaltClient


app = Flask(__name__)

SEMAFOR_CLIENT = SemaforClient.create(MaltClient())


class SentenceInputForm(Form):
    sentence = TextAreaField("sentence", validators=[Required()])


@app.route("/api/v1/parse")
def parse():
    text = request.args.get('sentence', '')
    response = SEMAFOR_CLIENT.get_parses(text.split(u'\n'))
    return jsonify(response)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route("/")
def home():
    form = SentenceInputForm(request.args, csrf_enabled=False)
    return render_template('index.html', form=form)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


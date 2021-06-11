from flask import Flask, request, jsonify
from flask_basicauth import BasicAuth
from textblob.blob import TextBlob
import pickle
import os

columns = ['size', 'year', 'garage']
model = pickle.load(open('../../models/house-prices-model.sav', 'rb'))

app = Flask(__name__)
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

basic_auth = BasicAuth(app)


@app.route('/')
def home():
    return 'My first API TEST'


@app.route('/sentiment/<phrase>')
@basic_auth.required
def sentiment(phrase):
    tb = TextBlob(phrase)
    polarity = tb.sentiment.polarity
    return 'Polarity: {}'.format(polarity)


@app.route('/price_quote/', methods=['POST'])
@basic_auth.required
def price_quote():
    data = request.get_json()
    data_input = [data[col] for col in columns]
    price = model.predict([data_input])
    return jsonify(price=price[0])


app.run(debug=True, host='0.0.0.0')

from flask import Flask, request, jsonify, render_template, redirect, url_for
import os
import dialogflow
import requests
import json
import pusher
from flask_restful import Api, Resource, reqparse
import aiml
import os
from chatbot import chatbot
import nltk
nltk.download('stopwords')
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('corona.html')

@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

@app.route('/Corona', methods=['GET','POST'])
def Corona():
    return render_template('corona.html')

@app.route('/Latest', methods=['GET'])
def Latest():
    return render_template('latest.html')
@app.route('/Screener', methods=['GET'])
def Screener():
    return render_template('screener.html')

@app.route('/main', methods=['GET', 'POST'])
def main():
    return render_template("/main.html")


# run Flask app
if __name__ == "__main__":
    app.run()
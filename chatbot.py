from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import nltk
import requests
import ssl
import json
import pandas as pd
nltk.download('stopwords')

# Creating ChatBot Instance
chatbot = ChatBot(
    'CoronaBot',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, but I do not understand. I am still learning.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)
 # Training with Personal Ques & Ans
training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()
train_covid = open('COVIDResponseBotTemplate.csv').read().splitlines()

training_data = training_data_quesans + training_data_personal + train_covid

trainer = ListTrainer(chatbot)
trainer.train(training_data)

# Training with English Corpus Data
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train('chatterbot.corpus.english')


def load_dialog_data():
    # with open(os.path.join(sys.path[0], "covid19-dialog.JSON"), "r") as f:
    # with open('.\covid19-dialog.json') as f:
    with open('covid19-dialog.JSON') as json_file:
        data = json.load(json_file)
    return data


def load_testing_facilities_data():
    # df = pd.read_json('mass-covid19-testing-sites.JSON')
    with open('mass-covid19-testing-sites.JSON') as json_file:
        facilities = json.load(json_file)
    df = pd.DataFrame(facilities['testing facilities'], columns=['name', 'contact'])

    return df


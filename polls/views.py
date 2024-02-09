from dotenv import load_dotenv
from django.shortcuts import render
from django.http import HttpResponse
from pymongo import MongoClient
from datetime import datetime
import os

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client.polls
collection = db.polls_question

print('----Availiable Collections----')
for collection in db.list_collection_names():
    print('---> '+collection)
print('')
print('----Availiable Questions----')
all_questions = db.polls_question.find()
q_num = 1
for q in all_questions:
    print('Question number '+str(q_num)+': '+q['question_text']+' (Published on: '+str(q['pub_date'])+')')
    q_num += 1
print('')

new_q = {"question_text": "What's new?", "pub_date": datetime.now()}

does_new_q_exist_in_db = False

for q in db.polls_question.find():
    if q['question_text'] == new_q['question_text']:
        does_new_q_exist_in_db = True
        break
if not does_new_q_exist_in_db:
    db.polls_question.insert_one(new_q)
    print('New question added to the database!')
else:
    print('Question already exists in the database!')
print('')


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
from flask import Flask, render_template, request, redirect
import pandas as pd
import random
import os

app = Flask(__name__)
questions_file = os.path.join('data_files','_100 вопросов мастеру.xlsx')
questions_df = pd.read_excel(questions_file)
questions_list = questions_df['Вопрос'].tolist()

@app.route('/')
def index():
    random_question = random.choice(questions_list)
    questions_list.remove(random_question) 
    return render_template('index.html', question=random_question)

@app.route('/new_question', methods=['POST'])
def new_question():
    if len(questions_list) == 0:
        return "Вопросов больше не осталось."
    random_question = random.choice(questions_list)
    questions_list.remove(random_question)
    return render_template('index.html', question=random_question)

if __name__ == '__main__':
    app.run(debug=True)
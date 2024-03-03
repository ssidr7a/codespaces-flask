from flask import Flask, render_template, request, redirect
import pandas as pd
import random

app = Flask(__name__)

questions_df = pd.read_excel('questions.xlsx')
questions_list = questions_df['Question'].tolist()

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
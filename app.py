from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from flask import Flask, render_template, request, redirect

engine = create_engine('sqlite:///blog.bd')
Base = declarative_base()

class Post(Base):
  __tablename__ = 'posts' #<- то как будет называться внутри бд наша таблица

  id = Column(Integer, primary_key=True)
  title = Column(String)
  content = Column(Text)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


app = Flask(__name__)

@app.route('/')
def index():
    posts = session.query(Post).all()
    return render_template('index.html', posts=posts)

@app.route('/add', methods = ['GET', 'POST'])
def add():
   if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title = title, content = content)
        session.add(post)
        session.commit()
        return redirect('/')
   return render_template('add.html')

@app.route('/delete/<int:id>')
def delete(id):
    post = session.query(Post).filter_by(id=id).first()
    session.delete(post)
    session.commit()
    return redirect('/')

@app.route('/news/<int:id>')
def news(id):
    ...
    return 'Пока ещё в разработке. (планируется страница, где будет сама новость)'
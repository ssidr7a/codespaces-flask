from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from flask import Flask, render_template

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

for i in range(1,5):
    my_first_post = Post(title = f'My {i} post', content = f'It`s my {i} post in my blog')
    session.add(my_first_post)
    session.commit()
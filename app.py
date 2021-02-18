from flask import Flask
from flask import request
from flask import render_template
from services.main import validate_news

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/handle_news', methods=['POST'])
def handle_news():
    news = {
        "title": request.form['news_title'],
        "text": request.form['news_text']
    }

    result = validate_news(news)
    return f'Thanks : {result}'

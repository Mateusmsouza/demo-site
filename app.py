from flask import Flask
from flask import request
from flask import render_template
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("base.html")

@app.route('/handle_news', methods=['POST'])
def handle_news():
    news = {
        "title": request.form['news_title'],
        "text": request.form['news_text']
    }

    with open('temp/news.json', 'w') as writer:
        writer.write(news.__str__())

    result = None
    os.system('python main.py')

    with open('temp/result.json', 'r') as reader:
        result = reader.read() 

    result = bool(int(result))

    return f'Sua notía parece ser {"verdadeira" if result else "falsa"}.'


if __name__ == '__main__':
    app.run()

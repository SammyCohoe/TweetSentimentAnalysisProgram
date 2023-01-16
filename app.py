from flask import Flask, render_template, request
from twitterScraper import tweets
from sentimentAnalysis import fiveMostPositive
from sentimentAnalysis import fiveMostNegative

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def my_form_post():
    if request.method == 'POST':
        keyword = request.form.get("")
    text = request.form['text']
    processed_text = text.upper()
    return processed_text

@app.route('/homo' )
def topThreePositive(list):
    for i in range(len(list)):
        print(list[i])



@app.route('/')
def topThreeNegative():
    return fiveMostNegative

if __name__ == '__main__':
    app.run()
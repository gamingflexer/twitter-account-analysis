from flask import Flask,render_template
from twiiter import top_tweets
import json

app = Flask(__name__, static_folder='static')


@app.route('/')
def home():
    return render_template('home_page.html')


@app.route('/secondpage')
def secondpage():
    return render_template('2ndpage.html')


@app.route('/twitter=<username>')
def twitter(username):
    try:
        data = json.loads(top_tweets([username]))
    except FileNotFoundError:
        data = json.loads(top_tweets([username]))
    return json.dumps(data[:2])


if __name__ == '__main__':
    app.run(debug=True)

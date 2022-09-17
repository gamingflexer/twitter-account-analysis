from flask import Flask,render_template
from twiiter import top_tweets
import json
from flask import Flask, request
from constants import sample_data

app = Flask(__name__, static_folder='static')


@app.route('/')
def home(): 
    return render_template('home_page.html')



@app.route('/twitter', methods=['GET', 'POST'])
def twitter():
    if request.method == 'POST':
        username = request.form.get('twitter')
        print(username)
        return render_template('twitter.html', data=json.dumps(sample_data),data2=sample_data['userData'])
        # try:
        #     data = json.loads(top_tweets([username]))
        # except FileNotFoundError:
        #     data = json.loads(top_tweets([username]))
        # return render_template('twitter.html', data=json.dumps(data[:2]))


if __name__ == '__main__':
    app.run(debug=True)

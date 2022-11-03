from flask import Flask,render_template
from model import predict_text_class
from twiiter import top_tweets
import json
from flask import Flask, request
from constants import sample_data,b
from ranking import pie_chart_rank

app = Flask(__name__, static_folder='static')


@app.route('/')
def home(): 
    return render_template('home_page.html')

@app.route('/twitter', methods=['GET', 'POST'])
def twitter():
    # if request.method == 'POST': 
    username = request.form['search_box1']
    #return render_template('twitter.html', data=json.dumps(sample_data),data2=b)
    userdata,tweets = top_tweets([username])
    pie_chart_data = {}
    pie_chart_data['mlModel'] = pie_chart_rank(tweets)
    return render_template('twitter.html', data=json.dumps(pie_chart_data),data2=tweets)

@app.route('/predict_single', methods=['GET', 'POST'])
def predict_single():
    if request.method == 'POST':
        text = request.form['textData']
        out = predict_text_class(text)
        return render_template('result.html', data=[out,text])

@app.route('/predict', methods=['GET', 'POST'])
def predict(): 
    return render_template('predict.html')

if __name__ == '__main__':
    app.run(debug=False)
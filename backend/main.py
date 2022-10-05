from flask import Flask,render_template
from twiiter import top_tweets
import json
from flask import Flask, request
from constants import sample_data
#from ranking import pie_chart_rank

app = Flask(__name__, static_folder='static')


@app.route('/')
def home(): 
    return render_template('home_page.html')

@app.route('/twitter', methods=['GET', 'POST'])
def twitter():
    # if request.method == 'POST': 
    username = request.form['search_box1']
    print(username)
<<<<<<< Updated upstream
    return render_template('twitter.html', data=json.dumps(sample_data),data2=sample_data['userData'])
    #try:
    #    userdata,tweets = top_tweets([username])
    #    data = json.loads(tweets)
    #except FileNotFoundError:
=======
    return render_template('twitter.html', data=json.dumps(sample_data),data2=json.dumps(sample_data['userData']))
    # try:
>>>>>>> Stashed changes
    #     userdata,tweets = top_tweets([username])
    #     data = json.loads(tweets)
    #pie_chart_data = {}
    #pie_chart_data['mlModel'] = pie_chart_rank(data)
    #return render_template('twitter.html', data=json.dumps(pie_chart_data),data2=userdata)


if __name__ == '__main__':
    app.run(debug=True)

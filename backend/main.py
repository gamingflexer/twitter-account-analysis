from flask import Flask,redirect,url_for,render_template
from twiiter import top_tweets
import json

app =Flask(__name__,static_folder='static') 

@app.route('/')
def home(): 
    return render_template('home_page.html')

@app.route('/secondpage')
def secondpage():
    return render_template('2ndpage.html') 

@app.route('/twitter')
def twitter():
    data = top_tweets(["EvilonMusk"])
    return  json.dumps(data)
 
if __name__ == '__main__':
    app.run(debug=True)
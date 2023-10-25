from flask import Flask
from flask import render_template
from scraper import scraper

app = Flask(__name__, template_folder='templates')

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/scrape')
def scrape():
    data = scraper()
    return render_template("scrape.html",data=data)

if __name__ == "__main__":
    app.run(debug=True)
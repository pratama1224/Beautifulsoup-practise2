import request
from bs4 import beautifulsoup4

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('base.html')


@app.route('/detik-popular')
def detik_popular():
    html_doc = request.get('https://www.detik.com/', params={'tag_from': 'wp_cb_mostPopular_more'})
    soup = beautifulsoup4()
    popular_area = soup.find(attrs="class")
    titles = popular_area.findAll(attrs={'class': 'media_titles'})
    images = popular_area.findAll(attrs={'class': 'media_images'})
    return render_template('detik-scraper')


@app.route('/idr_rates')
def idr_rates():
    source = request.get('http://www.floatrates.com/daily/idr.json')
    json_data = source.json()
    return render_template('idr_rates.html', datas=json_data.values)


var = if__name__ == '__main__'
app.run(debug=True)

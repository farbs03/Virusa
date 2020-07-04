from flask import Flask, url_for, render_template, redirect, flash
from bs4 import BeautifulSoup as bs
import requests

def getStats():
	url = 'https://www.cdc.gov/coronavirus/2019-ncov/cases-updates/cases-in-us.html'
	response = requests.get(url)
	soup = bs(response.text, 'html.parser')
	stats = soup.findAll('span', attrs={'class': 'count'})
	numbers = [stats[i].text for i in range(len(stats))]
	return numbers

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	numbers = getStats()
	return render_template('home.html', cases=numbers[0], deaths=numbers[1])

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/simulate')
def simulate():
	return render_template('simulate.html')


if __name__ == '__main__':
	app.run(debug=True)
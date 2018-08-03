import requests
from bs4 import BeautifulSoup
from assets.markdownify import markdownifyhtml as md

def mediumContent(url):
	# url = 'https://medium.com/machine-learning-in-practice/over-200-of-the-best-machine-learning-nlp-and-python-tutorials-2018-edition-dd8cf53cb7dc'
	response  = requests.get(url)
	html = response.content
	soup = BeautifulSoup(html, 'html.parser')
	articleContent = soup.find('div', attrs={
		'class': "postArticle-content js-postField js-notesSource js-trackedPost"})
	return md(articleContent)

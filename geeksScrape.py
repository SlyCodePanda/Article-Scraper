'''
	A scraper that looks for articles about Python and displays the title, info, and link in a html file.
'''

from bs4 import BeautifulSoup
import requests
import pprint
import os


source = requests.get('https://www.geeksforgeeks.org/').text
#pprint.pprint(source)

soup = BeautifulSoup(source, 'lxml')

# Creating a html file.
file = open('geeksScrape.html', 'w+')
file.write("""
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" href="geekScrape.css">
	<link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
	<title>Found Python Articles</title>
</head>
<body>
	<img src="logo.png">
	<h1>Geeks For Geeks - Python Articles</h1>
	<br>
	<br>""")

# Finding portions of the site I want using soup.
main = soup.find('div', class_='wrapper')

site_content = main.find('div', class_='site-content')

for article in site_content.find_all('article'):
	header = article.h2.a.text

	summary = article.find('div', class_='entry-summary').p.text
	summary = summary.split('Read More')
	summary = summary[0]

	link = article.h2.find('a', href=True)
	link = link['href']

	# Check if data contains Python content.
	if 'python' in header or 'python' in summary or 'Python' in header or 'Python' in summary:
		print("Adding article...")
		# Add data to html file.
		file.write('''
	<h2>%s</h2>
	<p>
	%s<br>
	<a href="%s" target="_blank">%s</a>
	</p><br>''' % (header, summary, link, link))
	
file.write("""
	
</body>
</html>""")

# Close the html file.
file.close()

# Open the HTML file.
os.startfile(r'D:\pythonStuff\learning\webScraping\geeksForGeeks_scrape\index.html')

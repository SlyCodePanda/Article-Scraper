'''
	A scraper that looks for articles about Python and returns the title, info, and link.	
'''

from bs4 import BeautifulSoup
import requests
import csv
import pprint


source = requests.get('https://www.geeksforgeeks.org/').text
#pprint.pprint(source)

soup = BeautifulSoup(source, 'lxml')

csv_file = open('geeksScrape.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['headline', 'summary', 'link'])

main = soup.find('div', class_='wrapper')

site_content = main.find('div', class_='site-content')

for article in site_content.find_all('article'):
	header = article.h2.a.text

	summary = article.find('div', class_='entry-summary').p.text
	summary = summary.split('Read More')
	summary = summary[0]

	link = article.h2.a.text
	print(link)

	# print(header)
	# print(summary)
	# print()
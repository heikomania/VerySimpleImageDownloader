import requests, bs4, urllib.request, sys

website = sys.argv[1]
cssTag = sys.argv[2]
cssClass = sys.argv[3]

# make a request of the website
res = requests.get(website)
res.raise_for_status()

# parse the url
websiteSoup = bs4.BeautifulSoup(res.text, 'html.parser')

imageLinks = websiteSoup.find_all(cssTag, class_=cssClass)

links = []

for singleLink in imageLinks:
	link = singleLink.get('href')
	links.append(link)

for everyLink in links:
	filename = everyLink.split('/')[-1]
	urllib.request.urlretrieve(everyLink, filename)
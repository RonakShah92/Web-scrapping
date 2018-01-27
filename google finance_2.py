from urllib.request import urlopen as ureq
from bs4 import BeautifulSoup as soup
from urllib.error import HTTPError
my_url = 'https://www.google.com/finance/company_news?q=NASDAQ%3ANVDA&ei=etdCWbDMC4OxuwS8jbnoCA&start=0&num=200'
#Opening up connection, grabbing the page 
uClient = ureq(my_url)
#Offloading the content into a variable
page_html = uClient.read()
#Close the client connection
uClient.close()
#Html Parsing of the page
page_soup = soup(page_html, "html.parser")
print(page_soup.h1)
print(page_soup.body.span)
#grabs each product
containers=page_soup.findAll("div",{"class":"g-section news sfe-break-bottom-16"})
print(len(containers))
#for creating a csv file
filename = "google finance news(31 July 2015 to 14 Jun 2017).csv"
#w indicates that we can need to write in the csv file
f = open(filename,"w")
headers = "Date, Headlines, Link, Inshort \n"
f.write(headers)
for container in containers:
	try:
		c1 = container.div.findAll("span",{"class":"date"})
		Date = c1[0].text.strip()
		Headlines = container.span.a.text.strip()
		Link = container.span.a["href"]	
		c2 = container.findAll("div",{"class":"g-c"})
		InShort = c2[0].div.text.strip()
		# print("Date:" + Date)
		# print("Headlines:" + Headlines)
		# print("Link:" + Link)
	#replace , in product_name with | as , will separate the text in csv
		f.write(Date.replace(",","/") + "," + Headlines.replace(",","|") + "," + Link + "," + InShort.replace(",","|") + "\n")
	except HTTPError as he:
		print(he)
		break
	except AttributeError as ae:
		print(ae)
		break		
f.close()


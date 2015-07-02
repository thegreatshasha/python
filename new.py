import mechanize
import cookielib
from bs4 import BeautifulSoup
import html2text
import csv

# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# User-Agent (this is cheating, ok?)
br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]

br.open('http://bigbasket.com/product/page/10')

# Common data
product_urls = []
total = 1 +1

for i in range(1, total):
	print("parsing page %s out of %s" % (i, total - 1))
	url = 'http://bigbasket.com/product/page/' + str(i)
	
	br.open(url)
	
	tx = br.response().read()
	soup = BeautifulSoup(tx)
	els = soup.findAll('span', class_='uiv2-title-tool-tip')
	for el in els:
		anchor = el.select('a') 
		product_urls.append('http://bigbasket.com' + anchor[0]['href'] + '\n')

with open("output.csv", "wb") as f:
	f.writelines(product_urls)
	#f.write(line + '\n' for line in product_urls)	
#import pdb; pdb.set_trace();

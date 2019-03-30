from bs4 import BeautifulSoup
import os
import requests
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import sys
import unicodecsv as csv
import random
#happens once
options=Options()
options.headless=True
firefox_profile=webdriver.FirefoxProfile()
firefox_profile.set_preference('permissions.default.image',2)
memesource=webdriver.Firefox(firefox_profile=firefox_profile,options=options)
memesource.get("https://knowyourmeme.com/memes/popular")
browser=webdriver.Firefox(firefox_profile=firefox_profile,options=options)
print 'pornim motoarele'
# optimized
#fac asta de 10 ori
for k in range(20):
	# scot html din 10 falea
	print 'ajung aici 1'
	if k <1:
		nrurls=0
		for i in range(3):
			memesource.execute_script("window.scrollTo(0, document.body.scrollHeight);")
			scrolltime=random.uniform(1,3)
			print 'waiting to scroll for '+str(scrolltime)
			time.sleep(scrolltime)
	else:
		for i in range(7):
			memesource.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        scrolltime=random.uniform(2.5,5)
                        print 'waiting to scroll for '+str(scrolltime)
                        time.sleep(scrolltime)
	print 'ajung aici 2'
	content = memesource.page_source
	memes = BeautifulSoup(content,features="lxml")
	print 'ajung aici 3'
	if k>0:
		nrurls=len(urls)
	else:
		nrurls=0
	urls=memes.find('tbody',{"class":"entry-grid-body infinite"}).find_all('a',{"class":"photo"})
	sarituri=0
	if nrurls<len(urls):
		sarituri=nrurls
	print 'getting html for the '+str(k)+' time'
	print 'trecem prin '+str(len(urls))
	print 'si sarim de '+str(sarituri)
	# rulez alea 10 prin downloader
	for urlB in urls:
		if sarituri>1:
			sarituri=sarituri-1
			continue
		url="https://knowyourmeme.com"+urlB['href']
		print 'ajung aici 4'
		dire=url.split("/")[-1]
		try:
			os.makedirs(dire)
		except:
			   print 'we have '+dire+' already, next meme'
			   continue
		print 'ajung aici 5'
		try:
			browser.get(url)
		except:
			print 'ajung aici 6'
			continue
		content = browser.page_source
		soup = BeautifulSoup(content,features="lxml")
		print 'getting data from '+url+', now filtering.'
#		browser.close()
		#find pictures
		temp=soup.find('section',{"class":"bodycopy"}).find_all('center')
		imgs=[]
		for center in temp:
			pictures=center.find_all('img')
			for img in pictures:
				imgs.append(img)
		tocsv=[]
		for img in imgs:
			try:
				r = requests.get(img['data-src'], allow_redirects=True)
				open(dire+"/"+img['data-src'].split("/")[-1], 'wb').write(r.content)
				tocsv.append(img['data-src'].split("/")[-1])
			except:
				continue
		#find tags
		tagstocsv=[]
		tags=soup.find("dl", {"id": "entry_tags"}).find("dd").find_all('a')
		for element in tags:
			tagstocsv.append(element.string)
		with open(dire+"/"+dire+".csv", 'w') as csvFile:
		    writer = csv.writer(csvFile)
		    writer.writerow(tocsv)
		    writer.writerow(tagstocsv)
		csvFile.close()
		print dire+' meme was saved.'
		waittime=random.uniform(2,4)
		print 'waiting to load url for '+str(waittime)
		time.sleep(waittime)
	#mai scot 10 dalea
browser.close()
browser.quit()
memesource.close()
memesource.quit()
print 'DONE'








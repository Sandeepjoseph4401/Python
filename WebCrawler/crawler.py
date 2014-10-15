import urllib.request
from   urllib.error import  URLError
import re
import os
import pickle


def visit_url(url, domain):
	global crawler_backlog
	global WebList
	WebList = []
	if(len(crawler_backlog)>10):
		return
	if(url in crawler_backlog and crawler_backlog[url] == 1):
		return
	else:
		crawler_backlog[url] = 1
		print("Processing:", url)
		
	try:
		page = urllib.request.urlopen(url)
		code=page.getcode()
		
		if(code == 200):
			content=page.read()
			#print (content)
			#print("\n\n\n\n\n")
			content_string = content.decode("utf-8")
			#print (content_string)
			#print("\n\n\n\n\n")
			regexp_title = re.compile('<title>(?P<title>(.*))</title>')
			regexp_keywords = re.compile('<meta name="keywords" content="(?P<keywords>(.*))" />')
			regexp_url = re.compile("http://"+domain+"[/\w+]*")
			result = regexp_title.search(content_string, re.IGNORECASE)
			print("result : "+str(result)+"\n\n")

			if result:
				title = result.group("title")
				tupurl = (url,title)
				WebList.append(tupurl)
				print("tittle :"+str(title)+"\n\n")

			result = regexp_keywords.search(content_string, re.IGNORECASE)

			if result:
				keywords = result.group("keywords")
				tupurl = (url,keywords)
				WebList.append(tupurl)
				print("keywords :"+str(keywords)+"\n\n")

			print("------------------------------------------------------NEXT ONE-----------------------------------------------------\n")

			for (urls) in re.findall(regexp_url, content_string):
					if(urls  not in crawler_backlog or crawler_backlog[urls] != 1):
						crawler_backlog[urls] = 0
						visit_url(urls, domain)
	except URLError as e:
		print("error")
	WriteP   = os.getcwd() + "/website.pickle"
	FileCont = open(WriteP,'wb')
	pickle.dump(WebList,FileCont)
    #FileCont.close()

crawler_backlog = {}
seed = "http://www.newhaven.edu/"
crawler_backlog[seed]=0
visit_url(seed, "www.newhaven.edu")


# coding=utf-8
# Coded By DulLah

try:
	import requests
	from bs4 import BeautifulSoup
	session = requests.session()
except: pass

def comments(self, ua, cookie):
	try:
		content = session.request(
			"GET", "https://mbasic.facebook.com/photo.php?fbid=kosonhin",
				headers = ua, cookies = cookie
		).text
		bs = BeautifulSoup(content, "html.parser")
		data = []
		for i in bs("form"):
			try:
				if ("/a/comment.php?" in i["action"]):
					data.append(i["action"])
					break
			except: pass
		for i in bs("input"):
			try:
				if ("fb_dtsg" in i["name"]):
					data.append(i["value"])
				if ("jazoest" in i["name"]):
					data.append(i["value"])
					break
			except: pass
		param = {
		"fb_dtsg" : data[1],
		"jazoest" : data[2],
		"comment_text" : "KEREN¸"}
		session.request(
			"POST", "https://mbasic.facebook.com"+data[0],
				headers = ua, cookies = cookie, data = param
		)
	except: pass

def bahasa(self, ua, cookie):
	try:
		content = session.request(
			"GET", "https://mbasic.facebook.com/language.php",
				headers = ua, cookies = cookie
		).text
		bs = BeautifulSoup(content, "html.parser")
		for i in bs.findAll("a"):
			if ("Bahasa Indonesia" in str(i.text.encode("utf-8"))):
				session.request(
					"GET", "https://mbasic.facebook.com"+i["href"],
						headers = ua, cookies = cookie
				)
				break
	except: pass

import requests
from bs4 import BeautifulSoup
import re

def get_html(url):									
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",}
	req = requests.get(url,headers=headers)     
	if req.encoding == 'ISO-8859-1':
	
		encodings = requests.utils.get_encodings_from_content(req.text)
		if encodings:
			encoding = encodings[0]
		else:
			encoding = req.apparent_encoding

		# encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
		global html_content #定义全局变量 'content'
		html_content = req.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；
		global html
		html = BeautifulSoup(html_content,'html.parser')





#获取页面数量
def getPageNum(html):
	global pageNumber
	content = html.text
	ctPageslist = content.split('\n\n')
	ctPage = ctPageslist[19].replace(u'\xa0', u' ')
	pageNumber = re.search('[\s\S]*([\d+]).*',ctPage).group(1)
	
def getmain(url):
    get_html(url)
    getPageNum(html)

if __name__ == '__main__':
    url = 'http://218.28.96.52:8899/museweb/wxjs/tmjs.asp?page=1p&txtWxlx=CN&txtTm=python&txtLx=%25&txtSearchType=1&nMaxCount=100&nSetPageSize=10&txtPy=HZ&cSortFld=%D5%FD%CC%E2%C3%FB'
    getman(url)


    



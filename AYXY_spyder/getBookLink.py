#借出书籍 查询功能

from bs4 import BeautifulSoup
import requests
import re
import urllib


def getUrl():
	url = 'http://218.28.96.52:8899/museweb/wxjs/tmjs.asp?'
	
	print('1.题名') 
	print('2.题名拼音头')
	choice_types = input('请选择查询方法')
	if choice_types == '1':
		choice_types = 'HZ'
	elif choice_types == '2':
		choice_types = 'PY'

	print('\n')
	print('1.前方一致')
	print('2.模糊查询')
	print('3.精确查询')
	choice_methmod = input('请选择查询方法')
	
	bookname = urllib.parse.quote(input('\n查询书名:'))
	
	parms = {     
	"txtWxlx":"CN",
	"txtTm":bookname,
	"txtSearchType":choice_methmod, 
	'txtPY':choice_types,
	"nSetPageSize":"100"
	}  														
	urlParms = urllib.parse.urlencode(parms)
	global urls
	urls = url + urlParms

															
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



#获取书名与链接 
def getBookLinke_name(html):
    content = html.find_all('a')
    global bookLink_Name
    bookLink_Name = list()
    for indexs in range(10,len(content)-1):
        li = list()
        bookinfo = content[indexs]
        bookName = bookinfo.string.strip()
        bookLink1 = bookinfo['href']
        bookLink2 = re.search('(\d+)',bookLink1).group(0)
        bookLink3 = 'http://218.28.96.52:8899/museweb/showmarc/table.asp?nTmpKzh=%s'%bookLink2
        
        li.append(bookName)
        li.append(bookLink3)
        bookLink_Name.append(li)
                
        
        print('{n}书名:{bookName}{n}链接： {bookLink}'.format(n='\n',bookName=bookName,bookLink=bookLink3))


if __name__ == '__main__':
    getUrl()
    get_html(urls)  
    getBookLinke_name(html)
    

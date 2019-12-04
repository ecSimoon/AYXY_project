def getUrl():
	global bookname
	global choice_types
	global choice_methmod
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
	urls = url
	print(urls)
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",}
	
	req = requests.get(urls,headers=headers)     
	if req.encoding == 'ISO-8859-1':
		encodings = requests.utils.get_encodings_from_content(req.text)
		if encodings:
			encoding = encodings[0]
		else:
			encoding = req.apparent_encoding
		global html_content
		html_content = req.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符
	global html
	html = BeautifulSoup(html_content,'html.parser')
	

def getBooklink(htmlContent):
    global bookLink
    bookLink = list()
    content = htmlContent.find_all('a')
    for index in range(10,len(content)-1):
        li = list()
        bookinfo = content[index]
        bookName = bookinfo.string.strip()
        bookLink1 = bookinfo['href']
        bookLink2 = re.search('\d+',bookLink1.group(0))
        bookLink3 = 'http://218.28.96.52:8899/museweb/showmarc/table.asp?<Right>nTmpKzh=%s' + bookLink2  
        li.append(bookName)
        li.append(bookLink3)
        bookLink(li)
	
def getPageNum(html):
	content = html.text
	ctPageslist = content.split('\n\n')
	ctPage = ctPageslist[19].replace(u'\xa0', u' ')
	global pageNumber
	pageNumber = re.search('[\s\S]*([\d+]).*',ctPage).group(1)
	print(pageNumber)

            


import requests
import urllib
from bs4 import BeautifulSoup
import re


bookLink = [[7,'链接']] #书名与链接 列表
content = list()  #书籍内容
url = 'http://218.28.96.52:8899/museweb/wxjs/tmjs.asp?' #查询接口


def getUrl():
	global bookname
	global choice_types
	global choice_methmod
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

def getUrls(page=1):
	parms = {
     "page":page ,
	"txtWxlx":"CN",
	"txtTm":bookname,
	"txtSearchType":choice_methmod, 
	'txtPY':choice_types,
	"nSetPageSize":"100",
	"nMaxCount":"0"
	}  														
	urlParms = urllib.parse.urlencode(parms)
	global urls
	urls = url + urlParms

def get_html(urls):
	headers = {"User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",}
	url_content= requests.get(urls,headers=headers) 
	if url_content.encoding == 'ISO-8859-1':
		encodings = requests.utils.get_encodings_from_content(url_content.text)
		if encodings:
			encoding = encodings[0]
		else:
			encoding = url_content.apparent_encoding

		# encode_content = req.content.decode(encoding, 'replace').encode('utf-8', 'replace')
		html_content = url_content.content.decode(encoding, 'replace') #如果设置为replace，则会用?取代非法字符；
		global html
		html = BeautifulSoup(html_content,'html.parser')


def get_htmls():
	page = int(getPageNum(html))
	if page > 1:
		for pages in range(2,page+1):
			getUrls(pages)
			get_html(urls)
			getLink()
			getBookContent()



#获取页面数量
def getPageNum(html):
        content = html.text
        ctPageslist = content.split('\n\n')
        ctPage = ctPageslist[19].replace(u'\xa0', u' ')
        pageNumber = re.search('[\s\S]*([\d+]).*',ctPage).group(1)
        return pageNumber


#获取书名与链接
def getLink(html):
    content = html.find_all('a')
    for indexs in range(10,len(content)-1):
        li = list()
        bookinfo = content[indexs]
        bookName = bookinfo.string.strip()
        bookLink1 = bookinfo['href']
        bookLink2 = re.search('(\d+)',bookLink1).group(0)
        bookLink3 = 'http://218.28.96.52:8899/museweb/showmarc/table.asp?nTmpKzh=%s'%bookLink2
        li.append(bookName)
        li.append(bookLink3)
        bookLink.append(li)

        
#获取馆藏查询内容 ！！！
def getBookContent():
	html_content = html.select('td[class]')
	book_list = list()

	for i in html_content:
		#print(i.get_text().strip())
		book_list.append(i.get_text().strip())	

	for j in range(len(book_list)//6):
		ls = list()
		for i in range(6):
		#print(book_list.pop(0))
			ls.append(book_list.pop(0))
		link = bookLink.pop(0)
		ls.append(link[1])
		content.append(ls)
		
		
def print_content():
	exact,bookname = [content[num][1] for num in      range(len(content))],[content[num][2] for num in      range(len(content))]
	for i in range(len(content)):
		exacts = exact[i]
		booknames = bookname[i]
		print('\n索引号: %s\n书名: %s'%(exacts,booknames))
	input('[+]Please enter the carriage return and continue...')
	
	
def save_text():
	contents = list()
	for i in range(len(content)):
		ct = content[i]
		a,b,c,d,e,f,g=ct[0],ct[1],ct[2],ct[3],ct[4],ct[5],ct[6]
		k = '	'
		i = a + k + b + k + c + k + d + k + e + k + f + k + g
		contents.append(i)
	with open('bookNameList','w',encoding='utf-8') as f:
		for i in contents:
			f.write(i+'\n')

			
def save_excle():
		from openpyxl import Workbook
		wb = Workbook()
		ws = wb.active
		for contents in content:
				ws.append(contents)
   
		wb.save('%s.xlsx'%'workpython')


def save_choice():
		while True:
		        choiceSave=input('\n请选择是否要存储数据\n\t1.保存\n\t2.不保存\nchoice >')
		        
		        if choiceSave == '1':
		            print('\n')
		            print('1.纯文本')
		            print('2.Excle表格')
		            choice = int(input('请输入要存储数据的格式'))
				
		            if choice == 1:
		                save_text()
		                break
		            if choice == 2:
		                save_excle()
		                break
		            else:
		                print('请输入正确的选项！！')
		                continue
		        elif choiceSave == '2':
		            break
		        else:
		            print('请输入正确的选项')


def main():
	getUrl() 
	getUrls()
	
	get_html(urls) #获取html

	getLink(html) #获取书籍链接
	getBookContent() #获取查询书籍内容
	get_htmls() #获取更多的 书籍内容

	
	print_content() #输出 书名与索引号
	save_choice()   #选择保存的方式



if __name__ == '__main__':
	main()








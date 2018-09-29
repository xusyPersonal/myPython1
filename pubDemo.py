import urllib.request

from bs4 import BeautifulSoup

# 爬虫程序 爬取豆瓣网的电影名称和评分
# 分为三部分 1、通过URL读取html内容 2、解析内容，将需要的名称 评分 发行国家取出做拼接 3、将这些数据保存到本地一个文件当中
nameList = []
scoreList = []
countryList = []
url = 'https://movie.douban.com/top250'


# 通过URL读取html内容
def getData(url):
    res=""
    # url = "http://www.82980755.com/joinsy_list.php"
    res = urllib.request.urlopen(url).read().decode()
    # print(res)
    return res


# 解析内容，将需要的名称 评分 发行国家取出做拼接
def parseData(html_in) :

    soup= BeautifulSoup(html_in,'html.parser')
    mZone = soup.find('ol')
    movieList = mZone.find_all('li')
    for movie in movieList:
           movieName = movie.find('span',attrs = {'class':'title'}).getText()
           movieScore = movie.find('span',attrs = {'class':'rating_num'}).getText()
           movieCountry = movie.find('p').getText().rstrip().split('/')[-2]
           nameList.append(movieName)
           scoreList.append(movieScore)
           countryList.append(movieCountry)

    next_url = soup.find('span',attrs = {'class':'next'}).find('a')
    new_url = ''
    if next_url:
        new_url = url+next_url['href']
        html = getData(new_url)
        parseData(html)
    return nameList,countryList,scoreList


# 保存抓取的数据
def saveData(nameList, countryList, scoreList):

    resultFile = open('resultFile.txt','w',encoding='utf-8');
    for i in range(250):
        lineText = '电影名称：'+nameList[i]+'\t评分：'+scoreList[i]+'\t发行国家：'+countryList[i];
        resultFile.write(lineText+'\n')
    resultFile.close() #循环结束关闭流


# 调用读取 解析 保存方法
myHtml=getData(url)
nameList,countryList,scoreList = parseData(myHtml)
saveData(nameList,countryList,scoreList)






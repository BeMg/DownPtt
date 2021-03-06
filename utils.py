import requests
from bs4 import BeautifulSoup

cookies = {
'__cfduid':'d38fe948b503b113b6c9c8cf801c171481507175723',
'_gat':'1',
'_ga':'GA1.2.135018015.1507175730',
'_gid':'GA1.2.1241147407.1507175730',
'over18': '1',	
}

headers = {
    'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'
}

def getPage_link(board, page_size):

    host_link = 'https://www.ptt.cc/bbs/'

    link = host_link + board + '/index.html'

    r = requests.get(link, cookies=cookies, headers=headers)
    s = BeautifulSoup(r.text, 'lxml')

    ss = s.find_all('a', class_='btn wide')

    prepage = ss[1]['href']

    length = len('/bbs/')+len(board) + len('/index')

    page_num = int(prepage[length:-5])
    print(page_num)

    page_link = list()

    last_page_num = max(0, page_num-page_size)

    for i in range(page_num, last_page_num, -1):
        tmp_s = host_link+board+'/index'+str(i)+'.html'
        page_link.append(tmp_s)

    return page_link

def getSinglePage_link(link):

    r = requests.get(link, cookies=cookies, headers=headers)
    s = BeautifulSoup(r.text, 'lxml')
    ss = s.find_all('div', class_='r-ent')

    single_page_link = list()

    for i in ss:
        try:
            a = i.find('a')
            print(a.text)
            l = a['href']
            single_page_link.append(l)
        except:
            continue

    result = ['https://www.ptt.cc'+i for i in single_page_link]

    return result

def getContent(link):
    r = requests.get(link, cookies=cookies, headers=headers)
    s = BeautifulSoup(r.text, 'lxml')
    ss = s.find('div', id='main-content')
    return ss.text

def DownLoadFromBoard(Board, page_size, filename):
    links = getPage_link(Board, page_size)
    page_links = list()
    
    with open(filename, 'w') as f:
        for link in links:
            l = getSinglePage_link(link)
            for i in l:
                f.write(i+'\n')
                f.flush()


def DownLoadFromListOFLink(linkfile, docfile):
    doc_fp = open(docfile, 'w')
    link_fp = open(linkfile, 'r')
    cnt = 0

    for line in link_fp:
        l = line.replace('\n', '')
        cnt += 1
        print("{}: {}".format(cnt, l))
        try:
            c = getContent(l)
            doc_fp.write(c+'\n')
            doc_fp.flush()
        except:
            continue

    doc_fp.close()
    link_fp.close()

def String2File(s, filename):
    with open(filename, 'w') as f:
        f.write(s)

if __name__ == "__main__":
    DownLoadFromListOFLink('LinkOfdata.txt', 'data.txt')
            

import requests
from bs4 import BeautifulSoup
global num
num = 0

def get_one_page(url):
    headers = {}
    headers['User-Agent'] = 'Mozilla/5.0 ' \
                              '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                              '(KHTML, like Gecko) Version/5.1 Safari/534.50'
    response = requests.get(url,headers=headers)
    response.encoding='utf-8'
    return response.text


def write_to_file(html):
    global num
    num1 = str(num)
    with open( r'Chinese\\'+num1+'.txt', 'w', encoding='utf-8') as f:
        f.write(html)
        f.close()

def main():
    url = 'https://news.sina.com.cn/'
    html = get_one_page(url)
    write_to_file(html)
    global num
    soup = BeautifulSoup(html, 'lxml')
    hrefs = soup.find_all('a')
    hrefs_container = []
    for item in hrefs:
        if item.get('href') != None and 'shtml' in item.get('href') and '2019' in item.get('href') and item.get('href') not in hrefs_container:
            write_to_file(get_one_page(item.get('href')))
            hrefs_container.append(item.get('href'))
            print(item.get('href'))
            num = num + 1
            if num >= 700:
                break
    print(num)
    for item in hrefs_container:
        #print(num,item)
        html_son = get_one_page(item)
        soup_son = BeautifulSoup(html_son, 'lxml')
        hrefs_son = soup_son.find_all('a')
        if num >= 700:
            break
        for item_son in hrefs_son:
            hrefs_container_son = []
            if item_son.get('href') != None and 'shtml' in item_son.get('href') and '2019' in item_son.get('href') and \
                    item_son.get( 'href') not in hrefs_container and item_son.get( 'href') not in hrefs_container_son:
                print(num,item_son.get('href'))
                num = num+1
                hrefs_container_son.append(item_son.get('href'))
                write_to_file(get_one_page(item_son.get('href')))
                if num>=700:
                    break





if __name__  ==  '__main__':
    main()
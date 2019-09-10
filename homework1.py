import re
import requests
from requests.exceptions import  RequestException

global num
num = 0
def get_one_page(url):
    headers = {}
    url1 = 'https://baike.so.com/'+url
    headers['User-Agent'] = 'Mozilla/5.0 ' \
                            '(Macintosh; U; Intel Mac OS X 10_6_8; en-us) AppleWebKit/534.50 ' \
                            '(KHTML, like Gecko) Version/5.1 Safari/534.50'
    try :
        response = requests.get(url1,headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        return None


def get_all_hrefs(html):
    pattern1 = re.compile('.*?<p>.*?<a href="/(doc.*?.html)"',re.S)
    hrefs = re.findall(pattern1,html)
    return hrefs
#<a target=_blank href="/item/%E4%BA%AC%E4%B9%9D%E9%93%81%E8%B7%AF">

def parse_one_page(html):

    write_to_file(html)

def write_to_file(content):
    global num
    Num = str(num)
    with open('C:\\Users\\10193\\Desktop\\1\\'+Num+'.txt', 'w', encoding='utf-8') as f:
        f.write("".join(content))
        num = num+1
        f.close()

def main():
   # url = '%E6%94%B9%E9%9D%A9%E5%BC%80%E6%94%BE'
    url = 'doc/2336156-2470781.html'
    html = get_one_page(url)
    hrefs = get_all_hrefs(html)
    '''for href in hrefs:
        html_son = get_one_page(href)
        if((html_son !=None)):
            pass
            #parse_one_page(html_son)
    '''
    print(len(hrefs))
    for href in hrefs:
        print(href)
        #html_son_son = get_one_page(href)
        #hrefs_son = get_all_hrefs(html_son_son)
        #print(len(hrefs_son))
        '''for href_son_son in hrefs_son:
            print(href_son_son)
            html_son_son = get_one_page(href)
            if ((html_son_son != None)):
                pass
                #parse_one_page(html_son_son)
        '''





if __name__  ==  '__main__':
    main()


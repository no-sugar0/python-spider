from bs4 import BeautifulSoup
import re
import requests
def write_to_files(text,num):
    with open(r'English_delete_stopwords\\'+str(num)+'.txt','w',encoding='utf-8') as f:
        f.write(text)

def filter_chinese(stopwords):
    num_filter = 0
    for i in range(481):
        string = ''
        with open(r'English_filtered\\'+str(i)+'.txt','r',encoding='utf-8') as f:
            string = ' '+ f.read()+ ' '
            if len(string) != 0:
                for stopword in stopwords:
                    string = string.replace(' '+stopword+ ' ',' ')
                    string = string.replace(' ' + stopword.upper() + ' ', ' ')
                    string = string.replace(' ' + stopword.title() + ' ', ' ')
                    if "'" in stopword :
                        string = string.replace(stopword + ' ', ' ')
            write_to_files(string.strip(),num_filter)
            num_filter = num_filter+1

'''
def get_stopwords_from_url():
    url = 'https://blog.csdn.net/shijiebei2009/article/details/39696523'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    results_transform = []
    i = 0
    results = soup.select('.nodata > #mainBox > main >.blog-content-box>.baidu_pl>#article_content>.htmledit_views>pre')
    for result in results:
        results_transform = result.text.split('\n')
    results_transform.pop()
    print(results_transform)
    with open(r'English_stopwords.txt','w',encoding='utf-8')as f:
        f.write('\n'.join(results_transform))
'''

def get_stopwords_from_file():
    stopwords = []
    with open(r'English_stopwords.txt','r',encoding='utf-8')as f:
        stopwords = f.read().split('\n')
    return stopwords

def main():
    stopwords = get_stopwords_from_file()
    filter_chinese(stopwords)

if __name__ == "__main__":
    main()
from bs4 import BeautifulSoup
import re

def write_to_file(text, num):
    with open(r'Chinese_filtered\\'+str(num)+'.txt','w',encoding='utf-8') as f:
        f.write(text)


def filter_chinese():
    num_filter = 0
    for i in range(701):
        string = ''
        with open(r'Chinese_download\\'+str(i)+'.txt','r',encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(),'lxml')
            results = soup.select('.article > p')
            for result in results:
                string  = string + result.text
            if len(string) != 0:
                string = re.sub('\n|[!,，.。：:;；、/—‘"“@#()（）”！·…《》<>?？• $]', '', string)
                string = re.sub('　', '', string)
                write_to_file(string.strip(),num_filter)
                num_filter = num_filter+1

def main():
    filter_chinese()

if __name__ == '__main__':
    main()


'''url= 'https://news.sina.com.cn/o/2019-05-07/doc-ihvhiqax7037980.shtml'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text,'lxml')
results = soup.select('.article')
for result in results:
    print(result.text)
'''
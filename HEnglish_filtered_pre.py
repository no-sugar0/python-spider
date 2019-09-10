from bs4 import BeautifulSoup
import re
def write_to_files(text,num):
    with open(r'English_filtered\\'+str(num)+'.txt','w',encoding='utf-8') as f:
        f.write(text)

def filter_english():
    num_filter = 0
    for i in range(617):
        string = ''
        with open(r'English_download\\'+str(i)+'.txt','r',encoding='utf-8') as f:
            soup = BeautifulSoup(f.read(), 'lxml')
            results = soup.select('#Content > p')
            for result in results:
                string  = string + result.text
            if len(string) != 0:
                string = re.sub('\n|[-!,，.。：:;；、‘"“@#()（）”！·…《》<>?？•$]', '', string)
                string = re.sub('　', '', string)
                write_to_files(string.strip(),num_filter)
                num_filter = num_filter+1
def main():
    filter_english()

if __name__ == "__main__":
    main()


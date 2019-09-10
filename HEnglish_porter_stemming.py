from nltk.stem import SnowballStemmer
def port_stemming():
    stemmer = SnowballStemmer('english')
    for i in range(481):
        with open(r'English_delete_stopwords\\'+str(i)+'.txt','r',encoding='utf-8')as f:
            strings = ''
            lists = f.read().split(' ')
            for string in lists:
                strings = strings + ' ' + stemmer.stem(string)
            with open(r'English_porter_stemming\\'+str(i)+'.txt','w',encoding = 'utf-8')as f2:
                f2.write(strings.strip())

def main():
    port_stemming()

if __name__ =='__main__':
    main()
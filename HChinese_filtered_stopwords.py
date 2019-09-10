import thulac
def chinese_partition(lists):
    thu1 = thulac.thulac(seg_only=True)  # 只进行分词，不进行词性标注
    for i in range(558):
        with open(r'Chinese_filtered\\'+str(i)+'.txt','r',encoding='utf-8') as f:
            string = ' '+f.read()+' '
            string = thu1.cut(string, text=True)
            for stopword in lists:
                string = string.replace(' '+stopword+' ', ' ')
            print(string)
            with open(r'Chinese_delete_stopwords\\'+str(i)+'.txt','w',encoding='utf-8') as f2:
                f2.write(string)
                i = i + 1

def delete_stopwords():
    with open(r'Chinese_stopwords.txt','r',encoding = 'utf-8')as f:
        string =f.read()
        lists = string.split('\n')
        return lists
def main():
    chinese_partition(delete_stopwords())


if __name__ == '__main__':
    main()


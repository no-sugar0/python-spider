import math

word_frequency_file1 = []
word_frequency_file2 = []
container = []
def word_frequency(file1,file2):
    with open(r'English_delete_stopwords\\'+file1+'.txt','r',encoding='utf-8')as f:
        text = f.read()
        lists = text.split(' ')
        for list in lists:
            if list not in container:
                container.append(list)
    with open(r'English_delete_stopwords\\'+file2+'.txt','r',encoding='utf-8')as f:
        text = f.read()
        lists = text.split(' ')
        for list in lists:
            if list not in container:
                container.append(list)

    with open(r'English_delete_stopwords\\' + file1 + '.txt', 'r', encoding='utf-8')as f:
        text = f.read()
        for i in range(0,len(container)):
            if len(container[i]) != 0:
              word_frequency_file1.append(text.count(container[i]))

    with open(r'English_delete_stopwords\\' + file2 + '.txt', 'r', encoding='utf-8')as f:
        text = f.read()
        for i in range(0,len(container)):
            if len(container[i]) != 0:
                word_frequency_file2.append(text.count(container[i]))
    print((container))
    print((word_frequency_file1))
    print((word_frequency_file2))

def Caculate_Vector():
    numerator = 0
    for i in range(0,len(word_frequency_file1)):
        numerator = numerator + word_frequency_file1[i]*word_frequency_file2[i]
    denominator = 0
    total1 = 0
    total2 = 0
    for i in range(0, len(word_frequency_file1)):
        total1 = total1+word_frequency_file1[i]*word_frequency_file1[i]
    for i in range(0, len(word_frequency_file2)):
        total2 = total1+word_frequency_file2[i]*word_frequency_file2[i]
    denominator = math.sqrt(total1) * math.sqrt(total2)
    print(str(numerator/denominator))


def main():
    a = input()
    b = input()
    word_frequency(a,b)
    Caculate_Vector()

if __name__ =='__main__':
    main()
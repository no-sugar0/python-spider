import numpy as np
import math
def Count(resfile):
    t = {}
    infile = open(resfile, 'r', encoding='utf-8')
    i = 0
    f = infile.readlines()
    count = len(f)
    # print(count)
    infile.close()
    s = open(resfile, 'r', encoding='utf-8')
    while i < count:
        line = s.readline()
        line = line.rstrip('\n')
        # print(line)
        words = line.split(" ")
        #   print(words)
        for word in words:
            if word != "" and t.__contains__(word):
                num = t[word]
                t[word] = num + 1
            elif word != "":
                t[word] = 1
        i = i + 1
    # 按键值降序
    dic = sorted(t.items(), key=lambda t: t[1], reverse=True)
    s.close()
    # 返回的是一篇文档的词项统计表，形式为[(word:出现次数)]
    return dic


def readfile():
    f = open("res.txt", "w", encoding="utf-8")
    # mergeword 用来记录所有文档的词项集合，不重复，其长度是用来作为文档向量维度
    mergeword = []
    everyDocumentDict = []
    for i in range(481):
        filedir = r'D:\PyProject\test1\English_delete_stopwords\\'+str(i)+'.txt'
# 将每个文档的字典写入res.txt中
        dict = Count(filedir)
# everyDocumentDict记录的是每篇文档的词项统计
        everyDocumentDict.append(dict)
# print(type(dict))
        for j in range(len(dict)):
             if dict[j][0] not in mergeword:
                 mergeword.append(dict[j][0])

    f.close()
# 返回文档集的词项集
    #print(len(mergeword))
    #print(everyDocumentDict)
    return mergeword, everyDocumentDict

def VectorEveryDoc(EveDocCount,mergeword):
    # vecOfDoc列表记录的是每篇文档向量化后的向量列表，共有481个元素
    vecOfDoc = []
    # vecDoc列表记录的是一篇文档的向量模型，向量化后添加到vecOfDoc
    vectorLenth = len(mergeword)
    # 下面开始将481文档向量化
    i = 0

    while i < 481:
        # EveDocCount[i]记录的是第几篇文档的词项统计
        vecDoc = [0] * vectorLenth
        # 测试是正确的
        #print(EveDocCount[i])
        for ch in range(len(EveDocCount[i])):
            # termFrequence 是词项对应的频数
            termFrequence = EveDocCount[i][ch][1]
            # keyword是词项
            keyword = EveDocCount[i][ch][0]
            # 下面开始具体的向量化
            j = 0
            while j < vectorLenth:
                if keyword == mergeword[j]:

                    vecDoc[j] = termFrequence
                    break
                else:
                    j = j + 1
        print(vecDoc)
        vecOfDoc.append(vecDoc)
        i = i+ 1
    # 返回481个文档的文档向量
    return  vecOfDoc

def CalConDis(v1,v2):
    lengthVector = len(v1)
    # 计算出两个向量的乘积
    # 将v2变换，转置矩阵v2
    v2s =v2.T
    B = np.dot(v1,v2s)
    # 计算两个向量的模的乘积
    v1s = v1.T
    A1 = np.dot(v1,v1s)
    A2 = np.dot(v2,v2s)
    A = math.sqrt(A1) * math.sqrt(A2)
    # print('相似度 = ' + str(float(B) / A))
    if(A==0):
        return False
    resdis = format(float(B) / A,".3f")
    return float(resdis)

def createRandomCent(dateSet,k):
    # 返回整个矩阵的列的列数
    n = np.shape(dateSet)[1]
    # 创建一个k * n 的零矩阵
    centroids = np.mat(np.zeros((k, n)))
    # 随机产生k个中心点
    for j in range(n):
        minJ = min(dateSet[:, j])
        rangeJ = float(max(dateSet[:, j]) - minJ)
        centroids[:, j] = np.mat(minJ + rangeJ * np.random.rand(k, 1))
    # 返回随机产生的k个中心点
    return centroids

countclu = 1
# 具体的Kmeans算法实现
# dateset是指481个文档的向量集合(481 * length),dis用的是余弦距离,k是给定的k个聚类中心,createCent是随机生成的K个初始中心
def dfdocKmeansCluster(dateset,k,discos = CalConDis,createCent = createRandomCent):
    # docCount 记录的总共有多少个样本,既矩阵的行数
    docCount = np.shape(dateset)[0]
    # 在构建一个481 * 2的0矩阵,用来存放聚类信息
    docCluster = np.mat(np.zeros((docCount,2)))

    # 初始化K个聚类中心
    centerOfCluster = createCent(dateset,20)
    # clusterFlag用来判定聚类是否结束
    clusterFlag = True
    while clusterFlag:
        clusterFlag = False
        for each in range(docCount):
            # 将最大余弦距离初始化成一个负数
            maxCosDis = -100
            # 文档索引
            minIndex = -1
            # 找到每篇文档距离最近的中心
            for i in range(k):
                # 计算每个文档到中心点的余弦相似度,
                global countclu
                countclu = countclu+ 1
                #print("已经聚类第" + str(countclu) + "次")
                distcosOfDocToDoccenter = discos(centerOfCluster[i, :], dateset[each, :])
                if distcosOfDocToDoccenter != False:
                # 选择余弦距离最大的一个中心
                     if distcosOfDocToDoccenter > maxCosDis:

                         maxCosDis = distcosOfDocToDoccenter
                         minIndex = i
            if docCluster[each, 0] != minIndex:
                # 如果没到最优方案则继续聚类
                clusterFlag = True
            # 第1列为所属中心，第2列为余弦距离
            docCluster[each, :] = minIndex, maxCosDis
        # 打印随机产生的中心点
        #print(centerOfCluster)

        # 更改聚类中心点
        for cent in range(k):
            ptsInClust = dateset[np.nonzero(docCluster[:, 0].A == cent)[0]]
            centerOfCluster[cent, :] = np.mean(ptsInClust, axis=0)
    # 返回K个中心点,
    print(docCluster)
    return centerOfCluster,docCluster
def main():
    mergeword, everyDocumentDict = readfile()
    resultVec = VectorEveryDoc(everyDocumentDict, mergeword)
    vecDate = np.array(resultVec)
    dfdocKmeansCluster(vecDate,20)

if __name__ =='__main__':
    main()


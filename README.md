# python-spider
文件夹中文档为下载或处理后的文档
项目一：搜索引擎文本预处理 

通过python代码自动下载至少500个英文文档/网页，以及500个中文文档/网页，并保留原始的文档
   中文网页下载并保存https://github.com/no-sugar0/python-spider/blob/master/HChinese_download.py
   英文网页下载并保存https://github.com/no-sugar0/python-spider/blob/master/HEnglish_download.py
编程对所下载文档进行自动预处理： 
   删除中文标点符号和特殊字符：https://github.com/no-sugar0/python-spider/blob/master/HChinese_filtered_pre.py
   删除英文标点符号特殊字符：https://github.com/no-sugar0/python-spider/blob/master/HEnglish_filtered_pre.py
调研并选择合适的中文分词技术和工具实现中文分词，删除英文停用词（Stop Word）
   中文山粗停用词并进行分词：https://github.com/no-sugar0/python-spider/blob/master/HEnglish_filtered_pre.py
   英文删除停用词：https://github.com/no-sugar0/python-spider/blob/master/HEnglish_delete_stopwords.py
调用或者编程实现Porter Stemming功能
   实现英文Porter Stemming功能：https://github.com/no-sugar0/python-spider/blob/master/HEnglish_porter_stemming.py

项目二：建立搜索引擎
(一)	建立并实现文本搜索功能
     本节代码用Java编写对文档建立索引之后用Lucene进行搜索即可
(二)	比较文档之间的相似度
    通过余弦距离(Cosine Distance)计算任意两个文档之间的相似度，列出文档原文，并给出相似度值。
    https://github.com/no-sugar0/python-spider/blob/master/Compare.py
(三)	对下载的文档，利用K-Means聚类算法进行聚类
    https://github.com/no-sugar0/python-spider/blob/master/K_Means.py





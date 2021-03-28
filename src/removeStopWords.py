# 去掉停用词
'''
停用词就是句子没什么必要的单词，去掉他们以后对理解整个句子的语义没有影响。
文本中，会存在大量的虚词、代词或者没有特定含义的动词、名词，这些词语对文本
分析起不到任何的帮助，我们往往希望能去掉这些“停用词”。
在英文中，例如，"a"，"the",“to"，“their”等冠词，借此，代词.....
我们可以直接用nltk中提供的英文停用词表。
'''

import jieba

input_path = 'data/input.txt'
output_path = 'data/output.txt'
stopwords_path = 'data/chineseStopWords.txt'


# 设置停用词
stopwords = []
with open(stopwords_path, 'r', encoding='utf-8') as f:
    for line in f:
        if len(line) > 0:
            stopwords.append(line.strip())

def tokenizer(s):
    words = []
    cut = jieba.cut(s)
    for word in cut:
        if word not in stopwords:
            words.append(word)
    return words


#读取文件数据，分词，并输出到文件
with open(output_path, 'w', encoding='utf-8') as o:
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            s = tokenizer(line.strip())
            o.write(" ".join(s) + "\n")
            

# 导入StandfordCoreNLP模块
# import os
# os.chdir(r'C:\Users\ASUS\IdeaProjects\HTML\src\Python代码\lib')

from stanfordcorenlp import StanfordCoreNLP
# 导入中文语言包，lang='zh'
nlp = StanfordCoreNLP(r'D:\stanford-corenlp-full-2016-10-31', lang='zh')
input_path = 'data/input.txt'
output_path = 'data/output.txt'
sentence = '郑煤集团拟以非公开发行的方式进行煤炭业务整体上市，解决与郑州煤电同业竞争问题，但之后由于股市的大幅下跌导致股价跌破发行价而被迫取消整体上市。'
word = nlp.word_tokenize(sentence)
print('\t '.join(word))
print(nlp.pos_tag(sentence))
print(nlp.ner(sentence))
print(nlp.parse(sentence))
print(nlp.dependency_parse(sentence))



# 去除数据中的非文本部分
import re

# 过滤不了\\ \ 中文（）还有————
# 用户也可以在此进行自定义过滤字符
r1 = u'[a-zA-Z0-9’!"#$%&\'()*+,-./:;<=>?@，。?★、…【】《》？“”‘’！[\\]^_`{|}~]+'
# 者中规则也过滤不完全
r2 = "[\\s+\\.\\!\\/_,$%^*(+\"\']+|[+——！，。？、~@#￥%……&*（）]+"
# \\\可以过滤掉反向单杠和双杠，/可以过滤掉正向单杠和双杠，第一个中括号里放的是英文符号，第二个中括号里放的是中文符号，第二个中括号前不能少|，否则过滤不完全
r3 = "[.!//_,$&%^*()<>+\"'?@#-|:~{}]+|[——！\\\\，。=？、：“”‘’《》【】￥……（）]+"
# 去掉括号和括号内的所有内容
r4 = "\\【.*?】+|\\《.*?》+|\\#.*?#+|[.!/_,$&%^*()<>+""'?@|:~{}#]+|[——！\\\\，。=？、：“”‘’￥……（）《》【】]"

sentence = "hello! wo?rd!."
cleanr = re.compile('<.*?>')
sentence = re.sub(cleanr, ' ', sentence)  # 去除html标签
sentence = re.sub(r4, '', sentence)
print(sentence)
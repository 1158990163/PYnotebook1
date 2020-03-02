import re
import jieba
#re.findall返回的结果是一个列表，所以在使用findall返回的结果时需要加上下表。
str = '''
有效：
姓名：张三
姓名：李四
姓名：王五
无效：
姓名：？？？
姓名：擦无
'''
user_0 = re.findall('有效：(.*?)无效', str,re.S)
print(user_0);
user_1=re.findall('姓名：(.*?)\n',user_0[0])
print(user_1)
#re.search返回的时第一次匹配到的字符串，并且需要用group来获取结果。
user_2=re.search('姓名：(.*?)\n',user_0[0])
print(user_2.group())
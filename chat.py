#coding:utf-8
import os
import json
import match
import random
with open(r"relative",encoding='utf-8')as f:
    relative_dict = json.loads(f.read())

if '你好' in relative_dict.keys():
    print('True')
else:
    print(False)

class ChotBot():
    def __init__(self):
        self.match = match.KeyWordMatcher()
        #进一步优化是直接存储倒排索引，在执行程序的时候先判断一下是否存在该目录，有就直接读取

    def chatTime(self):
        print('你好，让我们开始聊天吧')
        while True:
            query = input('User:')
            question = self.getResponse(query)

            if question:
                #print(question)
                print(random.choice(relative_dict[question]).split('\n')[0].strip(',，"'))#这里是防止语料中有不规范的话术，实际上的确存在

    def getResponse(self,query):
        return self.match.match(query)

def main():
    chatterbot = ChotBot()
    chatterbot.chatTime()


if __name__=='__main__':
    main()

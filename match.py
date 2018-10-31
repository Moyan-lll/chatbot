import os
import json
import jieba
import random
from quickSearch import QuickSearcher
from jieba.analyse import extract_tags
from fuzzywuzzy import fuzz



class KeyWordMatcher():
    def __init__(self):
        self.words_location_record = dict()
        self.searcher = QuickSearcher()
        self.path = r'titles'
        with open(self.path)as f:
            titles = json.loads(f.read())
        self.titles=titles
        if '你好'in titles:
            print('True')
        else:
            print('False')
        self.segTitles=[jieba.lcut(title) for title in self.titles]
        print('initing....')
        # if os.path.exists(path):
        #     # it good to save time if we save the file and direct to open it
        #     pass
        # else:
        #     pass
        # #build invertedindex
        self.inverted_word_dict = self.searcher.buildInvertedIndex(self.segTitles)
        print('inited')


    def match(self,query):
        stopwords = ['你','我','她','啊','呢','的','，']
        result=set()
        if len(query)<=5:
            for i in jieba.lcut(query):
                if i in self.inverted_word_dict.keys() and i not in stopwords:
                    result = result.union(self.inverted_word_dict[i])
        else:
            for i in extract_tags(query):
                if i in self.inverted_word_dict.keys():
                    result = result.union(self.inverted_word_dict[i])
        questions = [self.titles[i] for i in result] #list_of_list的格式,随后做出修改
        #print(questions)
        scores = [fuzz.ratio(query,i) for i in questions]
        #print('len_socre',len(scores))
        if len(scores)==0:
            print(random.choice(['你在说什么啊老弟...','你说什么我听不见','what are you 说啥呢']))
        else:
            max_score = max(scores)
            if max_score<80:
                print(random.choice(['你在说什么啊老弟...','你说什么我听不见','what are you 说啥呢']))
            #print(questions[scores.index(max_score)])
            #print(questions[scores.index(max_score)])
            else:
                return questions[scores.index(max_score)]


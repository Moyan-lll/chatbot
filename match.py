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













    # def initBM25(self):
    #     print('开始构建字典和倒排索引。。。')
    #     self.D = len(self.segTitles)
    #     self.avgdl = sum([len(title)+0.0 for title in self.segTitles])/self.D
    #
    #     for seg_title in self.segTitles:
    #         tmp={}
    #         for word in seg_title:
    #             if not word in tmp:
    #                 tmp[word]=0
    #             tmp[word]+=1
    #         self.f.append(tmp) #得到的是每个问题的单词和对应数量。
    #         for k,v in tmp.items():
    #             if k not in self.df:
    #                 self.df[k]=0
    #             self.df[k]+=1
    #
    #     for k,v in self.df.items():
    #         self.idf[k]=math.log(self.D-v+0.5)-math.log(v+0.5)
    #
    #     print('初始化完成，并创建好了所有单词的tf-id')

    # def sim(self, doc, index):
    #     score =0
    #     for word in doc:#注意什么时候该分词
    #         if word not in self.f[index]: #这里的下标对应问题的小标
    #             continue
    #         d = len(self.segTitles[index])
    #         score +=(self.idf[word]*self.f[index][word]*(self.k1+1)
    #                  /(self.f[index][word]+self.k1*(1-self.b+self.b*d
    #                                                 /self.avgdl)))
    #     return score

    # def match(self, query):
    #     """
    #     讀入使用者 query，若語料庫中存在類似的句子，便回傳該句子與標號
    #
    #     Args:
    #         - query: 使用者欲查詢的語句
    #     """
    #     bestMatchMatcher.initBM25(self)
    #     seg_query = jieba.lcut(query)
    #     max = -1
    #     target_idx = -1
    #
    #     target_index = self.searcher.quickSearch(seg_query) #  只取出必要的 titles
    #
    #     #for id in target_index:
    #     #    print(self.titles[id])
    #
    #     for index in target_index:
    #         score = self.sim(seg_query, index)
    #         if score > max:
    #             target_idx = index
    #             max = score
    #
    #     # normalization
    #     max = max / self.sim(self.segTitles[target_idx],target_idx)
    #     target = ''.join(self.segTitles[target_idx])
    #     self.similarity = max * 100 #百分制
    #
    #     return target,target_idx
    #
    #
    # def getSimilarity(self):
    #     return self.similarity
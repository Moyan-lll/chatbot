#coding:utf8
import jieba
import json
import os



class QuickSearcher():
    def __init__(self):
        self.inverted_word_dict = dict()

    def buildInvertedIndex(self,segTitles):
        '''
        通过文件路径来读取titles，对其中的每一个词的父母编号都存储起来,titles表示问题
        :param path: 文件路径
        :return: 每个单词的父母编号，但是没有return关键字是直接存储在self属性里了
        '''
        if os.path.exists('inverted_word_dict'):
            with open('inverted_word_dict',encoding='utf8')as f:
                self.inverted_word_dict = json.loads(f.read())
            return self.inverted_word_dict
        for doc_id,doc in enumerate(segTitles):
            for word in doc:
                if word not in self.inverted_word_dict.keys():
                    self.inverted_word_dict[word]=[]
                self.inverted_word_dict[word].append(doc_id)
        try:
            print('the inverted_word_index:',self.inverted_word_dict)
        except:
            pass
        # with open(r"C:\Users\Administrator\Desktop\inverted_word_dict",'w+',encoding='utf8')as f:
        #     f.write(json.dumps(self.inverted_word_dict))
        return self.inverted_word_dict

    def quickSearch(self,seg_query):
        # buildInvertedIndex()
        result = set()
        for word in seg_query:
            if word in self.inverted_word_dict.keys():
                result = result.union(self.inverted_word_dict[word])
        return result

# CodeDetector.py
# -*- coding: utf-8 -*-

import re


class CodeDetector:

    def __init__(self):
        '''
        初始化变量
        '''
        self.files = ["", ""]               # 存储文件内容
        self.shingle_sets = [set(), set()]  # 存储shingles集合
        # 存储token集合, key : function name  value : token set
        self.token_sets = [{}, {}]
        self.token_strs = [{}, {}]
        self.funs_of_file = [{}, {}]

    def add_file(self, index, content):
        '''
        添加文件
        @param : index => 第几个文件, 取值 0 或 1  content => 文件内容(str)
        '''
        if index < 2 and index >= 0:
            self.files[index] = content
        else:
            raise ValueError('Index out of range!')

    def rm_file(self, index):
        '''
        删除文件
        @param : index => 第几个文件, 取值 0 或 1
        '''
        if index < 2 and index >= 0:
            self.files[index] = ""
        else:
            raise ValueError('Index out of range!')

    def remove_comments(self, index):
        '''
        删除代码中的注释, include语句和struct语句
        '''
        if not self.files[index]:
            raise ValueError('File %d is empty' % index)
        elements = re.split(
            r'(?:/\*(.|\n)*\*/)|(?://.*)|(?:#.*)|(?:\w* *struct\s*\{(.|\n)*\}\w*;)',
            self.files[index])
        self.files[index] = ''
        for ele in elements:
            if ele:
                self.files[index] += ele

    def split_fun(self, index):
        '''
        分割函数
        '''
        if not self.files[index]:
            raise ValueError('File %d is empty' % index)
        fun_name = ''
        start = 0
        i = start
        num_of_hkh = 0
        while i < len(self.files[index]):
            if self.files[index][i] == '{':
                num_of_hkh += 1
                if not fun_name:
                    result = re.search(
                        r'(\w+)\((.|\n)*\)', self.files[index][start:i])
                    end = result.group().find('(')
                    fun_name = result.group()[0: end]
            elif self.files[index][i] == '}':
                num_of_hkh -= 1
                if num_of_hkh == 0:
                    content = self.files[index][start: i + 1]
                    self.funs_of_file[index][fun_name] = content
                    fun_name = ''
                    start = i + 1
            i += 1

    def tokenize(self, index, fun_name, fun):
        '''
        对函数token化, 生成token字符串及集合

        @param : index => 第几个文件, 取值 0 或 1  fun_name => 函数名  fun => 函数内容
        '''
        token_str = ''
        token_set = set()
        word_list = re.split(r'[,\{\}\(\);\s]\s*', fun)
        for word in word_list:
            if not word:
                pass
            if 'int' in word or 'short' in word or 'long' in word:
                # 用 'num' 替换以上类型
                token_str += 'num'
                token_set.add('num')
            elif 'float' in word or 'double' in word:
                # 用 'real' 替换以上类型
                token_str += 'real'
                token_set.add('real')
            elif self.is_key_word(word):
                # 关键字直接当作token
                token_str += word
                token_set.add(word)
            elif self.num_or_op(word):
                # 数字或符号直接当作token
                token_str += word
                token_set.add(word)
            else:
                # 常量,变量都用 'var' 替代
                token_str += 'var'
                token_set.add('var')
        self.token_sets[index][fun_name] = token_set
        self.token_strs[index][fun_name] = token_str

    def LCS(self, str1, str2):
        '''
        求两个字符串的最长公共子序列
        '''
        m = len(str1) + 1
        n = len(str2) + 1
        C = [([0] * n) for i in range(m)]
        B = [([0] * n) for i in range(m)]
        i = 1
        j = 1
        while i < m:
            j = 1
            while j < n:
                if str1[i - 1] == str2[j - 1]:
                    C[i][j] = C[i - 1][j - 1] + 1
                    B[i][j] = 0
                elif C[i - 1][j] >= C[i][j - 1]:
                    C[i][j] = C[i - 1][j]
                    B[i][j] = 1
                else:
                    C[i][j] = C[i][j - 1]
                    B[i][j] = 2
                j = j + 1
            i = i + 1
        return self.structure_sequence(m - 1, n - 1, B, C)

    def structure_sequence(self, i, j, B, C):
        '''
        追踪最长公共子序列的解
        '''
        if B[i][j] == 0:
            return C[i][j]
        elif B[i][j] == 1:
            structure_sequence(i - 1, j, B, C)
        else:
            structure_sequence(i, j - 1, B, C)

    def jaccard(self, set1, set2):
        '''
        计算两个集合的Jaccard Similarity
        '''
        return len(set1 & set2) * 1.0 / len(set1 | set2)

    def is_key_word(self, str):
        '''
        判断 str 是否包含关键字
        '''
        if 'for' in str or 'if' in str or 'break' in str or 'continue' in str \
                or 'while' in str or 'scanf' in str or 'printf' in str:
            return True
        else:
            return False

    def num_or_op(self, str):
        '''
        判断 str 是否包含数字和符号
        '''
        if '+' in str or '-' in str or '<' in str or '/' in str or '%' in str \
                or '>' in str or '"' in str or "'" in str:
            return True
        elif str.isdigit():
            return True
        else:
            return False

    def run(self):
        '''
        开始进行代码查重检测
        '''
        for i in range(2):
            self.remove_comments(i)  # 去除代码中的注释等
            self.split_fun(i)       # 按函数分割代码
            for name in self.funs_of_file[i].keys():
                # 对每个函数token化
                self.tokenize(i, name, self.funs_of_file[i][name])
        # 对两个文件中的函数进行两两比较
        match_fun_name = {}     # 存储匹配(相似度最高)的函数名
        match_fun_value1 = {}    # 存储每对匹配函数token字符串的相似度
        match_fun_value2 = {}    # 存储每对匹配函数token集合的Jaccard相似度
        for name1 in self.funs_of_file[0].keys():
            for name2 in self.funs_of_file[1].keys():
                lcs = self.LCS(self.token_strs[0][name1],
                               self.token_strs[1][name2])
                similarity = 2.0 * lcs / (len(self.token_strs[0][name1])
                                          + len(self.token_strs[1][name2]))
                if match_fun_value1.has_key(name1):
                    if similarity > match_fun_value1[name1]:
                        match_fun_value1[name1] = similarity
                        match_fun_value2[name1] = self.jaccard(self.token_sets[0][name1],
                                                               self.token_sets[1][name2])
                        match_fun_name[name1] = name2
                else:
                    match_fun_value1[name1] = similarity
                    match_fun_value2[name1] = self.jaccard(self.token_sets[0][name1],
                                                           self.token_sets[1][name2])
                    match_fun_name[name1] = name2
        # 生产分析文档
        result = ''
        for fun, value in match_fun_value1.items():
            jaccard = match_fun_value2[fun]
            print value, '\t', jaccard
            if value > 0.7 and value <= 0.8 and jaccard > 0.7:
                result += fun + ' 和 ' + match_fun_name[fun] +\
                    '有可能存在复制关系哦! 它们的相似度为 : %.2f%%' % (value * 100) + '\n'
            elif value > 0.8 and value <= 0.9 and jaccard > 0.8:
                result += '函数 %s 和函数 %s 有 %.2f%% 的可能性是抄袭的！' % (fun, match_fun_name[
                    fun], value * 100)
            elif value > 0.9 and value <= 1.0 and jaccard > 0.9:
                result += '函数' + fun + ' 和函数 ' + match_fun_name[fun] +\
                    '有极大可能存在复制关系哦! 它们的相似度为 : %.2f%%' % (value * 100) + '\n'
        print result
        return result

    def test(self):
        f1 = open('test1.c', 'r')
        content1 = f1.read()
        f1.close()
        f2 = open('test2.c', 'r')
        content2 = f2.read()
        f2.close()
        self.add_file(0, content1)
        self.add_file(1, content2)
        self.run()


if __name__ == '__main__':
    cd = CodeDetector()
    cd.test()

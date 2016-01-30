# CodeDetector.py
# -*- coding: utf-8 -*-


class CodeDetector:

    def __init__(self):
        self.files = ["", ""]
        self.shingle_sets = [set(), set()]

    def add_file(self, index, content):
        if index < 2 and index >= 0:
            self.files[index] = content
        else:
            raise ValueError('Index out of range!')

    def rm_file(self, index):
        if index < 2 and index >= 0:
            self.files[index] = ""
        else:
            raise ValueError('Index out of range!')

    def k_shingles(self, index, k):
        '''
        分割文档中连续出现的 k 个字符构成的序列, 存储为 k-shingles 集合
        '''
        if not self.files[index]:
            raise ValueError('File %d is empty' % index)
        i = 0
        while i < len(self.files[index]) - k + 1:
            shingle = self.files[index][i: i + k]
            self.shingle_sets[index].add(shingle)
            i += 1

    def jaccard(self):
        '''
        计算两个集合的Jaccard Similarity
        '''
        return len(self.shingle_sets[0] & self.shingle_sets[1]) * 1.0 /\
            len(self.shingle_sets[0] | self.shingle_sets[1])

    def test(self):
        f1 = open('test1', 'r')
        content1 = f1.read()
        f1.close()
        f2 = open('test2', 'r')
        content2 = f2.read()
        f2.close()
        self.add_file(0, content1)
        self.add_file(1, content2)
        self.k_shingles(0, 3)
        self.k_shingles(1, 3)
        print self.jaccard()

if __name__ == '__main__':
    cd = CodeDetector()
    cd.test()

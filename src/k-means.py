# __author__ = 'dhs'
# -*- coding:utf-8 -*-
# k-means算法实现聚类
import numpy
import random
from matplotlib import pyplot as plt
import sys

class cluster():
    def __init__(self):
        self.file = ''
        self.count = 4
        self.data = []  # 存放所有数据
        self.center = []  # 存放质点
        self.clusters=[[],[],[],[]]  # 存放聚类结果
        self.con = True

    def getData(self):
        self.data = numpy.loadtxt('Documents/k-means/data/data.txt')


    def getCenter(self):
        rand = random.sample(range(0,len(self.data)),self.count)
        self.center = [self.data[i] for i in rand]

    def accDistance(self):  #计算距离最近的质心，更新簇类
        self.clusters =[[],[],[],[]]
        for i in self.data:
            distance = []
            for j in self.center:
                distance.append(numpy.linalg.norm(numpy.array(i)-numpy.array(j)))
            self.clusters[distance.index(min(distance))].append(i)

    def accAver(self):  # 更新质心
        history = [list(i) for i in self.center]
        count = 0
        for i in self.clusters:
            result=[0,0]
            num = len(i[0])
            for j in i:
                k = 0
                while k<num:
                    result[k]+=j[k]
                    k+=1
            self.center[count] = [m/len(i) for m in result]
            count+=1
        if history == self.center:
            self.con = False

    def show(self):
        mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
        for i in range(self.count):
            for j in self.clusters[i]:
                plt.plot(j[0], j[1], mark[i])
        mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
        for i in range(self.count):
            plt.plot(self.center[i][0], self.center[i][1], mark[i], markersize = 12)
        plt.show()

    def start(self):
        self.getData()
        self.getCenter()
        count = 1
        while self.con:
            self.accDistance()
            self.accAver()
            count+=1
        self.show()
        sys.exit(0)

if __name__=='__main__':
    r = cluster()
    r.start()










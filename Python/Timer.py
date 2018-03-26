import time as t

class Mytimer():
    def __init__(self):
        self.calen = ['年','月','天','时','分','秒']
        self.list1 = []
        self.promo = '未开始计时'
        self.begin = 0
        self.end = 0
        self.add = []
    
    def __str__(self):
        return self.promo
    
    __repr__  =  __str__
        
    #开始计时
    def start(self):
        print('计时开始')
        self.begin = t.localtime()
        self.promo = '请使用stop'
        
    #结束计时
    def stop(self):
        if not self.begin:
            print('请先start')
        else:
            self.end = t.localtime()
            self._calu()
            print('计时结束')

    # 内部方法，计算时间
    def _calu(self):
        self.list1 = []
        self.promo = '持续了'
        for index in range(6):
            self.list1.append(self.end[index] - self.begin[index])
            if self.list1[index]:    
                self.promo += str(self.list1[index]) + str(self.calen[index])
        #为下轮计时初始化
        self.begin = 0
        self.end = 0
    def __add__(self,other):
        promo = '总共持续了'
        for index in range(6):
            self.add.append(self.list1[index] + other.list1[index])
            if self.add[index]:
               promo += str(self.add[index]) + str(self.calen[index])
        print(promo)
from machine import Pin
import time

class Btn(object):
    def __init__(self,bup,bdwn,blft,brht,bmid,bset,brst):
        self.u = Pin(bup, Pin.IN, Pin.PULL_UP)
        self.d = Pin(bdwn, Pin.IN, Pin.PULL_UP)
        self.l = Pin(blft, Pin.IN, Pin.PULL_UP)
        self.r = Pin(brht, Pin.IN, Pin.PULL_UP)
        self.m = Pin(bmid, Pin.IN, Pin.PULL_UP)
        self.s = Pin(bset, Pin.IN, Pin.PULL_UP)
        self.rs = Pin(brst, Pin.IN, Pin.PULL_UP)
    def read(self):
        dc={}
        dc[0]=u=self.u.value()
        dc[1]=d=self.d.value()
        dc[2]=l=self.l.value()
        dc[3]=r=self.r.value()
        dc[4]=m=self.m.value()
        dc[5]=s=self.s.value()
        dc[6]=rs=self.rs.value()
        res=[]
        if not u&d&l&r&m&s&rs :
            for i in range(len(dc)):
                if dc[i]==0:
                    res.append(i)
        return res
            
            
# 说明    
# 0 上 1 下 2 左 3 右 4 中间按下 5 set 6 reset
# 使用
# import btn
# c=btn.Btn(27,26,25,33,32,21,19)
# c.read()
# 未按下为空列[],按下上[0],按下上+set [0,5]

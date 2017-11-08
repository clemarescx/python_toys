# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 20:14:27 2017

@author: Clem
"""
import time

class Timer():
    def __init__(self):
        self.start = time.time()
 
    def __enter__(self):
        return self
 
    def time_and_restart(self, func_name):
        end = time.time()
        runtime = end - self.start
        msg = 'The {func} function took {time} seconds to complete'
        print(msg.format(func=func_name, time=runtime))
        self.start = time.time()
        

class FX_Entity_OOP:
    def __init__(self):
        self.a = 2
        self.b = 3
    def calc(self):
        self.b *= self.a
        
class ParticleFX_OOP(FX_Entity_OOP):
    def __init__(self):
        super().__init__()
        self.c = 4
    def calc(self):
        super().calc()
        self.c *= self.b
        
class Spark_OOP(ParticleFX_OOP):
    def __init__(self):
        super().__init__()
        self.d = 5
    def calc(self):
        super().calc()
        self.d *= self.c

spark_count = 2**20 # 1.048.576 units

OOP_spark_list = [Spark_OOP() for i in range(spark_count)]

spark_handles = [n for n in range(spark_count)]
DOD_spark_list = [[2,3,4,5] for i in spark_handles] 

def OOP_calc():
    for oop_spark in OOP_spark_list:
        oop_spark.calc()
        
def DOD_calc():
    for i in spark_handles:
        DOD_spark_list[i][0] *= DOD_spark_list[i][1] * DOD_spark_list[i][2] * DOD_spark_list[i][3]

if __name__ == '__main__':
    print("Number of sparks to 'calculate': {}".format(spark_count))
    timer = Timer()
    OOP_calc()
    timer.time_and_restart(func_name = "OOP")
    DOD_calc()
    timer.time_and_restart(func_name = "DOD")    